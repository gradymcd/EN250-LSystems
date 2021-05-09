import turtle

turtle.speed(500)


def square_spiral(walls):
	def square_spiral_helper(walls, distance, initial, count):
		if count == walls:
			turtle.done()
		turtle.left(90)
		turtle.forward(distance)
		square_spiral_helper(walls, distance + initial * (count % 2), initial, count + 1)
	
	square_spiral_helper(walls, 20, 20, 0)


square_spiral(50)


def octagonal_spiral(walls):
	def octagonal_spiral_helper(walls, distance, initial, count):
		if count == walls:
			turtle.done()
		turtle.left(10)
		turtle.forward(distance)
		octagonal_spiral_helper(walls, distance + initial * (count % 2), initial, count + 1)
	
	octagonal_spiral_helper(walls, 5, 1, 0)


#octagonal_spiral(400)
