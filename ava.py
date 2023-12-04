from turtle import Turtle,onscreenclick, onkey, listen, Screen
leo = Turtle ()
tela = Screen()
leo.speed(0)
resultado = 0
numero = 0

def trocar ():
    global resultado
    global numero
    numero = numero + 1
    resultado = numero % 2


leo.forward(100)
leo.backward(100)
leo.right(90)
leo.forward(100)
leo.left(180)
leo.forward(100)
leo.forward(100)
leo.backward(100)
leo.left(90)
leo.forward(100)
leo.left(180)
leo.forward(200)
leo.left(90)
leo.forward(100)
leo.backward(100)
leo.right(90)
leo.forward(100)
leo.backward(100)
leo.right(90)
leo.forward(100)
leo.right(90)
leo.forward(200)
leo.backward(300)
leo.forward(100)
leo.left(90)
leo.forward(100)
leo.backward(100)
leo.right(90)
leo.forward(100)
leo.left(90)
leo.forward(100)


def jogar(x, y): 
    leo.penup()
    leo.goto(x, y)
    if resultado == 0:
        x2()
    if resultado == 1:
        circulo()
    trocar()

def circulo():
    leo.color('green')
    r = 50
    leo.pendown()
    leo.circle(r)

def x2():
    leo.color('purple')
    leo.pendown()
    leo.right(45)
    for _ in range(4):
        leo.forward(70)
        leo.forward(-70)
        leo.right(90)
    leo.left(45)

tela.onscreenclick(jogar)

listen()
tela.mainloop()