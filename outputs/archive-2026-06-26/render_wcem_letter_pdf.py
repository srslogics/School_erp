from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


OUT = "/Users/shubhamsingh/Documents/New project/homepage/outputs/WCEM-Proposal-Letter.pdf"
W, H = letter
LEFT = 0.72 * inch
RIGHT = W - 0.72 * inch
WIDTH = RIGHT - LEFT

NAVY = (0.08, 0.16, 0.26)
INK = (0.11, 0.17, 0.22)
SLATE = (0.37, 0.42, 0.48)
LINE = (0.84, 0.88, 0.91)
GOLD = (0.63, 0.50, 0.22)
PAPER = (0.985, 0.982, 0.972)


def wrap_lines(text, font, size, max_width):
    words = text.split()
    lines = []
    cur = ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if stringWidth(trial, font, size) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_para(c, text, x, y, font="Times-Roman", size=11, leading=13.2, color=INK, gap=7):
    c.setFont(font, size)
    c.setFillColorRGB(*color)
    lines = wrap_lines(text, font, size, WIDTH)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y - gap


def main():
    c = canvas.Canvas(OUT, pagesize=letter)
    c.setFillColorRGB(*PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    top = H - 0.98 * inch
    c.setFillColorRGB(*NAVY)
    c.setFont("Times-Bold", 17.5)
    c.drawString(LEFT, top, "SrS Logics")
    c.setFillColorRGB(*SLATE)
    c.setFont("Times-Italic", 9.4)
    c.drawString(LEFT, top - 14, "Founder-led software engineering company")

    c.setFillColorRGB(*INK)
    c.setFont("Times-Roman", 9.2)
    c.drawRightString(RIGHT, top + 1, "srslogics.com")
    c.drawRightString(RIGHT, top - 12, "shubhamsingh@srslogics.com")
    c.drawRightString(RIGHT, top - 25, "+91 9270925106 | Nagpur, India")

    y = top - 30
    c.setStrokeColorRGB(*LINE)
    c.setLineWidth(0.9)
    c.line(LEFT, y, RIGHT, y)

    y -= 18
    c.setFillColorRGB(*GOLD)
    c.setFont("Times-Bold", 8.2)
    c.drawString(LEFT, y, "STRATEGIC PROPOSAL LETTER")
    c.setFillColorRGB(*SLATE)
    c.setFont("Times-Roman", 9.4)
    c.drawRightString(RIGHT, y, "21 June 2026")

    y -= 24
    c.setFillColorRGB(*NAVY)
    for line in wrap_lines("Strategic Proposal for Unified Digital Institution Transformation", "Times-Bold", 15.2, WIDTH):
        c.setFont("Times-Bold", 15.2)
        c.drawString(LEFT, y, line)
        y -= 18

    c.setFont("Times-Italic", 9.8)
    c.setFillColorRGB(*SLATE)
    c.drawString(LEFT, y, "For Wainganga College of Engineering and Management (WCEM), Nagpur.")

    y -= 22
    c.setStrokeColorRGB(*LINE)
    c.setLineWidth(0.85)
    c.line(LEFT, y, RIGHT, y)
    y -= 18
    c.setFont("Times-Roman", 10.6)
    c.setFillColorRGB(*INK)
    for line in [
        "To,",
        "The Director,",
        "Wainganga College of Engineering and Management (WCEM),",
        "Nagpur.",
    ]:
        c.drawString(LEFT, y, line)
        y -= 11.5

    y -= 3
    c.setFont("Times-Bold", 10.8)
    c.setFillColorRGB(*INK)
    c.drawString(LEFT, y, "Subject: Strategic Proposal for Unified Digital Institution Transformation")

    y -= 20
    paras = [
        ("Respected Sir,", "Times-Bold"),
        ("Following our upcoming meeting, I am formally submitting this proposal for the implementation of a comprehensive Digital Institution Transformation System at Wainganga College of Engineering and Management.", "Times-Roman"),
        ("Operating as an autonomous multi-program institution across B.Tech, M.Tech, Polytechnic, MBA, and MCA creates a complex demand across academic, examination, finance, and compliance workflows. Our analysis indicates that the core bottleneck is not a lack of software, but the operational friction created by disconnected data systems.", "Times-Roman"),
        ("Our proposal is the implementation of one unified digital operating system rather than fragmented portals. The platform integrates seven institutional layers: Admissions and Conversion, Academic Operations, Examination Control, Financial Integrity, Placement and Outcomes, Governance and NAAC Compliance, and an Executive Control Dashboard.", "Times-Roman"),
        ("Our commitment includes high-availability cloud deployment with college-controlled data sovereignty, a perpetual exclusive institutional license model, and a discovery process focused on mapping existing institutional workflows so the software fits staff reality rather than forcing teams to adapt to generic tools.", "Times-Roman"),
        ("Commercial & Operating Framework: The total investment for platform design, engineering, and deployment is Rs. 6,50,000/- (Six Lakhs, Fifty Thousand Rupees only), structured as 30 percent on kickoff, 40 percent on core module delivery, and 30 percent upon final stabilization. We also provide a Lifetime Proprietary Warranty on all code against the signed blueprint, ensuring long-term institutional stability at zero additional maintenance cost.", "Times-Roman"),
        ("Ongoing infrastructure costs are separate from our engineering fee and are paid directly by the college to service providers at actual usage rates. These include cloud infrastructure, DLT-approved SMS and WhatsApp Business API communication layers, and annual domain and security certification costs. For an institution of this scale, we estimate these external operating costs at approximately Rs. 18,500/- per month, with no markup from SrS Logics.", "Times-Roman"),
        ("Upon approval, we are prepared to initiate a structured Discovery and Blueprint Phase to finalize role hierarchies, approval workflows, and the implementation sequence required for a phased go-live aligned to the upcoming academic intake.", "Times-Roman"),
        ("I look forward to discussing how SrS Logics can help establish a stronger, more disciplined digital foundation for Wainganga College.", "Times-Roman"),
        ("Sincerely,", "Times-Roman"),
    ]

    for text, font in paras:
        y = draw_para(
            c,
            text,
            LEFT,
            y,
            font=font,
            size=10.4 if font == "Times-Roman" else 10.8,
            leading=12.4 if font == "Times-Roman" else 12.6,
            color=INK,
            gap=6,
        )

    c.setStrokeColorRGB(*LINE)
    c.setLineWidth(0.85)
    c.line(LEFT, y, LEFT + 2.4 * inch, y)
    y -= 16

    c.setFillColorRGB(*NAVY)
    c.setFont("Times-Bold", 11)
    c.drawString(LEFT, y, "Shubham Singh")
    y -= 13
    c.setFillColorRGB(*INK)
    c.setFont("Times-Roman", 9.8)
    c.drawString(LEFT, y, "Founder, SrS Logics")
    y -= 12
    c.setFillColorRGB(*SLATE)
    c.setFont("Times-Roman", 9.3)
    c.drawString(LEFT, y, "+91 9270925106")
    y -= 9
    c.drawString(LEFT, y, "shubhamsingh@srslogics.com")

    c.save()
    print(OUT)


if __name__ == "__main__":
    main()
