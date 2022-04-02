# Umbrella RE logo (turtle) :: github.com/sliatecinos
import turtle

# :: Configs. ::
fatias = 8
angulo = 112.5

u = turtle.Turtle()

u.shape('turtle')
u.width(8)
u.right(angulo)

# :: Criando desenho ::
for i in range(fatias):
    u.begin_fill()
    if i % 2 == 0:
        u.color('black', 'ivory')
        u.pencolor()
        'black'
        u.fillcolor()
        'ivory'
    else:
        u.color('black', 'DarkRed')
        u.pencolor()
        'black'
        u.fillcolor()
        'DarkRed'

    u.forward(200)
    u.left(angulo)
    u.forward(155)   # tam. base fatias
    u.left(angulo)
    u.forward(200)
    u.right(180)   # volta 180º para criar prox. fatia

    u.end_fill()

