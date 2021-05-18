import turtle

#turtle.speed(500)

#rules = {'F':'FLFRRFLF'}
rules = {'1':'11', '0':'1[0]0'}
iterations = 6
distance = 10
angle = 45
stack = []

def apply_rules(axiom):
	for i in range(iterations):
		for key in rules:
			axiom = axiom.replace(key, rules[key])
	return axiom

def draw(M):
	for m in M:
		if m == 'F':
			t.forward(distance)
		if m == 'B':
			t.backward(distance)
		if m == 'L':
			t.left(angle)
		if m == 'R':
			t.right(angle)
		if m == '[': # push position and angle, turn left 45 degrees
			stack.append([t.pos(), t.heading()])
			t.left(angle)
		if m == ']': # pop position and angle, turn right 45 degrees
			p = stack.pop()
			t.pu()
			t.setpos(p[0])
			t.setheading(p[1])
			t.right(angle)
			t.pd()
		if m == '0' or m == '1': # draw a line segment ending in a leaf
			t.forward(distance)

t = turtle.Turtle()
M = apply_rules("0")
print(M)

t.pu()
t.left(90)
t.back(400)
t.pd()
t.speed(10)

draw(M)
input("press enter to exit")
t.done()
