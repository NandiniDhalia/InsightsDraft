from reportlab.platypus import SimpleDocTemplate, Paragraph
from document.markdown_parser import markdown_to_pdf
from document.pdf_styles import get_theme
from document.cover_page import create_cover_page
from document.footer import add_footer

def generate_pdf(file_path,content,settings):
    title=settings["title"]
    document_type=settings["document_type"]
    author=settings["author_name"]
    inst_comp=settings["inst_comp_name"]
    date=settings["date_value"]
    footer=settings["footer_text"]
    cover_page=settings["cover_page"]
    toc=settings["toc"]
    page=settings["page"]
    theme=settings["theme"]
    styles = get_theme(theme)
    doc=SimpleDocTemplate(file_path)
    story=[]
    if cover_page:
        create_cover_page(story, settings, styles)
    story.extend(markdown_to_pdf(content, styles))
    doc.build(story, onFirstPage=lambda canvas, doc: add_footer(canvas, doc, settings), onLaterPages=lambda canvas, doc: add_footer(canvas, doc, settings))