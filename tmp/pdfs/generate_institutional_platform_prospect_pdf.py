from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import ListFlowable, ListItem, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path("/Users/shubhamsingh/Documents/New project/homepage")
OUT_DIR = ROOT / "output" / "pdf"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_PATH = OUT_DIR / "institutional-platform-prospect.pdf"


def get_styles():
    base = getSampleStyleSheet()
    return {
        "cover_kicker": ParagraphStyle("cover_kicker", parent=base["BodyText"], fontName="Helvetica-Bold", fontSize=9.5, leading=11, alignment=TA_LEFT, textColor=colors.HexColor("#8ed8ff"), spaceAfter=14),
        "cover_title": ParagraphStyle("cover_title", parent=base["Title"], fontName="Helvetica-Bold", fontSize=27, leading=31.5, alignment=TA_LEFT, textColor=colors.white, spaceAfter=16),
        "cover_sub": ParagraphStyle("cover_sub", parent=base["BodyText"], fontName="Helvetica", fontSize=11.4, leading=17.4, alignment=TA_LEFT, textColor=colors.HexColor("#dbe8f8"), spaceAfter=20),
        "cover_meta": ParagraphStyle("cover_meta", parent=base["BodyText"], fontName="Helvetica", fontSize=8.6, leading=12.2, alignment=TA_LEFT, textColor=colors.HexColor("#b9d6f2"), spaceAfter=0),
        "cover_panel_label": ParagraphStyle("cover_panel_label", parent=base["BodyText"], fontName="Helvetica-Bold", fontSize=8.5, leading=10.5, alignment=TA_LEFT, textColor=colors.HexColor("#8ed8ff"), spaceAfter=5),
        "cover_panel_body": ParagraphStyle("cover_panel_body", parent=base["BodyText"], fontName="Helvetica", fontSize=9.6, leading=14, alignment=TA_LEFT, textColor=colors.white, spaceAfter=0),
        "cover_note": ParagraphStyle("cover_note", parent=base["BodyText"], fontName="Helvetica", fontSize=8.2, leading=10.8, alignment=TA_LEFT, textColor=colors.HexColor("#7387a6"), spaceAfter=0),
        "section_kicker": ParagraphStyle("section_kicker", parent=base["BodyText"], fontName="Helvetica-Bold", fontSize=8.4, leading=10, textColor=colors.HexColor("#4f7fbe"), spaceAfter=6),
        "h1": ParagraphStyle("h1", parent=base["Heading1"], fontName="Helvetica-Bold", fontSize=15.6, leading=18.6, textColor=colors.HexColor("#162a45"), spaceAfter=10),
        "h2": ParagraphStyle("h2", parent=base["Heading2"], fontName="Helvetica-Bold", fontSize=11.6, leading=14.2, textColor=colors.HexColor("#162a45"), spaceBefore=10, spaceAfter=6),
        "body": ParagraphStyle("body", parent=base["BodyText"], fontName="Helvetica", fontSize=9.4, leading=13.8, alignment=TA_JUSTIFY, textColor=colors.HexColor("#24364d"), spaceAfter=8),
        "body_left": ParagraphStyle("body_left", parent=base["BodyText"], fontName="Helvetica", fontSize=9.4, leading=13.8, alignment=TA_LEFT, textColor=colors.HexColor("#24364d"), spaceAfter=6),
        "callout_title": ParagraphStyle("callout_title", parent=base["Heading3"], fontName="Helvetica-Bold", fontSize=10.4, leading=12.6, textColor=colors.HexColor("#10223c"), spaceAfter=5),
        "small": ParagraphStyle("small", parent=base["BodyText"], fontName="Helvetica", fontSize=8.6, leading=12, textColor=colors.HexColor("#6a7b95"), spaceAfter=4),
        "signature": ParagraphStyle("signature", parent=base["BodyText"], fontName="Helvetica", fontSize=8.8, leading=12.2, textColor=colors.HexColor("#30435b"), alignment=TA_LEFT, spaceAfter=0),
        "metric_value": ParagraphStyle("metric_value", parent=base["Heading1"], fontName="Helvetica-Bold", fontSize=16, leading=18, textColor=colors.HexColor("#ffffff"), alignment=TA_LEFT, spaceAfter=4),
        "metric_label": ParagraphStyle("metric_label", parent=base["BodyText"], fontName="Helvetica", fontSize=8.6, leading=11, textColor=colors.HexColor("#dce8f7"), alignment=TA_LEFT),
    }


