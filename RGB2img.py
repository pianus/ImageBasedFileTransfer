from PIL import Image
import numpy as np

#input a 1D list contains RGB values
#return a image of global size dimension 
def RGB2img(pixels, size):
	#assert size[0] * size[1] > len(pixels)
	#print(type(pixels))
	#assert type(pixels) == 'list'
	#print(pixels)
	print(len(pixels))
	pixels += [[255,255,255]] * (size[0] * size[1] - len(pixels))
	print(len(pixels))
	pixels2D = []
	for i in range(size[1]): 
		pixels2D.append(pixels[i*size[0]:(i+1)*size[0]-1])
	#print(pixels2D[0])
	# Convert the pixels into an array using numpy
	array = np.array(pixels2D, dtype=np.uint8)

	# Use PIL to create an image from the new array of pixels
	new_image = Image.fromarray(array)
	new_image.save('new.png')
	return new_image