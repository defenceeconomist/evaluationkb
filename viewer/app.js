const state = {
  data: null,
  pageIndex: 0,
  zoom: 1,
  selectedId: null,
  viewMode: "layout",
  layerMode: "combined",
  visibleTypes: new Set(),
  hideFilterable: false,
  showOverflow: true,
  showBoxes: true,
  showImages: true,
  qaKind: "all",
  qaItems: [],
  matches: [],
  matchIndex: -1,
};

const els = {
  sourceMeta: document.querySelector("#sourceMeta"),
  searchInput: document.querySelector("#searchInput"),
  prevMatchBtn: document.querySelector("#prevMatchBtn"),
  nextMatchBtn: document.querySelector("#nextMatchBtn"),
  matchCount: document.querySelector("#matchCount"),
  typeFilters: document.querySelector("#typeFilters"),
  qaTabs: document.querySelector("#qaTabs"),
  qaNavList: document.querySelector("#qaNavList"),
  tocList: document.querySelector("#tocList"),
  firstPageBtn: document.querySelector("#firstPageBtn"),
  prevPageBtn: document.querySelector("#prevPageBtn"),
  pageInput: document.querySelector("#pageInput"),
  pageTotal: document.querySelector("#pageTotal"),
  nextPageBtn: document.querySelector("#nextPageBtn"),
  lastPageBtn: document.querySelector("#lastPageBtn"),
  viewModeSelect: document.querySelector("#viewModeSelect"),
  layerModeSelect: document.querySelector("#layerModeSelect"),
  hideFilterableToggle: document.querySelector("#hideFilterableToggle"),
  showOverflowToggle: document.querySelector("#showOverflowToggle"),
  showBoxesToggle: document.querySelector("#showBoxesToggle"),
  showImagesToggle: document.querySelector("#showImagesToggle"),
  zoomSlider: document.querySelector("#zoomSlider"),
  zoomOutput: document.querySelector("#zoomOutput"),
  pageStats: document.querySelector("#pageStats"),
  selectionSummary: document.querySelector("#selectionSummary"),
  pageStage: document.querySelector("#pageStage"),
  pageSurface: document.querySelector("#pageSurface"),
  elementInspector: document.querySelector("#elementInspector"),
};

const defaultDataPaths = [
  "../book_extracted.json",
  "/book_extracted.json",
  "./book_extracted.json",
];

async function init() {
  wireControls();
  setLoading("Loading book_extracted.json...");

  try {
    state.data = await loadBookData();
    initialiseState();
    renderAll();
  } catch (error) {
    setLoading(error.message);
  }
}

async function loadBookData() {
  const requestedPath = new URLSearchParams(window.location.search).get("data");
  const paths = requestedPath ? [requestedPath, ...defaultDataPaths] : defaultDataPaths;
  const errors = [];

  for (const path of paths) {
    try {
      const response = await fetch(path, { cache: "no-store" });
      const contentType = response.headers.get("content-type") || "unknown content type";
      const text = await response.text();

      if (!response.ok) {
        errors.push(`${path}: HTTP ${response.status}`);
        continue;
      }

      try {
        return JSON.parse(text);
      } catch (error) {
        const preview = text.trim().slice(0, 80).replace(/\s+/g, " ");
        errors.push(`${path}: ${error.message} (${contentType}; starts with "${preview}")`);
      }
    } catch (error) {
      errors.push(`${path}: ${error.message}`);
    }
  }

  throw new Error(`Unable to load book_extracted.json\n\nTried:\n${errors.join("\n")}`);
}

