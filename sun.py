import turtle
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
Colors = ["yellow", "red", "yellow","orange"]

for i in range(120):
	for c in Colors:
		turtle.color(c)
		turtle.circle(200-1, 100)
		turtle.lt(98)
		turtle.circle(200-i, 100)
		turtle.rt(60)
		turtle.end_fill()
turtle.mainloop()