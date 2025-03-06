import cv2

"""
title: Image Processing with OpenCV and Matplotlib
description: This script performs image processing tasks such as color channel swapping and region copying using OpenCV and displays the modified image using Matplotlib.
input_files:
  - youtube_opencv/img/ada.jpeg
output_files:
  - youtube_opencv/img/ada_modificado.png
functions:
  - showImage(img): Converts the image from BGR to RGB and displays it using Matplotlib.
  - getColor(img, y, x): Retrieves the color values (B, G, R) at a specific (y, x) position in the image.
  - setColor(img, y, x, b, g, r): Sets the color values (B, G, R) at a specific (y, x) position in the image.
  - main(): Reads an image, prints its dimensions and color channels, swaps the green and blue channels for each pixel, copies a region of the image, saves the modified image, and displays it.
"""


def showImage(img):
    from matplotlib import pyplot as plt

    # convertendo padrao para mostrar corretamento no plt
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()


def getColor(img, y, x):
    # coletando o valor do canal de cor em determinada posição
    return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)


def setColor(img, y, x, b, g, r):
    # padrão BGR: setando o canal para determinado valor
    img.itemset((y, x, 0), b)
    img.itemset((y, x, 1), g)
    img.itemset((y, x, 2), r)


def main():
    # obj_img = cv2.imread("youtube_opencv/img/ada.jpeg", 0) # preto e branco
    obj_img = cv2.imread("youtube_opencv/img/ada.jpeg")
    altura, largura, canais_de_cor = obj_img.shape
    print("dimensões da imagem: " + str(largura) + "x" + str(altura))
    print("canais de cor: ", canais_de_cor)

    for y in range(0, altura):
        for x in range(0, largura):

            azul, verde, vermelho = getColor(obj_img, y, x)

            setColor(obj_img, y, x, verde, azul, vermelho)

            # print(obj_img[x][y])
            # input()

    eye_img = obj_img[164 : 164 + 30, 97 : 97 + 30]  # primeiro o y de depois o x
    obj_img[352 : 352 + eye_img.shape[0], 157 : 157 + eye_img.shape[1]] = eye_img

    cv2.imwrite("youtube_opencv/img/ada_modificado.png", obj_img)

    showImage(obj_img)


main()
