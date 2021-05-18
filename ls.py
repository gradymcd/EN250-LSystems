import turtle
import re
import ast

#turtle.speed(500)

#rules = {'F':'FLFRRFLF'}
rulesstr = input("Rules('1':'11', '0':'1[0]0): ")
if rulesstr == '':
	rules = {'1':'11', '0':'1[0]0'}
else:
	rules = ast.literal_eval('{' + re.sub("([A-Za-z0-9]+):([A-Za-z0-9]+)", r'"\1":"\2"', rulesstr) + '}')
iterations = input("Iterations (4): ")
if iterations == '':
	iterations = '4'
iterations = int(iterations)
angle = input("Angle(45): ")
if angle == '':
	angle = '45'
angle = int(angle)
distance = input("Distance (20): ")
if distance == '':
	distance = '20'
distance = int(distance)



#{'1':'11', '0':'1[0]0'}

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
print("Result string: ", M)

t.pu()
t.left(90)
t.back(512)
t.pd()
t.speed(10)

draw(M)
input("press enter to exit")
t.done()