def header_box():
    data = [[
        Paragraph("SrS Logics", ParagraphStyle("brand", fontName="Helvetica-Bold", fontSize=18, leading=20, textColor=colors.white, alignment=TA_LEFT, spaceAfter=3)),
        Paragraph("Institutional Software and Internal Systems", ParagraphStyle("tag", fontName="Helvetica", fontSize=9.2, leading=11, textColor=colors.HexColor("#d8e4f4"), alignment=TA_RIGHT)),
    ]]
    t = Table(data, colWidths=[95 * mm, 75 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#12263f")),
        ("LINEABOVE", (0, 0), (-1, 0), 1.4, colors.HexColor("#8ed8ff")),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return t


def bullets(items, style):
    return ListFlowable([ListItem(Paragraph(item, style), leftIndent=0) for item in items], bulletType="bullet", start="-", leftIndent=14, bulletFontName="Helvetica", bulletFontSize=9, bulletColor=colors.HexColor("#2d5b93"))


def callout(title, text, styles):
    t = Table([[Paragraph(title, styles["callout_title"])], [Paragraph(text, styles["body_left"])]], colWidths=[168 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f4f7fb")),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#d5e0ec")),
        ("LINEBEFORE", (0, 0), (0, -1), 3, colors.HexColor("#2d5b93")),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def outcome_card(title, text):
    title_style = ParagraphStyle("outcome_card_title", fontName="Helvetica-Bold", fontSize=9.8, leading=11.8, textColor=colors.HexColor("#142842"), alignment=TA_LEFT, spaceAfter=5)
    body_style = ParagraphStyle("outcome_card_body", fontName="Helvetica", fontSize=8.6, leading=11.4, textColor=colors.HexColor("#30435b"), alignment=TA_LEFT)
    t = Table([[Paragraph(title, title_style)], [Paragraph(text, body_style)]], colWidths=[81 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#d2dfec")),
        ("LINEABOVE", (0, 0), (-1, 0), 1.5, colors.HexColor("#8ed8ff")),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    return t


def add_page_frame(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#f4f8fc"))
    canvas.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)
    canvas.setFillColor(colors.HexColor("#eef4fb"))
    canvas.rect(0, A4[1] - 18 * mm, A4[0], 18 * mm, stroke=0, fill=1)
    canvas.setStrokeColor(colors.HexColor("#d6e2f0"))
    canvas.setLineWidth(0.6)
    canvas.rect(14 * mm, 12 * mm, A4[0] - 28 * mm, A4[1] - 24 * mm)
    canvas.setFont("Helvetica", 8.5)
    canvas.setFillColor(colors.HexColor("#72839a"))
    canvas.drawCentredString(A4[0] / 2, 8 * mm, f"Institutional Software Concept Note | Page {doc.page}")
    canvas.restoreState()


def build_pdf():
    s = get_styles()
    doc = SimpleDocTemplate(str(OUT_PATH), pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm, topMargin=18 * mm, bottomMargin=18 * mm)
    story = []

    cover_intro = [
        Paragraph("INSTITUTIONAL SOFTWARE CONCEPT NOTE", s["cover_kicker"]),
        Paragraph("Integrated Institutional Management Platform", s["cover_title"]),
        Paragraph("For colleges, universities, autonomous institutes, and education groups that need stronger administrative control, cleaner internal workflows, and more reliable reporting visibility.", s["cover_sub"]),
    ]
    cover_action = Paragraph(
        "<b>RECOMMENDED STARTING POINT</b><br/><br/>Institutional software audit, system blueprint, and phased implementation planning.",
        s["cover_panel_body"],
    )
    cover_meta_box = Paragraph(
        "<b>PREPARED BY</b><br/><br/>SrS Logics<br/>Founder: Shubham Singh<br/>Nagpur, Maharashtra",
        s["cover_meta"],
    )
    cover = Table(
        [
            [cover_intro[0], ""],
            [cover_intro[1], ""],
            [cover_intro[2], ""],
            [cover_action, cover_meta_box],
        ],
        colWidths=[76 * mm, 56 * mm],
    )
    cover.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#12263f")),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#203c61")),
        ("SPAN", (0, 0), (-1, 0)),
        ("SPAN", (0, 1), (-1, 1)),
        ("SPAN", (0, 2), (-1, 2)),
        ("LINEABOVE", (0, 0), (-1, 0), 2, colors.HexColor("#8ed8ff")),
        ("LINEBELOW", (0, 2), (-1, 2), 1, colors.HexColor("#284a73")),
        ("BACKGROUND", (0, 3), (-1, 3), colors.HexColor("#173252")),
        ("BOX", (0, 3), (-1, 3), 0.8, colors.HexColor("#2a4c73")),
        ("LINEBEFORE", (1, 3), (1, 3), 0.8, colors.HexColor("#2a4c73")),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("TOPPADDING", (0, 0), (-1, -1), 28),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 22),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(Spacer(1, 44 * mm))
    story.append(cover)
    story.append(Spacer(1, 14 * mm))
    story.append(Paragraph("Confidential concept submission intended for institutional review.", s["cover_note"]))
    story.append(PageBreak())

    story.append(header_box())
    story.append(Spacer(1, 8))
    story.append(Paragraph("Director Lens", s["section_kicker"]))
    story.append(Paragraph("What Leadership Is Actually Deciding", s["h1"]))
    story.append(Paragraph("Before approving a serious software initiative, leadership usually wants clear answers to a few practical questions: what problem is being solved, why it matters now, what the institution will receive in the first stage, how much disruption it creates, and why the team proposing it should be trusted.", s["body_left"]))
    story.append(Spacer(1, 6))
    story.append(callout("Core Idea", "This proposal is not asking the institution to approve a full ERP blindly. It is proposing a structured first step that produces something management can actually review before any larger commitment.", s))
    story.append(Spacer(1, 8))
    story.append(Paragraph("What the Institution Is Actually Evaluating", s["h2"]))
    buying_table = Table([
        [outcome_card("Operational clarity", "A clearer internal system across admissions, records, approvals, and institutional workflow."), outcome_card("Lower fragmentation", "Fewer disconnected tools, fewer parallel records, and less manual chasing.")],
        [outcome_card("Leadership visibility", "Cleaner reporting for review meetings, monitoring, and day-to-day institutional decisions."), outcome_card("Reviewable first step", "Whether the work begins with outputs management can assess before committing to a larger build.")],
        [outcome_card("Scalable foundation", "A system that can support future modules and growth without rebuilding from scratch."), outcome_card("Continuity", "Stronger continuity beyond individual people, isolated files, or ad hoc processes.")],
    ], colWidths=[82 * mm, 82 * mm])
    buying_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story.append(buying_table)
    story.append(PageBreak())

    story.append(header_box())
    story.append(Spacer(1, 8))
    story.append(Paragraph("Institutional Context", s["section_kicker"]))
    story.append(Paragraph("When Institutions Reach This Stage", s["h1"]))
    story.append(Paragraph("Most established institutions already have some software, portals, spreadsheets, admission tools, exam workflows, finance records, or departmental systems. The deeper issue is usually not digital absence. It is operational fragmentation.", s["body"]))
    story.append(Paragraph("Typical institutional pain points include disconnected records, person-dependent approvals, repeated manual compilation for management review, weak visibility across placements and compliance, and scattered documentation across departments.", s["body"]))
    story.append(callout("What Changes", "Once these issues begin affecting speed, control, and reporting quality, the software requirement becomes an institutional one rather than a departmental one.", s))
    story.append(Spacer(1, 8))
    story.append(Paragraph("What the First Stage Should Produce", s["h2"]))
    readiness_table = Table([
        [outcome_card("Process observations", "A grounded view of how selected functions currently operate and where coordination weakens."), outcome_card("Workflow maps", "Mapped approvals, movement of records, and key decision points across departments.")],
        [outcome_card("Gap diagnosis", "Clear identification of operational overlaps, bottlenecks, and reporting blind spots."), outcome_card("Module sequence", "A practical order for what should be built first instead of a vague everything-at-once scope.")],
        [outcome_card("Dashboard needs", "Leadership reporting expectations defined before system design moves ahead."), outcome_card("Phased roadmap", "A reviewable basis for deciding whether and how a larger implementation should proceed.")],
    ], colWidths=[82 * mm, 82 * mm])
    readiness_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story.append(readiness_table)
    story.append(PageBreak())

    story.append(header_box())
    story.append(Spacer(1, 8))
    story.append(Paragraph("Platform Vision", s["section_kicker"]))
    story.append(Paragraph("What the Integrated Platform Can Cover", s["h1"]))
    story.append(Paragraph("The proposed platform may be planned as a modular but connected institutional environment rather than as a rigid one-size-fits-all ERP. The objective is one coherent internal system that aligns people, records, approvals, and reporting.", s["body"]))
    module_table = Table([
        ["Admissions and Enquiry", "lead capture, applicant movement, document status, communication workflow"],
        ["Student Records", "student master data, program mapping, progression visibility, document governance"],
        ["Examination Workflow", "exam coordination support, result structure, exception and verification handling"],
        ["Department Administration", "internal approvals, faculty-role structure, departmental visibility"],
        ["Placement Operations", "recruiter tracking, student readiness, internships, offers, outcomes"],
        ["Compliance and Committees", "evidence repository, committee records, annual updates, publishing workflow"],
        ["Leadership Dashboards", "admissions, academics, placements, compliance, pending-action reporting"],
    ], colWidths=[48 * mm, 120 * mm])
    module_table.setStyle(TableStyle([
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.HexColor("#f9fbfd"), colors.white]),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#d6e0eb")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#d6e0eb")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.4),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#23354c")),
        ("LEADING", (0, 0), (-1, -1), 10.9),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(module_table)
    story.append(Spacer(1, 8))
    story.append(callout("What This Means", "The platform is meant to support how the institution works internally, not just to add separate digital tools.", s))

    story.append(header_box())
    story.append(Spacer(1, 8))
    story.append(Paragraph("Delivery Approach", s["section_kicker"]))
    story.append(Paragraph("What Happens First", s["h1"]))
    story.append(Paragraph("The recommended first stage is an institutional software audit and system blueprint. That allows the institution to review current workflows, define the right scope, and move into execution in a controlled way.", s["body"]))
    phase_table = Table([
        ["Phase 1", "institutional software audit and system blueprint"],
        ["Phase 2", "core platform foundation: data structure, roles, approvals, dashboard base"],
        ["Phase 3", "functional rollout across admissions, records, exams, placements, and compliance"],
        ["Phase 4", "training, controlled go-live, stabilization, and refinement"],
    ], colWidths=[26 * mm, 142 * mm])
    phase_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#173252")),
        ("TEXTCOLOR", (0, 0), (0, -1), colors.white),
        ("BACKGROUND", (1, 0), (1, -1), colors.HexColor("#f6f9fc")),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#d6e0eb")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#d6e0eb")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.9),
        ("TEXTCOLOR", (1, 0), (1, -1), colors.HexColor("#23354c")),
        ("LEADING", (0, 0), (-1, -1), 11.5),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(phase_table)
    story.append(PageBreak())

    story.append(header_box())
    story.append(Spacer(1, 8))
    story.append(Paragraph("Trust and Outcomes", s["section_kicker"]))
    story.append(Paragraph("What Leadership Should Expect from the Team", s["h1"]))
    gains_table = Table([
        [outcome_card("Operational understanding", "The team should understand how work actually moves before proposing software structure."), outcome_card("Scope discipline", "The institution should not be pushed into a vague or inflated full-ERP commitment on day one.")],
        [outcome_card("Phased control", "Leadership should be able to review the work in steps rather than approve a disruptive replacement blindly."), outcome_card("Reporting logic", "Dashboard and review needs should be clarified before implementation direction is locked.")],
        [outcome_card("Real institutional fit", "The structure should reflect the institution's actual processes, not a generic demo flow."), outcome_card("Long-term value", "If executed properly, the institution gains cleaner coordination, stronger reporting, and better continuity.")],
    ], colWidths=[82 * mm, 82 * mm])
    gains_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story.append(gains_table)
    story.append(Spacer(1, 6))
    story.append(callout("Recommended Entry Point", "Institutional software audit, system blueprint, and phased implementation planning.", s))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Prepared by<br/><b>Shubham Singh</b><br/>Founder, SrS Logics<br/>shubhamsingh@srslogics.com | +91 9270925106 | srslogics.com", s["signature"]))

    doc.build(story, onFirstPage=add_page_frame, onLaterPages=add_page_frame)


if __name__ == "__main__":
    build_pdf()
    print(OUT_PATH)
