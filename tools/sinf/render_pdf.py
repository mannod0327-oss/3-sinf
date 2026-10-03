"""PDF renderer (ReportLab) — child-friendly A4 pages set in Andika."""
from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, KeepTogether, PageBreak as RLPageBreak, PageTemplate,
    Image as RLImage, Paragraph, Spacer as RLSpacer, Table as RLTable, TableStyle,
)
from reportlab.platypus.flowables import HRFlowable

from . import icons
from .markup import strip, tokenize
from .model import (
    Block, Box, Bullets, Doc, Group, Heading, Lines, PageBreak, Para, Rule, Spacer, Table,
)

FONT_DIR = Path(__file__).resolve().parent.parent / "assets" / "fonts"
# DejaVu only supplies the few symbols Andika lacks; on machines without it Andika is used instead.
_DEJAVU_DIRS = ["/usr/share/fonts/truetype/dejavu", "/usr/share/fonts/dejavu", "/usr/share/fonts/TTF",
                "/Library/Fonts", "/System/Library/Fonts/Supplemental", "C:/Windows/Fonts"]


def _find_font(name: str, fallback: Path) -> str:
    for folder in _DEJAVU_DIRS:
        if (Path(folder) / name).exists():
            return str(Path(folder) / name)
    return str(fallback)


DEJAVU = _find_font("DejaVuSans.ttf", FONT_DIR / "Andika-400.ttf")
DEJAVU_BOLD = _find_font("DejaVuSans-Bold.ttf", FONT_DIR / "Andika-700.ttf")

PRIMARY = colors.HexColor("#1B6CA8")
ACCENT = colors.HexColor("#E8871E")
LIGHT = colors.HexColor("#EAF3FB")
SOFT = colors.HexColor("#F6F6F6")
BANK = colors.HexColor("#FFF6E0")
KEYRED = colors.HexColor("#B3261E")
GRID = colors.HexColor("#9FB3C8")
INK = colors.HexColor("#1F2933")

BOX_COLORS = {
    "note": (LIGHT, PRIMARY),
    "tip": (colors.HexColor("#EAF7EA"), colors.HexColor("#2E7D32")),
    "bank": (BANK, ACCENT),
    "grammar": (colors.HexColor("#F2EBFA"), colors.HexColor("#6A3FA0")),
    "answer": (colors.HexColor("#FDECEA"), KEYRED),
    "script": (colors.HexColor("#FDECEA"), KEYRED),
    "draw": (colors.white, GRID),
}

_FONTS_READY = False
_ANDIKA_GLYPHS: set[int] = set()


def _setup_fonts() -> None:
    global _FONTS_READY, _ANDIKA_GLYPHS
    if _FONTS_READY:
        return
    pdfmetrics.registerFont(TTFont("Andika", str(FONT_DIR / "Andika-400.ttf")))
    pdfmetrics.registerFont(TTFont("Andika-Bold", str(FONT_DIR / "Andika-700.ttf")))
    pdfmetrics.registerFont(TTFont("Andika-Italic", str(FONT_DIR / "Andika-400-italic.ttf")))
    pdfmetrics.registerFont(TTFont("Andika-BoldItalic", str(FONT_DIR / "Andika-700-italic.ttf")))
    pdfmetrics.registerFontFamily("Andika", normal="Andika", bold="Andika-Bold",
                                  italic="Andika-Italic", boldItalic="Andika-BoldItalic")
    pdfmetrics.registerFont(TTFont("DejaVu", DEJAVU))
    pdfmetrics.registerFont(TTFont("DejaVu-Bold", DEJAVU_BOLD))
    pdfmetrics.registerFontFamily("DejaVu", normal="DejaVu", bold="DejaVu-Bold",
                                  italic="DejaVu", boldItalic="DejaVu-Bold")
    _ANDIKA_GLYPHS = set(pdfmetrics.getFont("Andika").face.charToGlyph.keys())
    _FONTS_READY = True


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _font_safe(s: str) -> str:
    """Escape ``s`` and route glyphs Andika lacks (ticks, arrows…) to DejaVu."""
    s = re.sub(r" {2,}", lambda m: " " + "\u00a0" * (len(m.group()) - 1), s)  # keep runs of spaces
    out: list[str] = []
    fallback = False
    for ch in s:
        ok = ord(ch) in _ANDIKA_GLYPHS or ch in "\n\t \u00a0"
        if not ok and not fallback:
            out.append('<font name="DejaVu">')
            fallback = True
        elif ok and fallback:
            out.append("</font>")
            fallback = False
        out.append(_esc(ch))
    if fallback:
        out.append("</font>")
    return "".join(out)


