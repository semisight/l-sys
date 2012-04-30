from PIL import Image, ImageDraw
from math import sin, cos, pi
import sys

def __strip_non_directives(inp):
	return [x for x in inp if x in 'F+-']

def make_image(raw_data, iters, growth, size):
	scale = pow(growth, iters)
	data =__strip_non_directives(raw_data)
	direction = 0

	move_dist = scale*size
	#loc = size*scale, size*scale
	loc = 0,0

	output = Image.new('RGBA', (size, size), (255,255,255))
	draw = ImageDraw.Draw(output)

	for rule in data:

		if rule == 'F':
			tmp_loc = loc[0] + move_dist*cos(direction), \
					  loc[1] + move_dist*sin(direction)

			draw.line((loc, tmp_loc), fill = (128, 128, 128))
			loc = tmp_loc
		elif rule == '+':
			direction -= pi/2
		elif rule == '-':
			direction += pi/2
		else:
			sys.stdout.write('This should never happen.\n')

	del draw
	return output