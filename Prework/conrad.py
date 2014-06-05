import turtle
wn = turtle.Screen()
wn.bgcolor("#61231D")

lake = turtle.Turtle()

lake.color("#3CBAC8")
lake.shape("classic")

# draw the base of the tree
lake.up()
lake.forward(-50)
lake.right(90)
lake.forward(20)
lake.circle(100)
lake.beginfill()
lake.hideturtle()

eyes = turtle.Turtle()
eyes.color("#26A668")
eyes.forward(20)