function wireControls() {
  els.firstPageBtn.addEventListener("click", () => goToPage(0));
  els.prevPageBtn.addEventListener("click", () => goToPage(state.pageIndex - 1));
  els.nextPageBtn.addEventListener("click", () => goToPage(state.pageIndex + 1));
  els.lastPageBtn.addEventListener("click", () => goToPage(state.data.pages.length - 1));

  els.pageInput.addEventListener("change", () => {
    const pageNumber = Number.parseInt(els.pageInput.value, 10);
    goToPage(pageNumber - 1);
  });

  els.viewModeSelect.addEventListener("change", () => {
    state.viewMode = els.viewModeSelect.value;
    renderPage();
    updateStats();
  });

  els.layerModeSelect.addEventListener("change", () => {
    state.layerMode = els.layerModeSelect.value;
    applyFilters();
    updateStats();
  });

  els.zoomSlider.addEventListener("input", () => {
    state.zoom = Number.parseInt(els.zoomSlider.value, 10) / 100;
    els.zoomOutput.textContent = `${Math.round(state.zoom * 100)}%`;
    renderPage();
  });

  els.hideFilterableToggle.addEventListener("change", () => {
    state.hideFilterable = els.hideFilterableToggle.checked;
    applyFilters();
    updateStats();
  });

  els.showOverflowToggle.addEventListener("change", () => {
    state.showOverflow = els.showOverflowToggle.checked;
    markOverflow();
    updateStats();
  });

  els.showBoxesToggle.addEventListener("change", () => {
    state.showBoxes = els.showBoxesToggle.checked;
    applyFilters();
    updateStats();
  });

  els.showImagesToggle.addEventListener("change", () => {
    state.showImages = els.showImagesToggle.checked;
    applyFilters();
    updateStats();
  });

  els.searchInput.addEventListener("input", () => {
    updateMatches();
    renderPage();
  });

  els.prevMatchBtn.addEventListener("click", () => stepMatch(-1));
  els.nextMatchBtn.addEventListener("click", () => stepMatch(1));

  els.qaTabs.addEventListener("click", (event) => {
    const button = event.target.closest("[data-kind]");
    if (!button) return;
    state.qaKind = button.dataset.kind;
    els.qaTabs.querySelectorAll(".qa-tab").forEach((tab) => tab.classList.toggle("active", tab === button));
    buildQaNav();
  });
}

function initialiseState() {
  const typeCounts = getTypeCounts();
  state.visibleTypes = new Set(Object.keys(typeCounts));
  els.sourceMeta.textContent = `${state.data.source.file_name} - ${state.data.source.page_count} pages`;
  els.pageInput.max = String(state.data.pages.length);
  els.pageTotal.textContent = `/ ${state.data.pages.length}`;
  buildTypeFilters(typeCounts);
  state.qaItems = collectQaItems();
  buildQaNav();
  buildToc();
  updateMatches();
}

function renderAll() {
  renderPage();
  updateStats();
  updateNav();
}

function setLoading(message) {
  els.pageSurface.innerHTML = `<div class="page-empty">${escapeHtml(message)}</div>`;
  els.pageSurface.style.width = "520px";
  els.pageSurface.style.height = "680px";
  els.elementInspector.textContent = message;
}

function getTypeCounts() {
  const counts = {};
  for (const page of state.data.pages) {
    for (const element of page.elements) {
      counts[element.type] = (counts[element.type] || 0) + 1;
    }
  }
  return counts;
}

function buildTypeFilters(typeCounts) {
  els.typeFilters.innerHTML = "";
  Object.entries(typeCounts)
    .sort(([a], [b]) => a.localeCompare(b))
    .forEach(([type, count]) => {
      const label = document.createElement("label");
      label.className = "check-pill";
      label.innerHTML = `
        <input type="checkbox" checked data-type="${escapeAttr(type)}">
        <span>${escapeHtml(type)} (${count})</span>
      `;
      label.querySelector("input").addEventListener("change", (event) => {
        if (event.target.checked) {
          state.visibleTypes.add(type);
        } else {
          state.visibleTypes.delete(type);
        }
        applyFilters();
        updateStats();
      });
      els.typeFilters.appendChild(label);
    });
}

function collectQaItems() {
  const items = [];
  for (const [pageIndex, page] of state.data.pages.entries()) {
    const elementsById = new Map(page.elements.map((element) => [element.id, element]));
    for (const element of page.elements) {
      if (element.type === "figure") {
        const caption = (element.caption_element_ids || []).map((id) => elementsById.get(id)).find(Boolean);
        items.push({
          kind: "figure",
          pageIndex,
          elementId: element.id,
          title: caption?.text || `Figure ${element.id}`,
        });
      } else if (element.type === "box") {
        const children = (element.child_text_element_ids || []).map((id) => elementsById.get(id)).filter(Boolean);
        items.push({
          kind: "box",
          pageIndex,
          elementId: element.id,
          title: children[0]?.text || `Box ${element.id}`,
        });
      } else if (element.type === "table") {
        const caption = (element.caption_element_ids || []).map((id) => elementsById.get(id)).find(Boolean);
        items.push({
          kind: "table",
          pageIndex,
          elementId: element.id,
          title: caption?.text || element.alt_text || `Table ${element.id}`,
        });
      }
    }
  }
  return items;
}

