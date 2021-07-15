# Let's draw some drawings with the package turtle (built into python)

# 1st import turtle
import turtle
# # Let's get a nice set-up in turtle
turtle.bgcolor("black")      # bgcolor = background colour, standard bg is white
turtle.pensize(2)            # pen size to draw the purple
turtle.color("pink")
turtle.speed(0)              # drawing happens instantly, without it it'll take a while

# draw a square
# Note: turtle always draws from the centre (hence the arrow)
# if you want to draw elsewhere, make adjustments to lift the pen
# longer method
turtle.forward(50)  # turtle moves forward 50
turtle.left(90)     # turtle turns left 90 degrees
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.done()        # allows turtle to stay on the screen
# appears on the textbox, not the pycharm app

# highlight section, command + / --> to hashtag it so it doesn't run




# nice little project in turtle - create a nice drawing
# 1st import turtle
import turtle
# 'for' loop (short method)
for colours in ["blue", "grey", "yellow", "pink", "green", "red"]:   # 6 different colours, 6 different turtles
     turtle.color(colours)
     turtle.circle(150)  # pen size is 150
     turtle.left(60)     # moves the circle 60 degrees, creating a pattern
 turtle.done()




# let's make it cooler
# circles will move 10 degrees each time & loop round again
for i in range(6):
    for colours in ["blue", "grey", "yellow", "pink", "green", "red"]:  # 6 different colours, 6 different turtles
        turtle.color(colours)
        turtle.circle(150)  # pen size is 150
        turtle.left(10)  # moves the circle 10 degrees, creating a pattern with more circles
turtle.done()




# draw a pentagon

import turtle

turtle.bgcolor("pink")      # bgcolor = background colour, standard bg is white
turtle.pensize(14)           # pen size to draw the purple
turtle.color("black")
turtle.speed(100)

# short method --> use 'for' loop
# pentagon: 360 /5 = 72 print(360 / 5)
for i in range(5):
    turtle.right(72)
    turtle.forward(80)      # length of the pentagon sides
turtle.done()


