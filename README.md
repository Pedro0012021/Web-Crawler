# Web-Crawler
Esse projeto vai ler um site em Html que vai trazer o resultado solicitado, no caso o resultado vai ser a quantidade de infectados no município de Cidade Ocidental de
acordo com o site da prefeitura.




#Web Crawler que vai abrir o html do site do município e de acordo com a última atualização traz o número de casos confirmados infectados pelo Coronavírus. 
#após a posição  <span class="red">Casos Confirmados: o resultado mostra as 5 casas após a variável "posicao". 



import urllib.request

content = urllib.request.urlopen("https://www.cidadeocidental.go.gov.br/").read()
content = str(content)
find = '<span class="red">Casos Confirmados:'
posicao= int(content.index(find)+ len(find))
casos = content[posicao: posicao + 5]
print('Casos confirmados infectados pelo coronavírus no município de Cidade Ocidental:',casos)

