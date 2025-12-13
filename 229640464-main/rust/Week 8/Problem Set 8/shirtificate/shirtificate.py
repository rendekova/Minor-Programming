from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        # Setting and defining the front of the header
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 20, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

def main():
    name = input("Name: ")
    # The orientation of the PDF should be Portrait.
    # The format of the PDF should be A4, which is 210mm wide by 297mm tall.
    pdf = Shirtificate(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()
    # The shirt’s image should be centered horizontally.
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(255, 255, 255)
    pdf.image("shirtificate.png", x=30, y=70, w=150)

    # The user’s name should be on top of the shirt, in white text.
    text= f"{name} took CS50"
    text_width = pdf.get_string_width(text)
    page_width = 210
    pdf.text(x=(page_width - text_width)/2, y=130, txt=text)

    pdf.output("shirtificate.pdf")





if __name__ == "__main__":
     main()