function buildQaNav() {
  els.qaNavList.innerHTML = "";
  const visibleItems = state.qaItems.filter((item) => state.qaKind === "all" || item.kind === state.qaKind);
  if (!visibleItems.length) {
    els.qaNavList.innerHTML = `<div class="muted">No items.</div>`;
    return;
  }

  for (const item of visibleItems) {
    const button = document.createElement("button");
    button.className = "qa-nav-item";
    button.type = "button";
    button.dataset.id = item.elementId;
    button.dataset.kind = item.kind;
    button.innerHTML = `
      <span class="qa-kind">${escapeHtml(item.kind)}</span>
      <span class="qa-title">${escapeHtml(item.title)}</span>
      <span class="qa-page">Page ${state.data.pages[item.pageIndex].page_number}</span>
    `;
    button.addEventListener("click", () => {
      state.pageIndex = item.pageIndex;
      state.selectedId = item.elementId;
      state.viewMode = "readable";
      els.viewModeSelect.value = "readable";
      renderAll();
      requestAnimationFrame(() => {
        const node = findRenderedNodeByElementId(item.elementId);
        node?.scrollIntoView({ block: "center", inline: "center" });
      });
    });
    els.qaNavList.appendChild(button);
  }
}

function buildToc() {
  els.tocList.innerHTML = "";
  for (const item of state.data.toc) {
    const button = document.createElement("button");
    button.className = "toc-item";
    button.dataset.page = String(item.page);
    button.style.setProperty("--toc-indent", `${Math.max(0, item.level - 1) * 14}px`);
    button.innerHTML = `
      <span class="toc-title">${escapeHtml(String(item.title || "").trim())}</span>
      <span class="toc-page">Page ${item.page}</span>
    `;
    button.addEventListener("click", () => goToPage(item.page - 1));
    els.tocList.appendChild(button);
  }
}

function goToPage(index) {
  if (!state.data) return;
  const bounded = Math.max(0, Math.min(index, state.data.pages.length - 1));
  state.pageIndex = bounded;
  state.selectedId = null;
  renderAll();
}

function renderPage() {
  if (!state.data) return;
  const page = state.data.pages[state.pageIndex];
  const width = Math.round(page.width * state.zoom);
  const height = Math.round(page.height * state.zoom);
  els.pageSurface.innerHTML = "";
  els.pageSurface.className = `page-surface mode-${state.viewMode}`;

  const fragment = document.createDocumentFragment();
  if (state.viewMode === "readable") {
    els.pageSurface.style.width = "";
    els.pageSurface.style.height = "";
    fragment.appendChild(renderReadablePage(page));
  } else {
    els.pageSurface.style.width = `${width}px`;
    els.pageSurface.style.height = `${height}px`;
    for (const element of page.elements) {
      fragment.appendChild(renderLayoutElement(element));
    }
  }
  els.pageSurface.appendChild(fragment);
  els.pageInput.value = String(page.page_number);
  updateInspector();
  applyFilters();
  markOverflow();
  updateNav();
  updateTocActive();
}

function renderLayoutElement(element) {
  const node = document.createElement("article");
  const [x0, y0, x1, y1] = element.render_bbox || element.bbox;
  node.className = `element element-${element.type}`;
  if (element.block_role) node.classList.add(`role-${element.block_role}`);
  if (element.render_layer) node.dataset.layer = element.render_layer;
  node.dataset.id = element.id;
  node.dataset.type = element.type;
  node.dataset.blockRole = element.block_role || element.role || "";
  node.dataset.filterable = String(Boolean(element.filterable));
  node.dataset.text = element.text || "";
  node.style.left = `${x0 * state.zoom}px`;
  node.style.top = `${y0 * state.zoom}px`;
  node.style.width = `${Math.max(1, (x1 - x0) * state.zoom)}px`;
  node.style.height = `${Math.max(1, (y1 - y0) * state.zoom)}px`;

  if (element.id === state.selectedId) node.classList.add("selected");
  if (isCurrentMatch(element)) node.classList.add("match");

  if (element.type === "figure" || element.type === "box" || element.type === "table") {
    const image = document.createElement("img");
    image.alt = element.alt_text || element.type;
    image.loading = "lazy";
    image.src = element.embedded_text;
    node.appendChild(image);
    const badge = document.createElement("span");
    badge.className = "type-badge";
    badge.textContent = element.type;
    node.appendChild(badge);
  } else {
    node.appendChild(renderTextElementContent(element));
  }

  node.addEventListener("click", (event) => {
    event.stopPropagation();
    state.selectedId = element.id;
    selectElementNode(node);
    updateInspector(element);
  });

  return node;
}

