from PIL import Image
import numpy as np
size = [1916, 1076]

#input a 1D list contains RGB values
#return a image of global size dimension 
def RGB2img(pixels):
	global size
	assert size[0] * size[1] >= len(pixels)
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




### base64 to RGB value

import string
alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
assert alphabet[0] == 'A'
assert alphabet[20] == 'U'
assert alphabet[62] == '+'

RGB_list = []
RGB_values = [0,85,170,255]
for i in range(4):
	for j in range(4):
		for k in range(4):
			RGB_list.append([RGB_values[i],RGB_values[j],RGB_values[k]])
RGB_list = tuple(RGB_list)

base642RGB_dict = {}

for i in range(64):
	base642RGB_dict[str(alphabet[i])] = RGB_list[i]

base64Index = {k: v for v, k in enumerate(alphabet)}
assert base64Index['A'] == 0
#input a list of base64 String
#return a 1D list of RBG pixel values
def base642RGB(base64_string):
	#unit test

	#/ unit test

	global base642RGB_dict
	global base64Index

	RGB_list = []
	
	l = list(base64_string)
	for i in l:
		RGB_list.append(base642RGB_dict[i])
	#print(l)
	return RGB_list



#input a directory path
#output a list for all the full system path of the files under the input 
def dir2fileList(directory_path):
	return

#input to be a full file path
#output a string of base64 encoded file
def file2txt(file_path):
	return

#input a text, return a size[0]*size[1] image
#each text is a self contained packet
#each image should contain 6bit * 1920*1080 data
def txt2image(text):
	max_text_size = size[0]*size[1]-200

	if text.size() > max_text_size:
		return null
	return


from tkinter import *  
from PIL import ImageTk,Image  
import time
timeout = time.time() + 6   # 6 seconds from now

root = Tk()  
canvas = Canvas(root, width = size[0], height = size[1])  
canvas.pack()  
img = ImageTk.PhotoImage(RGB2img(base642RGB(("A"*1920+"B"*1920+"C"*1920)+"D"*1920+"E"*1920+"Z"*1920)*10))
canvas.create_image(2, 2, anchor=NW, image=img) 
root.wm_attributes('-fullscreen',True)

while True:
    root.mainloop()
    if time.time() > timeout:
        root.destroy()
        break