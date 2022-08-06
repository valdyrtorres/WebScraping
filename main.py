from config import URL, URL_BASE
import requests, csv
from bs4 import BeautifulSoup

paginas = []

headers = {
    'User-Agent': 'Valdir Torres Borges',
    'From': 'valdyrtorres@yahoo.com.br'
}

# Criando um arquivo .csv
arquivo_csv = csv.writer(open('nomes_artistas_z.csv', 'w',  newline='\n'))
arquivo_csv.writerow(['Nomes_Artistas', 'URL_Artistas'])

for num_page in range(1, 5):
    paginas.append(f'http://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ{num_page}.htm')

for url_por_pagina in paginas:
    pagina = requests.get(url_por_pagina, headers=headers)
    soup = BeautifulSoup(pagina.text, 'html.parser')

    #Remover links inferiores
    ultimos_links = soup.find(class_='AlphaNav')
    ultimos_links.decompose()

    # Pegar o conteúdo da body test
    bloco_nomes_artistas = soup.find(class_='BodyText')
    lista_nomes_artistas = bloco_nomes_artistas.find_all('a')

    print()
    for nome_artista in lista_nomes_artistas:
        nomes = nome_artista.contents[0]
        links = f"{URL_BASE}{nome_artista.get('href')}'"
        arquivo_csv.writerow([nomes, links])
        print(nomes)
        print(links)

print()
print(bloco_nomes_artistas)

print()
print(lista_nomes_artistas)