function renderTextElementContent(element) {
  const text = document.createElement("div");
  text.className = "element-text";
  text.textContent = element.text || "";
  text.style.fontSize = `${Math.max(5, (element.style?.font_size || 10) * state.zoom)}px`;
  if (element.block_role === "drop_cap") text.classList.add("drop-cap-text");
  return text;
}

function renderReadablePage(page) {
  const container = document.createElement("div");
  container.className = "readable-page";

  const heading = document.createElement("div");
  heading.className = "readable-page-heading";
  heading.textContent = `Page ${page.page_number}`;
  container.appendChild(heading);

  const readableItems = buildReadableItems(page);
  for (let index = 0; index < readableItems.length; index += 1) {
    const item = readableItems[index];
    if (item.type === "list_item") {
      const listItems = [item];
      let cursor = index + 1;
      while (cursor < readableItems.length && readableItems[cursor].type === "list_item" && readableItems[cursor].listKind === item.listKind) {
        listItems.push(readableItems[cursor]);
        cursor += 1;
      }
      container.appendChild(renderReadableList(listItems));
      index = cursor - 1;
    } else {
      container.appendChild(renderReadableItem(item));
    }
  }

  return container;
}

function buildReadableItems(page) {
  const elementsById = new Map(page.elements.map((element) => [element.id, element]));
  const consumed = new Set();
  const items = [];
  for (let index = 0; index < page.elements.length; index += 1) {
    const element = page.elements[index];
    if (consumed.has(element.id) || element.filterable) continue;

    if (isTableCaption(element)) {
      const table = page.elements.find((candidate) => candidate.type === "table" && (candidate.caption_element_ids || []).includes(element.id));
      const cells = table ? (table.child_text_element_ids || []).map((id) => elementsById.get(id)).filter(Boolean) : collectTableCells(page, element);
      const group = table ? [table, element, ...cells] : [element, ...cells];
      group.forEach((groupElement) => consumed.add(groupElement.id));
      items.push({
        id: table?.id || element.id,
        type: "table",
        blockRole: "table",
        text: group.map((groupElement) => groupElement.text || "").join(" "),
        table,
        caption: element,
        cells,
        elements: group,
      });
      continue;
    }

    if (isFigureCaption(element)) {
      const figure = page.elements.find((candidate) => candidate.type === "figure" && (candidate.caption_element_ids || []).includes(element.id));
      if (figure) {
        consumed.add(element.id);
        consumed.add(figure.id);
        for (const childId of figure.child_text_element_ids || []) consumed.add(childId);
        items.push({
          id: figure.id,
          type: "figure",
          blockRole: "figure",
          text: element.text || "",
          figure,
          caption: element,
          elements: [figure, element],
        });
        continue;
      }
    }

    if (element.type === "figure" || element.type === "table") {
      consumed.add(element.id);
      for (const childId of element.child_text_element_ids || []) consumed.add(childId);
      items.push({
        id: element.id,
        type: element.type,
        blockRole: element.block_role || element.type,
        text: "",
        figure: element,
        table: element.type === "table" ? element : null,
        caption: null,
        elements: [element],
      });
      continue;
    }

    if (element.type === "box") {
      const children = (element.child_text_element_ids || []).map((id) => elementsById.get(id)).filter(Boolean);
      consumed.add(element.id);
      children.forEach((child) => consumed.add(child.id));
      items.push({
        id: element.id,
        type: "box",
        blockRole: "box",
        text: children.map((child) => child.text || "").join(" "),
        box: element,
        children,
        elements: [element, ...children],
      });
      continue;
    }

    if (!element.text || element.block_role === "figure_text" || element.block_role === "box_text") continue;

    if (element.block_role === "drop_cap") {
      const group = [element];
      let cursor = index + 1;
      while (cursor < page.elements.length && group.length < 3 && page.elements[cursor].block_role === "body_text") {
        group.push(page.elements[cursor]);
        cursor += 1;
      }
      group.forEach((groupElement) => consumed.add(groupElement.id));
      items.push({
        id: group.map((groupElement) => groupElement.id).join("__"),
        type: "paragraph",
        blockRole: "chapter_opener",
        text: composeChapterOpenerText(group),
        elements: group,
      });
      index = cursor - 1;
      continue;
    }

    consumed.add(element.id);
    items.push({
      id: element.id,
      type: element.block_role === "list_item" ? "list_item" : element.type,
      blockRole: element.block_role || element.role || "",
      listKind: element.list_kind || "unordered",
      listMarker: element.list_marker || "",
      text: normaliseReadableText(element.text || "", element),
      elements: [element],
    });
  }
  return items;
}

