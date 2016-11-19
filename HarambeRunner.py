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
	print ("salam")
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
canvas.grid(row=0, column=0, rowspan=8)
canvasImageRef = canvas.create_image(0,0,image=img, anchor="nw")

coordLabel = Label(root, text="Coord (0,0)")
coordLabel.grid(row=0, column=1, sticky=W)

delayLabel = Label(root, text="Delay")
delayLabel.grid(row=1, column=1, sticky=W)

delayEntry = Entry(root, bg="blue")
delayEntry.grid(row=1, column=2)
delayEntry.insert(0,"1")

nextButton = Button(root, text="Next")
nextButton.grid(row=2, column=1)

executeButton = Button(root, text="Execute")
executeButton.grid(row=2, column=2)

logLabel = Label(root, text="Log :")
logLabel.grid(row=3, column=1, sticky=W)

logText = Text(root, bg="red")
logText.grid(row=4, column=1, columnspan=4 )
logText.insert(END, "il vaut mieux avoir affaire a dieu qua ses saints")

#mouseclick event
canvas.bind("<Button 1>",printcoords)

root.mainloop()