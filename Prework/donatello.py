import turtle
wn = turtle.Screen()
wn.bgcolor("#3C4544")

donatello = turtle.Turtle()

donatello.color("#3CBAC8")
donatello.speed("fastest")
donatello.up()
donatello.goto(-150, 160)
donatello.down()
donatello.begin_fill()

for i in range(4):
    donatello.forward(300)
    donatello.right(45)
    donatello.forward(25)
    donatello.right(45)

donatello.end_fill()

donatello.color("#26A668")
donatello.shape("turtle")
donatello.up()
donatello.goto(0, 0)

for i in range(20):
	donatello.forward(int(i*2))
	donatello.stamp()
	donatello.left(90)

	import turtle
wn = turtle.Screen()
wn.bgcolor("#3C4544")

donatello = turtle.Turtle()

donatello.color("#3CBAC8")
donatello.speed("fastest")
donatello.up()
donatello.goto(-150, 160)
donatello.down()
donatello.begin_fill()

for i in range(4):
    donatello.forward(300)
    donatello.right(45)
    donatello.forward(25)
    donatello.right(45)

donatello.end_fill()

donatello.color("#26A668")
donatello.shape("turtle")
donatello.up()
donatello.goto(-130, 130)

for rainbowcolor in ['red', 'orange', 'yellow', 'green', 'blue', 'purple']:
    donatello.color(rainbowcolor)
    for i in range(10):
        donatello.stamp()
        donatello.forward(50)
    for i in range(7):
        donatello.goto(-130, 130-i*10)