function renderReadableItem(item) {
  if (item.type === "figure") return renderReadableFigure(item);
  if (item.type === "box") return renderReadableBox(item);
  if (item.type === "table") return renderReadableTable(item);
  return renderReadableTextItem(item);
}

function renderReadableList(items) {
  const kind = items[0]?.listKind === "ordered" ? "ol" : "ul";
  const node = setupReadableNode(document.createElement(kind), {
    id: items.map((item) => item.id).join("__"),
    type: "list",
    blockRole: "list",
    text: items.map((item) => item.text || "").join(" "),
    elements: items.flatMap((item) => item.elements),
  });
  node.classList.add("readable-list", `readable-list-${kind}`);
  if (kind === "ol") applyOrderedListMarker(node, items[0]?.listMarker || "");
  for (const item of items) {
    const listItem = document.createElement("li");
    listItem.textContent = stripListMarker(item.text || "");
    node.appendChild(listItem);
  }
  return node;
}

function setupReadableNode(node, item) {
  const firstElement = item.elements[0];
  node.classList.add("readable-element", `readable-${item.type}`);
  if (item.blockRole) node.classList.add(`role-${item.blockRole}`);
  node.dataset.id = item.id;
  node.dataset.ids = item.elements.map((itemElement) => itemElement.id).join(" ");
  node.dataset.type = item.type;
  node.dataset.blockRole = item.blockRole || "";
  node.dataset.filterable = String(Boolean(firstElement.filterable));
  node.dataset.text = item.text || "";
  if (item.elements.some((itemElement) => itemElement.id === state.selectedId)) node.classList.add("selected");
  if (item.elements.some((itemElement) => isCurrentMatch(itemElement))) node.classList.add("match");
  node.addEventListener("click", (event) => {
    event.stopPropagation();
    state.selectedId = firstElement.id;
    selectElementNode(node);
    updateInspector(firstElement);
  });
  return node;
}

function renderReadableTextItem(item) {
  const node = document.createElement(item.type === "heading" ? "h2" : "p");
  setupReadableNode(node, item);
  node.textContent = item.text || "";
  return node;
}

function renderReadableFigure(item) {
  const node = setupReadableNode(document.createElement("figure"), item);
  if (item.caption) {
    const caption = document.createElement("figcaption");
    caption.textContent = item.caption.text || "";
    node.appendChild(caption);
  }
  const image = document.createElement("img");
  image.alt = item.caption?.text || item.figure.alt_text || "Figure";
  image.loading = "lazy";
  image.src = item.figure.embedded_text;
  node.appendChild(image);
  return node;
}

function renderReadableBox(item) {
  const node = setupReadableNode(document.createElement("aside"), item);
  for (const child of item.children) {
    const paragraph = document.createElement(child.block_role === "heading" ? "h3" : "p");
    paragraph.textContent = child.text || "";
    node.appendChild(paragraph);
  }
  return node;
}

