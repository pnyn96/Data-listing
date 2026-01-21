from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(df):
    path = "/tmp/report.pdf"
    c = canvas.Canvas(path, pagesize=A4)

    y = 800
    for row in df.itertuples(index=False):
        c.drawString(40, y, str(row))
        y -= 20

    c.save()
    return path
