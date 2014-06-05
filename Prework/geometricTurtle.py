import turtle
wn = turtle.Screen()
wn.bgcolor("#C8B4AC")

nathanael = turtle.Turtle()
nathanael.color("#2CA29B")
nathanael.speed("fastest")
nathanael.shape("triangle")

nathanael.up()
nathanael.goto(40, 155)
nathanael.down()
nathanael.begin_fill()

# draw Nathanael's shell
nathanael.right(30)
nathanael.forward(120)
nathanael.right(45)
nathanael.forward(120)
nathanael.right(105)
nathanael.forward(275)
nathanael.right(105)
nathanael.forward(120)
nathanael.right(45)
nathanael.forward(120)
nathanael.end_fill()
nathanael.up()

# draw Nathanael's Easter-yellow head
nathanael.color("#F9E157")
nathanael.goto(-85, 95)
nathanael.left(225)
nathanael.down()

nathanael.begin_fill()
nathanael.forward(70)
nathanael.right(90)
nathanael.forward(65)
nathanael.right(45)
nathanael.forward(50)
nathanael.right(90)
nathanael.forward(75)
nathanael.right(68)
nathanael.forward(54)
nathanael.end_fill()
nathanael.up()

# now we're gonna draw his feet
nathanael.goto(-30, -35)
nathanael.down()
nathanael.right(140)
nathanael.begin_fill()
for i in range(3):
    nathanael.forward(70)
    nathanael.left(120)
nathanael.end_fill()
nathanael.up()

nathanael.goto(170, -35)
nathanael.down()
nathanael.begin_fill()
for i in range(3):
    nathanael.forward(70)
    nathanael.left(120)
nathanael.end_fill()
nathanael.up()

# he's not a turtle without a tail
nathanael.goto(155, 90)
nathanael.down()
nathanael.begin_fill()
nathanael.right(75)
for i in range(4):
    nathanael.right(120)
    nathanael.forward(35)
nathanael.end_fill()
nathanael.up()

# let's give him some personality
nathanael.color("#F7E6F1")
nathanael.goto(-145, 95)
for i in range(8):
    nathanael.right(60)
    nathanael.stamp()
nathanael.goto(-160, 60)
nathanael.stamp()

# now for some shell texture
nathanael.goto(35, 87)
nathanael.right(180)
for i in range(27):
    nathanael.stamp()
    nathanael.right(25)
    nathanael.forward(10+i)
    
# he needs some pink grass to eat
nathanael.color("#A61F43")
nathanael.goto(-200, -150)
nathanael.right(2)

for i in range(45):
    nathanael.stamp()
    nathanael.right(90)
    nathanael.forward(10)
    nathanael.left(90)

nathanael.down()
nathanael.left(90)
nathanael.begin_fill()
nathanael.forward(500)
nathanael.left(90)
nathanael.forward(50)
nathanael.left(90)
nathanael.forward(500)
nathanael.end_fill()