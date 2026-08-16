from reportlab.lib.units import inch

def add_footer(canvas, doc, settings):
    canvas.saveState()
    footer = settings["footer_text"]
    page= settings["page"]
    if footer:
        canvas.drawString(40,30,footer)
    if page:
        canvas.drawRightString(550,30,f"Page {canvas.getPageNumber()}")
    canvas.restoreState()