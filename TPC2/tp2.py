import re

#markdown to html converter
# Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
#In: # Exemplo
#Out: <h1>Exemplo</h1>

#Bold: pedaços de texto entre "**":
#In: Este é um **exemplo** ...
#Out: Este é um <b>exemplo</b> ...

#Itálico: pedaços de texto entre "*":
#In: Este é um *exemplo* ...
#Out: Este é um <i>exemplo</i> ...

# Lista numerada:
#In:
#1. Primeiro item
#2. Segundo item
#3. Terceiro item

#out
#<ol>
#<li>Primeiro item</li>
#<li>Segundo item</li>
#<li>Terceiro item</li>
#</ol>

 #Link: [texto](endereço URL)
 #In: Como pode ser consultado em [página da UC](http://www.uc.pt)
 #out Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>

 #imagem ![texto alternativo](path para a imagem)
#in In: Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
#Out: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...

def markdown2html(text):

    #cabeçalhos
    text = re.sub(r'(\n|^)### (.*)', r'\1<h3>\2</h3>', text,flags=re.MULTILINE)
    text = re.sub(r'(\n|^)## (.*)', r'\1<h2>\2</h2>', text,flags=re.MULTILINE)
    text = re.sub(r'(\n|^)# (.*)', r'\1<h1>\2</h1>', text,flags=re.MULTILINE)

    #bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)



    #itálico
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    



    #lista numerada
    text = re.sub(r"^[0-9]+\.(.+)$", r"\t<li>\1</li>", text, flags = re.MULTILINE)
    text = re.sub(r"((\t<li>.+</li>\n)+)", r"<ol>\n\1</ol>\n", text, flags = re.MULTILINE)

      # imagem
    text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', text)

    #link
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
   
   
    
    return text




 
    

exemplo = '''
# Exemplo

Este é um **exemplo** ...

Este é um *exemplo* ...

1. Primeiro item
2. Segundo item
3. Terceiro item

Como pode ser consultado em [página da UC](http://www.uc.pt)

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
'''

htmlconversed = markdown2html(exemplo)


print(htmlconversed)