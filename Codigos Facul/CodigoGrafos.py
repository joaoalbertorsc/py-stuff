import turtle
import math

# Função para desenhar um círculo com número dentro
def draw_circle_with_number(t, x, y, radius, number):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(radius)
    t.penup()
    t.goto(x, y - radius - 20)
    t.pendown()
    t.write(number, align="center", font=("Arial", 30, "normal"))
    t.hideturtle()

# Função para desenhar uma seta apontando para um círculo
def draw_arrow_to_circle(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

# Leitura dos dados do arquivo de texto
with open("grafo_5.txt", "r") as file:
    lines = file.readlines()

# Configuração inicial
screen = turtle.Screen()
screen.setup(800, 600)  # Configura o tamanho da janela
screen.bgcolor("white")

# Centralizar o desenho na tela
width = screen.window_width()
height = screen.window_height()

# Parâmetros para desenhar os círculos em uma ordem circular
radius = min(width, height) / 2 - 50
center_x = 0
center_y = 0
num_circles = len(lines) + 1
angle_step = 360 / num_circles

# Lista para armazenar os círculos desenhados
circles = {}

# Desenhar os círculos
for i, line in enumerate(lines):
    x, y = map(int, line.split())
    angle = math.radians(i * angle_step)
    circle_x = center_x + math.cos(angle) * radius
    circle_y = center_y + math.sin(angle) * radius

    circle = turtle.Turtle()
    circle.shape("circle")
    circle.color("blue")
    circle_radius = 20
    draw_circle_with_number(circle, circle_x, circle_y, circle_radius, str(x))
    circles[x] = circle

# Desenhar as setas
for line in lines:
    x, y = map(int, line.split())
    circle1 = circles[x]
    circle2 = circles[y]
    arrow = turtle.Turtle()
    arrow.shape("arrow")
    arrow.color("black")
    draw_arrow_to_circle(arrow, circle1.xcor(), circle1.ycor(), circle2.xcor(), circle2.ycor())

# Finalização do desenho
turtle.done()