function renderReadableTable(item) {
  const node = setupReadableNode(document.createElement("section"), item);
  const caption = document.createElement("div");
  caption.className = "readable-table-caption";
  caption.textContent = item.caption?.text || item.table?.alt_text || "";
  if (caption.textContent) node.appendChild(caption);

  if (item.table?.embedded_text) {
    const image = document.createElement("img");
    image.className = "readable-table-image";
    image.alt = item.caption?.text || item.table.alt_text || "Table";
    image.loading = "lazy";
    image.src = item.table.embedded_text;
    node.appendChild(image);
    return node;
  }

  const cells = item.cells.filter((cell) => cell.text && /[^\s]/.test(cell.text));
  if (!cells.length) return node;

  const bbox = mergeReadableBbox(cells.map((cell) => cell.render_bbox || cell.bbox));
  const width = Math.max(1, bbox[2] - bbox[0]);
  const height = Math.max(1, bbox[3] - bbox[1]);
  const scale = Math.min(1.55, 620 / width);
  const table = document.createElement("div");
  table.className = "readable-table-layout";
  table.style.width = `${Math.ceil(width * scale)}px`;
  table.style.height = `${Math.ceil(height * scale)}px`;

  for (const cell of cells) {
    const [x0, y0, x1, y1] = cell.render_bbox || cell.bbox;
    const span = document.createElement("span");
    span.className = "readable-table-cell";
    span.textContent = cell.text || "";
    span.style.left = `${(x0 - bbox[0]) * scale}px`;
    span.style.top = `${(y0 - bbox[1]) * scale}px`;
    span.style.width = `${Math.max(8, (x1 - x0) * scale)}px`;
    span.style.minHeight = `${Math.max(8, (y1 - y0) * scale)}px`;
    table.appendChild(span);
  }

  node.appendChild(table);
  return node;
}

function collectTableCells(page, caption) {
  const startY = caption.bbox[3];
  const captionWideOrTall = caption.bbox[3] - caption.bbox[1] > 120 || caption.bbox[2] - caption.bbox[0] > page.width * 0.7;
  return page.elements.filter((element) => {
    if (!element.text || element.id === caption.id || element.filterable) return false;
    if (String(element.block_role || "").endsWith("_caption") || element.type === "heading") return false;
    if (captionWideOrTall) {
      return element.bbox[1] >= caption.bbox[1] - 2 && element.bbox[3] <= caption.bbox[3] + 2;
    }
    return element.bbox[1] >= startY - 2;
  });
}

function mergeReadableBbox(bboxes) {
  return [
    Math.min(...bboxes.map((bbox) => bbox[0])),
    Math.min(...bboxes.map((bbox) => bbox[1])),
    Math.max(...bboxes.map((bbox) => bbox[2])),
    Math.max(...bboxes.map((bbox) => bbox[3])),
  ];
}

function composeChapterOpenerText(elements) {
  if (!elements.length) return "";
  const [dropCap, firstLine, ...rest] = elements;
  const first = firstLine ? `${dropCap.text || ""}${firstLine.text || ""}` : dropCap.text || "";
  return [first, ...rest.map((element) => element.text || "")]
    .join(" ")
    .replace(/\s+/g, " ")
    .trim();
}

function normaliseReadableText(text, element) {
  if (element.block_role === "body_text" && /^[A-Z] [A-Z]{1,3}\b/.test(text)) {
    return text.replace(/^([A-Z])\s+([A-Z])/, "$1$2");
  }
  return text;
}

function stripListMarker(text) {
  return String(text || "").replace(/^(?:[•▪◦·]|[-–]|\d+[.)]|[a-zA-Z][.)])\s+/, "").trim();
}

function applyOrderedListMarker(node, marker) {
  const value = String(marker || "").replace(/[.)]$/, "");
  if (/^\d+$/.test(value)) {
    node.start = Number.parseInt(value, 10);
  } else if (/^[a-z]$/.test(value)) {
    node.type = "a";
    node.start = value.charCodeAt(0) - 96;
  } else if (/^[A-Z]$/.test(value)) {
    node.type = "A";
    node.start = value.charCodeAt(0) - 64;
  }
}

function selectElementNode(node) {
  els.pageSurface.querySelectorAll(".selected").forEach((selected) => selected.classList.remove("selected"));
  node.classList.add("selected");
}

