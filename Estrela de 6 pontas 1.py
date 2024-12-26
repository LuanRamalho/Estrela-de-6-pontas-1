import turtle
import random

def draw_triangle(t, size, color, pointing_up=True):
    """Desenha um triângulo equilátero preenchido."""
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        if pointing_up:
            t.left(120)
        else:
            t.right(120)
    t.end_fill()

def draw_star_of_david():
    """Desenha uma estrela de 6 pontas (Estrela de Davi) com uma cor aleatória."""
    # Configurar a tela e a tartaruga
    screen = turtle.Screen()
    screen.title("Estrela de Davi")
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # Escolher uma cor aleatória
    color = random.choice(['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan', 'magenta'])

    # Definir o tamanho dos triângulos
    size = 200

    # Desenhar o triângulo apontando para cima
    t.penup()
    t.goto(-size / 2, -size / (2 * (3**0.5)))
    t.pendown()
    draw_triangle(t, size, color, pointing_up=True)

    # Desenhar o triângulo apontando para baixo
    t.penup()
    t.goto(-size / 2, size / (2 * (3**0.5)))
    t.pendown()
    draw_triangle(t, size, color, pointing_up=False)

    # Manter a janela aberta
    screen.mainloop()

# Executar o programa
draw_star_of_david()
