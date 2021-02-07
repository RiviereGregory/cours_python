import turtle


def escalier(taille, nb):
    for i in range(0, nb):
        if i == 0:
            t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        t.forward(taille)
        i = i + 1


def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)

def carres(taille_depart, nb):
    for i in range(0, nb):
        i += 1
        taille = i*taille_depart
        carre(taille)


t = turtle.Turtle()
# escalier(50, 5)
# carre(100)
carres(50, 5)

turtle.done()
