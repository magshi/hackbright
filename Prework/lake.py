import turtle
wn = turtle.Screen()
wn.bgcolor("#3C4544")

lake = turtle.Turtle()

donatello = turtle.Turtle()
donatello.color("#26A668")
donatello.shape("turtle")
donatello.ht()

lake.color("#3CBAC8")
lake.speed("fastest")

lake.up()
lake.left(90)
lake.forward(100)
lake.right(90)
lake.forward(175)
lake.right(180)
lake.down()

for i in range(5):
	lake.forward(350)
	lake.left(90)
	lake.up()
	lake.forward(5)
	lake.left(90)
	lake.down()
	lake.forward(350)
	lake.right(90)
	lake.up()
	lake.forward(5)
	lake.right(90)
	lake.down()
end

donatello.stamp()

wn.exitonclick()