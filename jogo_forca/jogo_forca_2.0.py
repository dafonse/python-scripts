# Title: Jogo da Forca (Hangman Game)
# Description: This script implements a simple hangman game where the user has to guess the letters of a secret word.
# Author: dafonse
# Date: 05/03/2025
# Version: 2.0
# Usage: Run the script and follow the prompts to guess the letters of the secret word.
# Requirements: Python 3.x
# Notes: The secret word is hardcoded as 'canino'. The user is prompted to input one letter at a time.

palavra_secreta = 'canino'
letras = []

while True:
    letra = input('Informe uma letra: ')

    if len(letra) > 1 or not letra.isalpha():
        print('Informe apenas uma letra.')
        continue

    palavra_temp = ''

    if letra in palavra_secreta:
        letras.append(letraa)

    for l in palavra_secreta:
        if l in letras:
            palavra_temp += l
        else:
            palavra_temp += '_'

    if palavra_secreta == palavra_temp:
        print(f'Parabéns, a palavra secreta é {palavra_temp.upper()}!!!')
        break

    print(palavra_temp)
