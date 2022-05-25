import os
from RGB2img import RGB2img
from base642RGB import base642RGB
from base64Encode import *


size = [400,100]
file_path = os.path.abspath("test_files/Bad_design_example-Le Yu.docx")

encoded = base64Encode(file_path)
RGB_array = base642RGB(encoded)
img = RGB2img(RGB_array,size)



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
img = ImageTk.PhotoImage(img)
canvas.create_image(2, 2, anchor=NW, image=img) 
#root.wm_attributes('-fullscreen',True)

root.mainloop()