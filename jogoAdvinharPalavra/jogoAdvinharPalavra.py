palavra = 'cachorro'
vazio = ''


def advinhar(preencher, letra):
    temp = ''
    for i, v in enumerate(palavra):
        if preencher[i] == '_' and letra != v:
            temp = temp + '_'
            continue
        temp = temp + v
    return temp

def check():
    if vazio == palavra:
        print('Parabéns!!!')
        return True
    else:
        True


def prencher(word=palavra):
    global vazio
    for i in range(len(word)):
        vazio = vazio + '_'


prencher()

while True:
    x = input('Informe uma letra (SAIR para sair do script): ')
    if x.lower() == 'sair' or check():
        break
    elif len(x) > 1 or not x.isalpha:
        print('Informe apenas uma letra!')
    vazio = advinhar(vazio, x)
    print(vazio)
