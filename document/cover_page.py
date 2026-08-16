from reportlab.platypus import Paragraph, Spacer, PageBreak, HRFlowable

def create_cover_page(story,settings,styles):
    title = settings["title"]
    document_type = settings["document_type"]
    author = (settings["author_name"]).title()
    institution = settings["inst_comp_name"]
    date = settings["date_value"]
    story.append(Spacer(1, 100))
    story.append(Paragraph(document_type, styles["title"]))
    story.append(Paragraph(title, styles["title"]))
    
    story.append(Spacer(1, 50))
    if author:
        story.append(Paragraph(f"Prepared by:\n{author}", styles["body"]))
    story.append(Spacer(1, 20))
    if institution:
        story.append(Paragraph(f"Institution:\n{institution}", styles["body"]))
    story.append(Spacer(1, 20))
    if date:
        story.append(Paragraph(f"Date:\n{date}", styles["body"]))
    story.append(PageBreak())