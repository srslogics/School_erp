from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path("/Users/shubhamsingh/Documents/New project/homepage")
OUT_DIR = ROOT / "output" / "pdf"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_PATH = OUT_DIR / "wcem-one-page-letter.pdf"


def build_styles():
    styles = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "title",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=18,
            textColor=colors.HexColor("#0f1c2f"),
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.2,
            leading=11,
            textColor=colors.HexColor("#3d516e"),
            alignment=TA_CENTER,
            spaceAfter=12,
        ),
        "label": ParagraphStyle(
            "label",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.2,
            leading=11,
            textColor=colors.HexColor("#0f1c2f"),
            spaceAfter=2,
        ),
        "body": ParagraphStyle(
            "body",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.35,
            leading=13.1,
            alignment=TA_JUSTIFY,
            textColor=colors.HexColor("#223248"),
            spaceAfter=5,
        ),
        "body_left": ParagraphStyle(
            "body_left",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.35,
            leading=13.1,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#223248"),
            spaceAfter=3,
        ),
        "section": ParagraphStyle(
            "section",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=10.2,
            leading=12,
            textColor=colors.HexColor("#0f1c2f"),
            spaceBefore=4,
            spaceAfter=4,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.15,
            leading=12.1,
            leftIndent=10,
            firstLineIndent=0,
            bulletIndent=0,
            textColor=colors.HexColor("#223248"),
            spaceAfter=1,
        ),
        "signoff": ParagraphStyle(
            "signoff",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=12,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#223248"),
            spaceAfter=1,
        ),
    }


def hr(width_mm=165):
    line = "_" * 160
    return Paragraph(
        f'<font color="#d5dfec">{line[: int(width_mm)]}</font>',
        ParagraphStyle(
            "hr",
            fontName="Helvetica",
            fontSize=4,
            leading=4,
            alignment=TA_CENTER,
        ),
    )


def add_page_frame(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#f7fafe"))
    canvas.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)
    canvas.setStrokeColor(colors.HexColor("#d6e2f0"))
    canvas.setLineWidth(0.8)
    canvas.rect(14 * mm, 12 * mm, A4[0] - 28 * mm, A4[1] - 24 * mm)
    canvas.restoreState()


def build_pdf():
    styles = build_styles()
    doc = SimpleDocTemplate(
        str(OUT_PATH),
        pagesize=A4,
        leftMargin=17 * mm,
        rightMargin=17 * mm,
        topMargin=11 * mm,
        bottomMargin=11 * mm,
    )

    story = []

    story.append(Paragraph("To", styles["label"]))
    story.append(
        Paragraph(
            "The Director / Management<br/>"
            "Wainganga College of Engineering and Management (WCEM)<br/>"
            "Near Gumgaon Railway Station, Dongargaon, Wardha Road,<br/>"
            "Nagpur, Maharashtra 441108",
            styles["body_left"],
        )
    )
    story.append(Spacer(1, 2))
    story.append(
        Paragraph(
            "<b>Subject:</b> Submission for Institutional Software Audit and System Blueprint",
            styles["body_left"],
        )
    )
    story.append(Spacer(1, 3))

    body_paragraphs = [
        "Respected Sir/Madam,",
        "Please find enclosed a concept note from SrS Logics for a phased institutional software initiative for Wainganga College of Engineering and Management.",
        "For an institution operating across admissions, academics, examinations, placements, compliance, and internal administration, the long-term challenge is usually not the absence of software. It is the lack of one dependable internal structure across records, approvals, reporting, and department-level coordination.",
        "In view of this, SrS Logics proposes a <b>Unified Institutional Management Platform</b> for WCEM, aligned to the college's actual operating model rather than to a generic ERP template.",
    ]
    for text in body_paragraphs:
        story.append(Paragraph(text, styles["body"]))

    story.append(Paragraph("The platform can be planned to support admissions, student records, examination workflows, departmental administration, placement operations, compliance processes, and management reporting.", styles["body"]))

    story.append(Paragraph("Recommended First Stage", styles["section"]))
    story.append(
        Paragraph(
            "<b>Institutional Software Audit and System Blueprint</b>",
            styles["body_left"],
        )
    )

    audit_items = [
        "process and system review across selected functions",
        "workflow and approval mapping",
        "identification of operational gaps, overlaps, and reporting issues",
        "recommendation of priority modules",
        "dashboard and visibility requirements",
        "phase-wise implementation roadmap",
    ]
    for item in audit_items:
        story.append(Paragraph(item, styles["bullet"], bulletText="-"))

    closing_paragraphs = [
        "This gives management a clear basis to decide whether, how, and in what order a larger software build should move forward.",
        "SrS Logics builds internal systems around real operational requirements, with emphasis on administrative control, workflow clarity, reporting discipline, and phased execution.",
        "We would value an opportunity to present the concept note and discuss whether WCEM may consider an initial audit and blueprint exercise.",
    ]
    story.append(Spacer(1, 2))
    for text in closing_paragraphs:
        story.append(Paragraph(text, styles["body"]))

    story.append(Spacer(1, 5))
    signoff = [
        "Regards,",
        "<b>Shubham Singh</b> | Founder, <b>SrS Logics</b>",
        "shubhamsingh@srslogics.com | +91 9270925106 | https://srslogics.com/",
    ]
    for line in signoff:
        story.append(Paragraph(line, styles["signoff"]))

    doc.build(story, onFirstPage=add_page_frame)


if __name__ == "__main__":
    build_pdf()
    print(OUT_PATH)
