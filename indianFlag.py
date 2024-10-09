import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("white")

# Create a new turtle object
flower = turtle.Turtle()
flower.speed(7)  # Set the speed of drawing

# Function to draw a petal
def draw_petal(turt, radius, color):
    turt.fillcolor(color)
    turt.begin_fill()
    for _ in range(36):
        turt.forward(radius)
        turt.right(10)
    turt.end_fill()

# Draw the flower
flower.penup()
flower.goto(0, 0)  # Move to the center of the flower
flower.pendown()

# Draw the saffron petals
for _ in range(5):
    draw_petal(flower, 30, "orange")
    flower.right(72)

# Draw the white petals
for _ in range(5):
    draw_petal(flower, 20, "white")
    flower.right(72)

# Draw the green petals
for _ in range(5):
    draw_petal(flower, 10, "green")
    flower.right(72)

# Hide the turtle object
flower.hideturtle()

# Keep the window open
turtle.done()
