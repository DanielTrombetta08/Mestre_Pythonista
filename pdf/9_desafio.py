import csv
from fpdf import FPDF


class PDF(FPDF):

    def colored_table(self, headings, rows, col_widths=(4.2, 3.9, 3.5)):
        # Colors, line width and bold font:
        self.set_fill_color(255, 100, 0)
        self.set_text_color(255)
        self.set_draw_color(255, 0, 0)
        self.set_line_width(0.03)
        self.set_font(style="B")
        for col_width, heading in zip(col_widths, headings):
            self.cell(col_width, 0.7, heading, border=1, align="C", fill=True)
        self.ln()
        # Color and font restoration:
        self.set_fill_color(224, 235, 255)
        self.set_text_color(0)
        self.set_font()
        fill = False
        for row in rows:
            self.cell(col_widths[0], 0.6, row[0],
                      border="LR", align="L", fill=fill)
            self.cell(col_widths[1], 0.6, row[1],
                      border="LR", align="L", fill=fill)
            self.cell(col_widths[2], 0.6, row[2],
                      border="LR", align="R", fill=fill)
            self.ln()
            fill = not fill
        self.cell(sum(col_widths), 0, "", "T")


def load_data_from_csv(csv_filepath):
    headings, rows = [], []
    with open(csv_filepath, encoding="utf8") as csv_file:
        for row in csv.reader(csv_file, delimiter=";"):
            if not headings:  # extracting column names from first row:
                headings = row
            else:
                rows.append(row)
    return headings, rows


colunas_carros_americanos, dados_carros_americanos = load_data_from_csv(
    "carros_americanos.csv")
colunas_carros_italianos, dados_carros_italianos = load_data_from_csv(
    "carros_italianos.csv")

pdf = PDF(unit='cm')
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(w=0, h=0.5, txt='Relatório de Vendas',
         align='c', new_x='LMARGIN', new_y='NEXT')
pdf.ln(1)

pdf.set_font("helvetica", style='', size=12)
pdf.multi_cell(
    w=0, h=0.5, txt='Para o mês de dezembro, foram registrados um total de 10 vendas para o setor de veículos importados', align='j', new_x='LMARGIN', new_y='NEXT')
pdf.ln(0.5)

pdf.set_font("helvetica", "B", 16)
pdf.cell(w=0, h=0.5, txt='Vendas de carros americanos',
         align='l', new_x='LMARGIN', new_y='NEXT')
pdf.ln(0.2)

pdf.set_font("helvetica", style='', size=12)
pdf.multi_cell(
    w=0, h=0.5, txt='Foram vendidos 5 carros americanos', align='j', new_x='LMARGIN', new_y='NEXT')
pdf.colored_table(colunas_carros_americanos, dados_carros_americanos)
pdf.ln(0.5)

pdf.set_font("helvetica", "B", 16)
pdf.cell(w=0, h=0.5, txt='Vendas de carros italianos',
         align='l', new_x='LMARGIN', new_y='NEXT')
pdf.ln(0.2)

pdf.set_font("helvetica", style='', size=12)
pdf.multi_cell(
    w=0, h=0.5, txt='Foram vendidos 5 carros italianos', align='j', new_x='LMARGIN', new_y='NEXT')
pdf.colored_table(colunas_carros_italianos, dados_carros_italianos)

pdf.output("demo1.pdf")