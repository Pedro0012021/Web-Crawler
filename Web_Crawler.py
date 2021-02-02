import urllib.request

#Web Crawler que vai abrir o html do site do município e de acordo com a última atualização traz o número
#de casos confirmados infectados pelo Coronavírus.
#após a posição 
# <span class="red">Casos Confirmados: tras 5 casas adiante. 
content = urllib.request.urlopen("https://www.cidadeocidental.go.gov.br/").read()
content = str(content)
find = '<span class="red">Casos Confirmados:'
posicao= int(content.index(find)+ len(find))
casos = content[posicao: posicao + 5]
print('Casos confirmados infectados pelo coronavírus no município de Cidade Ocidental:',casos)


