import turtle
wn = turtle.Screen()
arachne = turtle.Turtle()
wn.bgcolor("#BBDFBC")
arachne.color("black")
arachne.shape("arrow")

legs = int(input("How many legs do you grant the hellbeast? "))
angle = 360/legs

for i in range(legs):

	# turn the appropriate angle, draw a leg
    arachne.right(angle)
    arachne.forward(150)
    
    # turn a little to give the legs creepy hooks
    arachne.right(30)
    arachne.forward(35)
    arachne.forward(-35)
    arachne.left(30)

    # turn around, head back to the center, and turn around to prepare for next loop iteration
    arachne.right(180) 
    arachne.forward(150)
    arachne.right(180)

# draw the spider's horrifying and poisonous abdomen
arachne.shape("circle")
arachne.color("#722521")

wn.exitonclick()