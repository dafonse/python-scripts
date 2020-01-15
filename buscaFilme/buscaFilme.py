import requests
import json

api_key = "APIKEY"
lista = []


# é um método, pois não tem retorno e só modifica a lista[]
def busca(buscar):
    page = 1
    seq = 1
    print('Buscando...')
    while True:
        req = requests.get(
            'http://www.omdbapi.com/?apikey={key}&s={search}&type=movie&page={page}'.format(key=api_key, search=buscar, page=page))
        dicionario = json.loads(req.text)

        if dicionario['Response'] == 'False':
            print('Nenhum resultado encontrado!') if page == 1 else None
            break
        elif page == 1:
            print('Foram encontrados {} resustados.'.format(
                dicionario['totalResults']))

        for filme in dicionario['Search']:
            lista.append('{}) {}'.format(seq, filme['Title']))
            seq += 1

        page += 1


def imprime():
    for i in lista:
        print(i)


while True:
    lista.clear()
    escolha = input('Qual filme deseja pesquisar? (S para sair): ')
    if escolha.lower() == 's':
        print('Saindo do script...')
        break
    busca(escolha)
    imprime_esc = input('Deseja imprimir a lista? (Y/N): ')
    if imprime_esc.lower() == 'y':
        imprime()

print('Encerrado!')