def rl_text(text: str, icon_pt: float = 15.0) -> str:
    """Convert inline markup to ReportLab paragraph XML."""
    _setup_fonts()
    parts: list[str] = []
    for tok in tokenize(text):
        if tok.kind == "text":
            parts.append(_font_safe(tok.value))
        elif tok.kind == "bold":
            parts.append(f"<b>{_font_safe(tok.value)}</b>")
        elif tok.kind == "ans":
            parts.append(f'<font color="#B3261E"><b>{_font_safe(tok.value)}</b></font>')
        elif tok.kind == "br":
            parts.append("<br/>")
        elif tok.kind == "icon":
            path = icons.png(tok.value)
            if path is None:
                continue
            size = tok.size or icon_pt
            valign = "bottom" if size > 22 else "middle"   # big pictures sit on the baseline
            parts.append(f'<img src="{path}" width="{size:.1f}" height="{size:.1f}" valign="{valign}"/>')
    return "".join(parts)


def _styles() -> dict[str, ParagraphStyle]:
    _setup_fonts()
    base = dict(fontName="Andika", textColor=INK, fontSize=11.5, leading=17, spaceAfter=3)
    return {
        "body": ParagraphStyle("body", **base),
        "small": ParagraphStyle("small", **{**base, "fontSize": 9, "leading": 12.5}),
        "center": ParagraphStyle("center", alignment=TA_CENTER, **base),
        "right": ParagraphStyle("right", alignment=TA_RIGHT, **base),
        "instruction": ParagraphStyle("instruction", **{**base, "fontName": "Andika-Bold",
                                                        "fontSize": 12, "spaceBefore": 6, "spaceAfter": 4}),
        "note": ParagraphStyle("note", **{**base, "fontName": "Andika-Italic", "fontSize": 10, "leading": 14}),
        "h1": ParagraphStyle("h1", **{**base, "fontName": "Andika-Bold", "fontSize": 18, "leading": 23,
                                      "textColor": PRIMARY, "spaceBefore": 8, "spaceAfter": 6}),
        "h2": ParagraphStyle("h2", **{**base, "fontName": "Andika-Bold", "fontSize": 14, "leading": 19,
                                      "textColor": PRIMARY, "spaceBefore": 10, "spaceAfter": 4}),
        "h3": ParagraphStyle("h3", **{**base, "fontName": "Andika-Bold", "fontSize": 12, "leading": 16,
                                      "textColor": ACCENT, "spaceBefore": 8, "spaceAfter": 3}),
        "cell": ParagraphStyle("cell", **{**base, "fontSize": 10.5, "leading": 14.5, "spaceAfter": 0}),
        "cellc": ParagraphStyle("cellc", alignment=TA_CENTER, **{**base, "fontSize": 10.5, "leading": 14.5,
                                                                 "spaceAfter": 0}),
        "cellh": ParagraphStyle("cellh", **{**base, "fontName": "Andika-Bold", "fontSize": 10.5,
                                            "leading": 14.5, "spaceAfter": 0, "textColor": colors.white}),
        "bullet": ParagraphStyle("bullet", **{**base, "leftIndent": 14, "bulletIndent": 3, "spaceAfter": 2}),
    }


class _Numbered(BaseDocTemplate):
    pass


_TALL_ICON = re.compile(r"\[\[([^\]|]+)\|(\d+(?:\.\d+)?)\]\]")
TALL_PT = 22


def _rich(text: str, style: ParagraphStyle, avail: float, icon_pt: float | None = None):
    """A paragraph, or — when the line holds a tall inline picture — a one-row table [text | picture | text].

    ReportLab sizes a line for an inline picture but still draws the first baseline from ``leading``, so tall
    pictures spill into the line above. A table row keeps picture and words aligned without overlap."""
    tall = [m for m in _TALL_ICON.finditer(text)
            if float(m.group(2)) > TALL_PT and not text[max(0, m.start() - 1):m.start()] == "\n"
            and not text[m.end():m.end() + 1] == "\n"]
    if not tall:
        return Paragraph(rl_text(text, icon_pt) if icon_pt else rl_text(text), style)
    cells, widths, pos = [], [], 0
    for m in tall:
        before = text[pos:m.start()].strip()
        if before:
            cells.append(Paragraph(rl_text(before, icon_pt) if icon_pt else rl_text(before), style))
            widths.append(pdfmetrics.stringWidth(strip(before), "Andika-Bold" if "**" in before else "Andika",
                                                 style.fontSize) + 8)
        size = float(m.group(2))
        path = icons.png(m.group(1).strip())
        if path is not None:
            cells.append(RLImage(str(path), width=size, height=size))
            widths.append(size + 6)
        pos = m.end()
    after = text[pos:].strip()
    if after:
        cells.append(Paragraph(rl_text(after, icon_pt) if icon_pt else rl_text(after), style))
        widths.append(max(avail - sum(widths), 40))
    t = RLTable([cells], colWidths=widths)
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
    t.hAlign = "LEFT"
    return t


