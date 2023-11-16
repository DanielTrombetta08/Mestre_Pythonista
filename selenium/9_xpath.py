# Como montar um XPATH
# De forma geral você vai montar um xpath da seguinte forma
//tag[@atributo="valor"]

# Ultra genérico(engloba todas tags da página)
//* 

# Ultra genérico + tag
//*[tag]

# apenas contem um parte do texto
//*[contains(text(),"Exemplo")] 
//*[contains(text(),"Exemplo") or contains( text(), "Dropdown" )]
//*[contains(text(),'Dropdown') and  contains(text(),'Bootstrap') ]

# Inicia com um texto
//*[starts-with(text(),"Exemplo")]
//*[starts-with(@class,"btn")]

# Buscando apenas por um texto spefícico
//*[text()="Exemplo Checkbox"] # Genérico, porém especificando o texto
//h4[text()="Exemplo Checkbox"] # Com tag e especificando o texto

# Buscando por um elemento específico usando tag e propriedade
//button[@id="dropdownMenuButton"] # tag com propriedade e valor
//section[@class="jumbotron"] # tag com propriedade e valor
//div[@class="form-check"] #tag com propriedade e valor

# Como encontrar filhos de cada elemento
# Encontra único filho
//div/fieldset
//div/fieldset/h4
# Encontrar filho, quando há multiplos filhos
# Find child when multiple elements
//thead/tr//th[2]