function applyFilters() {
  const query = normalise(els.searchInput.value);
  for (const node of els.pageSurface.querySelectorAll(".element")) {
    const type = node.dataset.type;
    const blockRole = node.dataset.blockRole;
    const filterable = node.dataset.filterable === "true";
    const text = normalise(node.dataset.text);
    const typeVisible = state.visibleTypes.has(type);
    const filterableVisible = !(state.hideFilterable && filterable);
    const boxVisible = state.showBoxes || type !== "box";
    const imageVisible = state.showImages || (type !== "figure" && type !== "table");
    const layerVisible =
      state.layerMode === "combined" ||
      (state.layerMode === "images" && (type === "box" || type === "figure" || type === "table")) ||
      (state.layerMode === "text" && type !== "box" && type !== "figure" && type !== "table");
    const figureTextVisible = blockRole !== "figure_text" || state.layerMode === "text";
    const searchVisible = !query || text.includes(query) || type === "figure" || type === "box" || type === "table";
    node.classList.toggle(
      "filtered",
      !(typeVisible && filterableVisible && boxVisible && imageVisible && layerVisible && figureTextVisible && searchVisible),
    );
  }

  for (const node of els.pageSurface.querySelectorAll(".readable-element")) {
    const type = node.dataset.type;
    const filterable = node.dataset.filterable === "true";
    const text = normalise(node.dataset.text);
    const typeVisible = type === "table" || state.visibleTypes.has(type);
    const filterableVisible = !(state.hideFilterable && filterable);
    const boxVisible = state.showBoxes || type !== "box";
    const imageVisible = state.showImages || (type !== "figure" && type !== "table");
    const searchVisible = !query || text.includes(query);
    node.classList.toggle("filtered", !(typeVisible && filterableVisible && boxVisible && imageVisible && searchVisible));
  }
  markOverflow();
}

function markOverflow() {
  const overflows = [];
  for (const node of els.pageSurface.querySelectorAll(".element")) {
    node.classList.remove("overflow-risk");
    const text = node.querySelector(".element-text");
    if (!state.showOverflow || !text || node.classList.contains("filtered")) continue;
    const hasOverflow = text.scrollHeight > text.clientHeight + 1 || text.scrollWidth > text.clientWidth + 1;
    if (hasOverflow) {
      node.classList.add("overflow-risk");
      overflows.push(node.dataset.id);
    }
  }
  els.pageSurface.dataset.overflowCount = String(overflows.length);
}

function updateStats() {
  if (!state.data) return;
  const page = state.data.pages[state.pageIndex];
  const counts = {};
  for (const element of page.elements) {
    counts[element.type] = (counts[element.type] || 0) + 1;
  }
  const countText = Object.entries(counts)
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([type, count]) => `${type}: ${count}`)
    .join(" - ");
  const overflowCount = Number.parseInt(els.pageSurface.dataset.overflowCount || "0", 10);
  const overflowText = state.viewMode === "layout" ? ` - overflow risks: ${overflowCount}` : "";
  els.pageStats.textContent = `Page ${page.page_number}: ${page.elements.length} elements - ${countText}${overflowText}`;
}

function updateNav() {
  if (!state.data) return;
  const last = state.data.pages.length - 1;
  els.firstPageBtn.disabled = state.pageIndex === 0;
  els.prevPageBtn.disabled = state.pageIndex === 0;
  els.nextPageBtn.disabled = state.pageIndex === last;
  els.lastPageBtn.disabled = state.pageIndex === last;
}

function updateInspector(element) {
  const selected = element || getSelectedElement();
  if (!selected) {
    els.selectionSummary.textContent = "No element selected";
    els.elementInspector.textContent = "Select an element.";
    return;
  }
  const preview = { ...selected };
  if (preview.embedded_text) {
    preview.embedded_text = `${preview.embedded_text.slice(0, 80)}... (${selected.embedded_text.length} chars)`;
  }
  els.selectionSummary.textContent = `${selected.id} - ${selected.type} - ${selected.block_role || selected.role} - ${formatBbox(selected.bbox)}`;
  els.elementInspector.innerHTML = `
    <div class="inspector-summary">
      <div><strong>${escapeHtml(selected.id)}</strong> ${escapeHtml(selected.type)} / ${escapeHtml(selected.block_role || selected.role || "")}</div>
      <div>bbox: ${escapeHtml(formatBbox(selected.bbox))}</div>
      <div>render: ${escapeHtml(formatBbox(selected.render_bbox || selected.bbox))}</div>
      ${renderRelationButtons("Children", selected.child_text_element_ids)}
      ${renderRelationButtons("Captions", selected.caption_element_ids)}
      ${renderRelationButtons("Parents", selected.parent_box_element_ids)}
      ${renderRelationButtons("Figures", selected.parent_figure_element_ids)}
    </div>
    <pre>${escapeHtml(JSON.stringify(preview, null, 2))}</pre>
  `;
  els.elementInspector.querySelectorAll("[data-jump-id]").forEach((button) => {
    button.addEventListener("click", () => selectElementById(button.dataset.jumpId));
  });
}