def _flow(blocks: list[Block], st: dict[str, ParagraphStyle], width: float) -> list:
    out: list = []
    for b in blocks:
        out.extend(_one(b, st, width))
    return out


def _one(b: Block, st: dict[str, ParagraphStyle], width: float) -> list:
    if isinstance(b, Heading):
        return [Paragraph(rl_text(b.text, 18), st[f"h{min(max(b.level, 1), 3)}"])]
    if isinstance(b, Para):
        flow = _rich(b.text, st.get(b.style, st["body"]), width)
        return [flow, RLSpacer(1, 3)] if isinstance(flow, RLTable) else [flow]
    if isinstance(b, Bullets):
        items = []
        for i, it in enumerate(b.items, 1):
            bullet = f"{i}." if b.ordered else "•"
            items.append(Paragraph(rl_text(it), st["bullet"], bulletText=bullet))
        return items
    if isinstance(b, Spacer):
        return [RLSpacer(1, b.h * mm)]
    if isinstance(b, PageBreak):
        return [RLPageBreak()]
    if isinstance(b, Rule):
        return [HRFlowable(width="100%", thickness=0.6, color=GRID, spaceBefore=3, spaceAfter=3)]
    if isinstance(b, Lines):
        rows = [[""] for _ in range(b.n)]
        t = RLTable(rows, colWidths=[width], rowHeights=[b.height * mm] * b.n)
        t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.6, GRID)]))
        return [t, RLSpacer(1, 2 * mm)]
    if isinstance(b, Group):
        return [KeepTogether(_flow(b.blocks, st, width))]
    if isinstance(b, Box):
        return _box(b, st, width)
    if isinstance(b, Table):
        return _table(b, st, width)
    raise TypeError(f"unknown block {type(b)!r}")


