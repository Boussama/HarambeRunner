from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import Image, ImageTk
import os

# Variables
margin = 150
ratio = 1
filePath = "/Users/MacBook/offlineDesktop/python/HarambeRunner/actual.png"

# Functions
def loadImage():
	global rawImage
	global img
	rawImage.close()
	rawImage = Image.open(filePath)
	#resizing the image to fit the screen with the new ratio
	rawImage = rawImage.resize((int(canvasImgWidth), int(canvasImgHeight)) ,Image.ANTIALIAS)
	img = ImageTk.PhotoImage(rawImage)
	#refresh the image
	canvas.itemconfig(canvasImageRef, image=img)

def printcoords(event):
	#normalise the coordinate by dividing by the ration
	mouseX = int( float(event.x) / float(ratio) )
	mouseY = int( float(event.y) / float(ratio) )

    #outputting x and y coords to console
	print (mouseX,mouseY)
	os.system("monkeyrunner HarambeBridge.py " + str(mouseX) + " " + str(mouseY) )
	print "salam"
	loadImage()

root = Tk()
rawImage = Image.open(filePath)

# Adapting img to screen

canvasImgWidth = rawImage.width
canvasImgHeight = rawImage.height

if canvasImgWidth > (root.winfo_screenwidth() - margin):
	ratio = float( float(root.winfo_screenwidth() - margin) / float(canvasImgWidth) )
	canvasImgWidth *= ratio
	canvasImgHeight *= ratio

if canvasImgHeight > (root.winfo_screenheight() - margin):
	ratio = float( float(root.winfo_screenheight() - margin) / float(canvasImgHeight) )
	canvasImgWidth *= ratio
	canvasImgHeight *= ratio

#resizing the image to fit the screen with the new ratio
rawImage = rawImage.resize((int(canvasImgWidth), int(canvasImgHeight)) ,Image.ANTIALIAS)
img = ImageTk.PhotoImage(rawImage)

canvas = Canvas(root, bd=0, width=canvasImgWidth, height=canvasImgHeight)
canvasImageRef = canvas.create_image(0,0,image=img, anchor="nw")

#mouseclick event
canvas.bind("<Button 1>",printcoords)

canvas.pack()
root.mainloop()