function renderRelationButtons(label, ids) {
  if (!ids || !ids.length) return "";
  const buttons = ids
    .map((id) => `<button class="relation-button" type="button" data-jump-id="${escapeAttr(id)}">${escapeHtml(id)}</button>`)
    .join("");
  return `<div class="relation-row"><span>${escapeHtml(label)}:</span> ${buttons}</div>`;
}

function findRenderedNodeByElementId(id) {
  return Array.from(els.pageSurface.querySelectorAll("[data-id], [data-ids]")).find((node) => {
    if (node.dataset.id === id) return true;
    return (node.dataset.ids || "").split(/\s+/).includes(id);
  });
}

function selectElementById(id) {
  const page = state.data.pages[state.pageIndex];
  const element = page.elements.find((candidate) => candidate.id === id);
  if (!element) return;
  state.selectedId = id;
  const node = findRenderedNodeByElementId(id);
  if (node) {
    selectElementNode(node);
    node.scrollIntoView({ block: "center", inline: "center" });
  }
  updateInspector(element);
}

function getSelectedElement() {
  if (!state.selectedId) return null;
  const page = state.data.pages[state.pageIndex];
  return page.elements.find((element) => element.id === state.selectedId) || null;
}

function updateMatches() {
  const query = normalise(els.searchInput.value);
  state.matches = [];
  state.matchIndex = -1;
  if (query) {
    state.data.pages.forEach((page, pageIndex) => {
      page.elements.forEach((element) => {
        if (element.text && normalise(element.text).includes(query)) {
          state.matches.push({ pageIndex, elementId: element.id });
        }
      });
    });
  }
  els.matchCount.textContent = `${state.matches.length} ${state.matches.length === 1 ? "match" : "matches"}`;
  els.prevMatchBtn.disabled = state.matches.length === 0;
  els.nextMatchBtn.disabled = state.matches.length === 0;
}

function stepMatch(direction) {
  if (!state.matches.length) return;
  state.matchIndex = (state.matchIndex + direction + state.matches.length) % state.matches.length;
  const match = state.matches[state.matchIndex];
  state.pageIndex = match.pageIndex;
  state.selectedId = match.elementId;
  renderAll();
  requestAnimationFrame(() => {
    const node = findRenderedNodeByElementId(match.elementId);
    node?.scrollIntoView({ block: "center", inline: "center" });
  });
}

function isCurrentMatch(element) {
  if (state.matchIndex < 0) return false;
  const match = state.matches[state.matchIndex];
  return match && match.pageIndex === state.pageIndex && match.elementId === element.id;
}

function updateTocActive() {
  const currentPage = state.pageIndex + 1;
  let active = null;
  for (const button of els.tocList.querySelectorAll(".toc-item")) {
    const page = Number.parseInt(button.dataset.page, 10);
    button.classList.remove("active");
    if (page <= currentPage) active = button;
  }
  active?.classList.add("active");
}

function normalise(value) {
  return String(value || "").toLowerCase().replace(/\s+/g, " ").trim();
}

function isTableCaption(element) {
  return element.block_role === "table_caption";
}

function isFigureCaption(element) {
  return /^(figure|fig\.)\s+\d+(?:\.\d+)?\b/i.test((element.text || "").trim());
}

function formatBbox(bbox) {
  return bbox.map((value) => Math.round(value)).join(", ");
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function escapeAttr(value) {
  return escapeHtml(value).replaceAll("`", "&#096;");
}

els.pageSurface.addEventListener("click", () => {
  state.selectedId = null;
  els.pageSurface.querySelectorAll(".selected").forEach((selected) => selected.classList.remove("selected"));
  updateInspector();
});

init();
