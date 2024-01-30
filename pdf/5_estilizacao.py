from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Calculating width of title and setting cursor position:
        width = self.get_string_width(self.title) + 0.6
        self.set_x(((21 - width) / 0.2) / 10)
        # Setting colors for frame, background and text:
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Setting thickness of the frame (1 cm)
        self.set_line_width(0.1)
        # Printing title:
        self.cell(
            w=width,
            h=0.9,
            txt=self.title,
            border=True,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            fill=True,
        )
        # Performing a line break:
        self.ln(1)

    def footer(self):
        # Setting position at 1.5 cm from bottom:
        self.set_y(-1.5)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Setting text color to gray:
        self.set_text_color(128)
        # Printing page number
        self.cell(0, 1, f"Page {self.page_no()}", align="C")

    def chapter_title(self, num, label):
        # Setting font: helvetica 12
        self.set_font("helvetica", "", 12)
        # Setting background color
        self.set_fill_color(200, 220, 255)
        # Printing chapter name:
        self.cell(
            w=0,
            h=0.6,
            txt=f"Capítulo {num} : {label}",
            new_x="LMARGIN",
            new_y="NEXT",
            align="L",
            fill=True,
        )
        # Performing a line break:
        self.ln(0.4)

    def chapter_body(self, filepath):
        # Reading text file:
        with open(filepath, "rb") as fh:
            txt = fh.read().decode("latin-1")
        # Setting font: Times 12
        self.set_font("Times", size=12)
        # Printing justified text:
        self.multi_cell(w=0, h=0.5, txt=txt)
        # Performing a line break:
        self.ln()
        # Final mention in italics:
        self.set_font(style="I")
        self.cell(0, 0.5, "(fim do capítulo)")

    def print_chapter(self, num, title, filepath):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(filepath)


pdf = PDF(unit='cm')
pdf.set_title("20000 Leagues Under the Seas")
pdf.set_author("Jules Verne")
pdf.print_chapter(1, "A RUNAWAY REEF", "capítulo1.txt")
pdf.print_chapter(2, "THE PROS AND CONS", "capítulo2.txt")
pdf.output("tuto3.pdf")