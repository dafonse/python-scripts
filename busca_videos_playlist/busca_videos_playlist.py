import json
import os
import webbrowser

import requests
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()  # Load the .env file
api_key = os.getenv("API_KEY")
playlistid = "PL8GnYZim3SzbHyNgmBmCEl8PjI_H7uxpT"
url2 = 'https://www.yout.com/watch?v='
lista = []
lista_links = []
quant = 0

# IMPORTANTE: A PLAYLIST DEVE ESTAR EM MODO >>>>>PÚBLICO<<<<<


def busca():
    page = ''
    seq = 0
    print('Buscando...')
    while True:

        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&pageToken={pg}&playlistId={id}&key={key}'.format(
            pg=page, key=api_key, id=playlistid
        )

        req = requests.get(url)
        dicionario = json.loads(req.text)

        if 'error' in dicionario:
            print(f"Erro encontrado: {dicionario['error']['message']}")
            break
        elif 'pageInfo' in dicionario:
            print(f"Foram encontrados {dicionario['pageInfo']['totalResults']} resustados.")

            for filme in dicionario['items']:
                lista.append('{}) {}'.format(seq, filme['contentDetails']['videoId']))
                lista_links.append(url2 + filme['contentDetails']['videoId'])
                seq += 1

        if 'nextPageToken' in dicionario:
            page = dicionario['nextPageToken']
        else:
            break

    if 'pageInfo' in dicionario:
        return dicionario['pageInfo']['totalResults']


def imprime(l):
    """
    Recebe uma lista e imprime seus elementos.
    """
    for i in l:
        print(i)


def abrir_url(url):
    """
    Recebe uma lista de links e abre-os no navegador
    padrão do sistema operacional.
    """
    for i in url:
        print(f'Abrindo: {i}')
        webbrowser.open(i)
        clica(i)


def clica(url):
    driver = webdriver.Firefox()
    driver.get(url)
    button = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div[2]/div[3]/div[3]/div[5]/button").click()


while True:
    lista.clear()
    lista_links.clear()
    quant = busca()
    imprime_esc = input('Deseja imprimir a lista? (Y/N): ')

    if imprime_esc.lower() == 'y':
        # imprime(lista)
        imprime(lista_links)

    abre_url = input(f'Deseja abrir as {quant} urls no navegador? (Y/N): ')

    if abre_url.lower() == 'y':
        abrir_url(lista_links[:5])

    break

print('Encerrado!')
print('Encerrado!')
