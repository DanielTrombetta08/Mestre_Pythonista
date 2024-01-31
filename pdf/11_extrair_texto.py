from pdfminer.high_level import extract_text,extract_pages
from pdfminer.layout import LTTextContainer

# # Imprimir todo o texto contido em um PDF
# text = extract_text('historias.pdf')
# # print(text)
# if 'Mexico' in text:
#     print('Estamos no PDF historias.pdf')

# # Salvar texto do PDF para um arquivo de texto
# with open('historias.txt','w') as file:
#     file.write(text)
# Como extrair partes de um texto ou fazer qualquer operação com base em um texto que está dentro de um pdf
for page_layout in extract_pages('demo.pdf'):
    for element in page_layout:
        if isinstance(element,LTTextContainer):
            if '5 carros italianos' in element.get_text():
                print('Encontrado frase sobre 5 carros italianos')
                print(element.get_text())


from pdfminer.high_level import extract_text


# Extrair texto apenas de algumas páginas
text = extract_text('historias.pdf', page_numbers=[0, 1])
# print(text)
# Extrair textos de até X páginas
text = extract_text('historias.pdf', maxpages=2)
print(text)