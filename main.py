from contorno import contorno
from operadorMorfologico import operadorMorfologico
from espacoCores import espacoCores

if __name__ == '__main__':
    imgs = ["./Aviao.jpeg", "./GIRAFA.jpeg", "./Satelite.jpeg"]

    for img in imgs:
        contorno(img)
        operadorMorfologico(img)
        espacoCores(img)