def _box(b: Box, st: dict[str, ParagraphStyle], width: float):
    fill, edge = BOX_COLORS.get(b.kind, BOX_COLORS["note"])
    inner: list = []
    if b.title:
        p = ParagraphStyle("bt", parent=st["body"], fontName="Andika-Bold", textColor=edge, spaceAfter=2)
        inner.append(Paragraph(rl_text(b.title), p))
    inner.extend(_flow(b.blocks, st, width - 10 * mm))
    if b.kind == "draw":
        inner.append(RLSpacer(1, 26 * mm))
    t = RLTable([[inner]], colWidths=[width])
    style = [
        ("BACKGROUND", (0, 0), (-1, -1), fill),
        ("BOX", (0, 0), (-1, -1), 1.0, edge),
        ("LEFTPADDING", (0, 0), (-1, -1), 5 * mm), ("RIGHTPADDING", (0, 0), (-1, -1), 5 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 3 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
    ]
    if b.kind == "draw":
        style.append(("BOX", (0, 0), (-1, -1), 1.0, GRID))
    t.setStyle(TableStyle(style))
    return [t, RLSpacer(1, 3 * mm)]


def _table(b: Table, st: dict[str, ParagraphStyle], width: float):
    ncols = max(len(r) for r in b.rows)
    fr = b.widths or [1 / ncols] * ncols
    total = sum(fr)
    if b.width_mm:
        width = min(width, b.width_mm * mm)
    widths = [width * f / total for f in fr]
    cell_style = st["cellc"] if b.align == "center" else st["cell"]
    if b.size:
        cell_style = ParagraphStyle("cs", parent=cell_style, fontSize=b.size, leading=b.size * 1.35)
    data = []
    for ri, row in enumerate(b.rows):
        cells = []
        for ci in range(ncols):
            text = row[ci] if ci < len(row) else ""
            if b.header and ri == 0:
                cells.append(Paragraph(rl_text(text), st["cellh"]))
            else:
                cells.append(_rich(text, cell_style, widths[ci] - 8, icon_pt=(b.size or 10.5) + 4))
        data.append(cells)
    t = RLTable(data, colWidths=widths, repeatRows=1 if b.header else 0,
                rowHeights=[b.row_height * mm] * len(data) if b.row_height else None)
    cmds: list = [("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                  ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                  ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
    if b.style == "grid":
        cmds += [("GRID", (0, 0), (-1, -1), 0.6, GRID)]
    elif b.style == "stage":
        cmds += [("GRID", (0, 0), (-1, -1), 0.5, GRID), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                 ("ROWBACKGROUNDS", (0, 1 if b.header else 0), (-1, -1), [colors.white, SOFT])]
    elif b.style == "cards":
        cmds += [("GRID", (0, 0), (-1, -1), 0.8, colors.HexColor("#7F8C9A"))]
        cmds[0] = ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
    if b.header:
        cmds += [("BACKGROUND", (0, 0), (-1, 0), PRIMARY)]
    if b.bg:
        for ri, row in enumerate(b.bg):
            for ci, col in enumerate(row):
                if col:
                    cmds.append(("BACKGROUND", (ci, ri), (ci, ri), colors.HexColor("#" + col.lstrip("#"))))
    t.setStyle(TableStyle(cmds))
    if b.width_mm:
        t.hAlign = "CENTER"
    return [t, RLSpacer(1, 2 * mm)]


def render_pdf(doc: Doc, path: str | Path) -> Path:
    _setup_fonts()
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    st = _styles()
    left, right, top, bottom = 16 * mm, 16 * mm, 30 * mm, 17 * mm
    if doc.name_line:
        top += 9 * mm
    width = A4[0] - left - right

    def on_page(canvas, d):  # header + footer
        canvas.saveState()
        w, h = A4
        canvas.setFillColor(PRIMARY)
        canvas.rect(0, h - 22 * mm, w, 22 * mm, stroke=0, fill=1)
        canvas.setFillColor(ACCENT)
        canvas.rect(0, h - 23.5 * mm, w, 1.5 * mm, stroke=0, fill=1)
        canvas.setFillColor(colors.white)
        badge_w = pdfmetrics.stringWidth(doc.badge, "Andika-Bold", 9.5) + 8 * mm if doc.badge else 0
        room = w - left - right - badge_w
        title_pt = 17.0
        while title_pt > 12 and pdfmetrics.stringWidth(doc.title, "Andika-Bold", title_pt) > room:
            title_pt -= 0.5            # long titles shrink instead of running into the badge
        canvas.setFont("Andika-Bold", title_pt)
        canvas.drawString(left, h - 12.5 * mm, doc.title)
        if doc.subtitle:
            canvas.setFont("Andika", 10)
            canvas.drawString(left, h - 18.3 * mm, doc.subtitle)
        if doc.badge:
            canvas.setFont("Andika-Bold", 9.5)
            canvas.drawRightString(w - right, h - 12.5 * mm, doc.badge)
        if doc.key:
            canvas.setFillColor(colors.white)
            canvas.roundRect(w - right - 38 * mm, h - 20.5 * mm, 38 * mm, 5.5 * mm, 2, stroke=0, fill=1)
            canvas.setFillColor(KEYRED)
            canvas.setFont("Andika-Bold", 9)
            canvas.drawCentredString(w - right - 19 * mm, h - 19.3 * mm, "TEACHER'S KEY")
        if doc.name_line:
            y = h - 31 * mm
            canvas.setFillColor(INK)
            canvas.setFont("Andika", 11)
            canvas.drawString(left, y, "Name:")
            canvas.drawString(left + 88 * mm, y, "Class:")
            canvas.drawString(left + 128 * mm, y, "Date:")
            canvas.setStrokeColor(GRID)
            canvas.setLineWidth(0.6)
            canvas.line(left + 14 * mm, y - 1, left + 84 * mm, y - 1)
            canvas.line(left + 101 * mm, y - 1, left + 124 * mm, y - 1)
            canvas.line(left + 141 * mm, y - 1, w - right, y - 1)
        canvas.setFillColor(colors.HexColor("#6B7785"))
        canvas.setFont("Andika", 7.5)
        foot = doc.footer or "3-sinf · original teaching material · emoji: Twemoji (CC-BY 4.0)"
        canvas.drawString(left, 9 * mm, foot)
        canvas.drawRightString(w - right, 9 * mm, f"{d.page}")
        canvas.restoreState()

    frame = Frame(left, bottom, width, A4[1] - top - bottom, leftPadding=0, rightPadding=0,
                  topPadding=0, bottomPadding=0, id="main")
    tmpl = PageTemplate(id="p", frames=[frame], onPage=on_page)
    pdf = BaseDocTemplate(str(path), pagesize=A4, pageTemplates=[tmpl], title=doc.title,
                          author="3-sinf", subject=doc.subtitle or doc.title)
    pdf.build(_flow(doc.blocks, st, width))
    return path
