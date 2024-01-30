from fpdf import FPDF


class PDF(FPDF):
    def __init__(self):
        super().__init__(unit='cm')
        self.col = 0  # Current column
        self.y0 = 0  # Ordinate of column start

    def header(self):
        self.set_font("helvetica", "B", 15)
        width = self.get_string_width(self.title) + 0.6
        self.set_x(((21 - width) / 0.2)/10)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.set_line_width(0.1)
        # Printing title:
        self.cell(
            width,
            0.9,
            self.title,
            border=1,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            fill=True,
        )
        self.ln(1)
        # Saving ordinate position:
        self.y0 = self.get_y()

    def footer(self):
        self.set_y(-1.5)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(128)
        self.cell(0, 1, f"Page {self.page_no()}", align="C")

    def set_col(self, col):
        # Set column position:
        self.col = col
        x = 1 + col * 6.5
        self.set_left_margin(x)
        self.set_x(x)

    @property
    def accept_page_break(self):
        if self.col < 2:
            # Go to next column:
            self.set_col(self.col + 1)
            # Set ordinate to top:
            self.set_y(self.y0)
            # Stay on the same page:
            return False
        # Go back to first column:
        self.set_col(0)
        # Trigger a page break:
        return True

    def chapter_title(self, num, label):
        self.set_font("helvetica", "", 12)
        self.set_fill_color(200, 220, 255)
        self.cell(
            0,
            0.6,
            f"Chapter {num} : {label}",
            new_x="LMARGIN",
            new_y="NEXT",
            border="L",
            fill=True,
        )
        self.ln(0.4)
        # Saving ordinate position:
        self.y0 = self.get_y()

    def chapter_body(self, name):
        # Reading text file:
        with open(name, "rb") as fh:
            txt = fh.read().decode("latin-1")
        # Setting font: Times 12
        self.set_font("Times", size=12)
        # Printing text in a 6cm width column:
        self.multi_cell(6, 0.5, txt)
        self.ln()
        # Final mention in italics:
        self.set_font(style="I")
        self.cell(0, 0.5, "(end of excerpt)")
        # Start back at first column:
        self.set_col(0)

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)


pdf = PDF()
pdf.set_title("20000 Leagues Under the Seas")
pdf.set_author("Jules Verne")
pdf.print_chapter(1, "A RUNAWAY REEF", "capítulo1.txt")
pdf.print_chapter(2, "THE PROS AND CONS", "capítulo2.txt")
pdf.output("demo.pdf")