# Title: Jogo da Forca (Hangman Game)
# Description: This script implements a simple hangman game where the user has to guess the letters of a secret word.
# Author: dafonse
# Date: 05/03/2025
# Version: 1.0
# Usage: Run the script and follow the prompts to guess the letters of the secret word.
# Requirements: Python 3.x
# Notes: The secret word is hardcoded as 'canino'. The user is prompted to input one letter at a time.

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
