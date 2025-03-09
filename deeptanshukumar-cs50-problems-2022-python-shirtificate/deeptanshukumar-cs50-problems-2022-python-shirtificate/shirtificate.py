from fpdf import FPDF
from PIL import Image

def main():
    make_shirtificate(input("Name: "))


def make_shirtificate(name):
    pdf = FPDF()
    pdf.add_page()

    img = Image.open("shirtificate.png")
    img = img.resize((540,540))
    temp_path = "temp_image.png"
    img.save(temp_path)

    pdf.image(temp_path, x=10, y=70)
    pdf.set_font("arial", style="", size=50)
    pdf.cell(195, 50, "CS50 Shirtificate", align='C')
    pdf.set_font("arial", style="", size=25)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(-200, 250, f"{name} took CS50", align='C')
    pdf.output("shirtificate.pdf")

main()

