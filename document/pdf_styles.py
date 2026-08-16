from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor

PRIMARY_BLUE   = "#1F4E79"   # Deep Blue
ACCENT_BLUE    = "#4F81BD"   # Soft Blue
TEXT_DARK      = "#222222"   # Primary Text
TEXT_LIGHT     = "#666666"   # Secondary Text
BACKGROUND     = "#F8F9FA"   # Very Light Grey
DIVIDER        = "#D9E2EC"   # Light Divider
SUCCESS_GREEN  = "#2E8B57"   # Green
MODERN_CYAN    = "#17A2B8"   # Cyan
CREATIVE_ORANGE= "#F57C00"   # Orange
CORPORATE_NAVY = "#0B2545"   # Navy

def get_theme(theme):
    styles=getSampleStyleSheet()

    if theme == "Professional":
        title_style= ParagraphStyle("Title", fontName="Helvetica-Bold", fontSize=24, leading=28, alignment=TA_CENTER, textColor=PRIMARY_BLUE)
        heading_style= ParagraphStyle("Heading2", fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=ACCENT_BLUE)
        body_style= ParagraphStyle("BodyText", fontName="Helvetica", fontSize=12, leading=16, textColor=TEXT_DARK)
        return {"title": title_style, "heading": heading_style, "body": body_style}
    
    elif theme == "Creative":
        title_style= ParagraphStyle("Title", fontName="Helvetica-BoldOblique", fontSize=26, leading=30, alignment=TA_CENTER, textColor=CREATIVE_ORANGE)
        heading_style= ParagraphStyle("Heading2", fontName="Helvetica-BoldOblique", fontSize=20, leading=24, textColor=HexColor("#FF9800"))
        body_style= ParagraphStyle("BodyText", fontName="Helvetica-Oblique", fontSize=14, leading=18, textColor=HexColor("#333333"))
        return {"title": title_style, "heading": heading_style, "body": body_style}
    
    elif theme == "Minimalist":
        title_style= ParagraphStyle("Title", fontName="Helvetica-Bold", fontSize=22, leading=26, alignment=TA_CENTER, textColor=HexColor("#333333"))
        heading_style= ParagraphStyle("Heading2", fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=HexColor("#555555"))
        body_style= ParagraphStyle("BodyText", fontName="Helvetica", fontSize=12, leading=16, textColor=TEXT_DARK)
        return {"title": title_style, "heading": heading_style, "body": body_style}
    
    elif theme == "Academic":
        title_style= ParagraphStyle("Title", fontName="Helvetica-Bold", fontSize=24, leading=28, alignment=TA_CENTER, textColor=HexColor("#000080"))
        heading_style= ParagraphStyle("Heading2", fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=PRIMARY_BLUE)
        body_style= ParagraphStyle("BodyText", fontName="Helvetica", fontSize=12, leading=16, textColor=HexColor("#000000"))
        return {"title": title_style, "heading": heading_style, "body": body_style}
    
    elif theme == "Modern":
        title_style= ParagraphStyle("Title", fontName="Helvetica-Bold", fontSize=28, leading=32, alignment=TA_CENTER, textColor=MODERN_CYAN)
        heading_style= ParagraphStyle("Heading2", fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=HexColor("#20C997"))
        body_style= ParagraphStyle("BodyText", fontName="Helvetica", fontSize=14, leading=18, textColor=TEXT_DARK)
        return {
            "title": title_style,
            "heading": heading_style,
            "body": body_style
        }
    
    elif theme == "Corporate":
        title_style= ParagraphStyle("Title", fontName="Helvetica-Bold", fontSize=26, leading=30, alignment=TA_CENTER, textColor=CORPORATE_NAVY)
        heading_style= ParagraphStyle("Heading2", fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=PRIMARY_BLUE)
        body_style= ParagraphStyle("BodyText", fontName="Helvetica", fontSize=12, leading=16, textColor=TEXT_DARK)
        return {
            "title": title_style,
            "heading": heading_style,
            "body": body_style
        }
    