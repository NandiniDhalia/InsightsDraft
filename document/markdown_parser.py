import re
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def markdown_to_pdf(markdown_txt, styles):
    story=[]
    lines=markdown_txt.split('\n')
    for line in lines:
        line=line.strip()
        if not line:
            story.append(Spacer(1, 12))
            continue
        if line.startswith('###'):
            story.append(Paragraph(line[4:],styles["heading"]))
        elif line.startswith('##'):
            story.append(Paragraph(line[3:],styles["heading"]))
        elif line.startswith('#'):
            story.append(Paragraph(line[2:],styles["title"]))
        elif line.startswith('- '):
            story.append(Paragraph(f"&bull; {line[2:]}",styles["body"]))
        elif re.match(r'^\d+\.', line):
            story.append(Paragraph(line,styles["body"]))
        else:
            line=re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            line=re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)
            story.append(Paragraph(line,styles["body"]))
    return story
