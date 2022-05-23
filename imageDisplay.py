from tkinter import *  
from PIL import ImageTk,Image  
import time
timeout = time.time() + 6   # 6 seconds from now

root = Tk()  
canvas = Canvas(root, width = 1920, height = 1080)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("FHDtest.png"))  
canvas.create_image(0, 0, anchor=NW, image=img) 
root.attributes('-fullscreen',True)

while True:
    root.mainloop()
    if time.time() > timeout:
        root.destroy()
        break
