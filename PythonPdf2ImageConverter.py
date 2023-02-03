# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI APPLICATION TO CONVERT PDF FILE INTO IMAGES USING THE PyMuPDF MODULE.

# ALL THE PDF PAGES WILL BE CONVERTED INTO IMAGES BUT ONLY THE LAST IMAGE WILL BE DISPLAYED IN THE GUI

# PyMuPDF is a Python binding for MuPDF – a lightweight PDF, XPS, and E-book viewer, renderer, and toolkit,
# which is maintained and developed by Artifex Software, Inc
# PyMuPDF can access files with extensions like “.pdf”, “.xps”, “.oxps”, “.cbz”, “.fb2”, “.mobi” or “.epub”.
# PyMuPDF provides access to many important functions of MuPDF from within a Python environment

# The module can be installed using the command - pip install PyMuPDF

# Importing necessary packages
import os
import fitz
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog

#  To get better resolution
zoom_x = 2.0  # horizontal zoom
zoom_y = 2.0  # vertical zoom
mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    root.previewlabel = Label(root, bg="tan4", fg="white", text="IMAGE PREVIEW (ONLY LAST PAGE IS DISPLAYED)",
                              font=('Comic Sans MS',20))
    root.previewlabel.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

    root.imageLabel = Label(root, bg="tan4", borderwidth=3, relief="groove")
    root.imageLabel.grid(row=2, column=1, padx=10, pady=10, columnspan=3)

    pdfFileLabel = Label(root, text="PDF FILE NAME : ", bg="tan4")
    pdfFileLabel.grid(row=3, column=1, padx=5, pady=10)

    root.openPDFEntry = Entry(root, width=35, textvariable=filePath)
    root.openPDFEntry.grid(row=3, column=2, padx=10, pady=10)

    root.openPDFButton = Button(root, width=10, text="BROWSE", command=pdfBrowse)
    root.openPDFButton.grid(row=3, column=3, padx=10, pady=10)

    root.captureBTN = Button(root, text="CONVERT", command=Convert, bg="LIGHTBLUE", font=('Comic Sans MS',15), width=20)
    root.captureBTN.grid(row=4, column=2, padx=10, pady=10)

    imageView = Image.open("<YOUR_DEFAULT_IMAGE_PATH>")
    imageResize = imageView.resize((640, 480), Image.ANTIALIAS)
    imageDisplay = ImageTk.PhotoImage(imageResize)
    root.imageLabel.config(image=imageDisplay)
    root.imageLabel.photo = imageDisplay

# Defining pdfBrowse() to browse for the PDF file that is to be converted
def pdfBrowse():
    # Presenting user with a pop-up for directory selection. initialdir argument is optional
    # Retrieving the user-input destination directory and storing it in destinationDirectory
    # Setting the initialdir argument is optional. SET IT TO YOUR DIRECTORY PATH
    openDirectory = filedialog.askopenfilename(initialdir="YOUR DIRECTORY PATH")
    # Displaying the directory in the directory textbox
    filePath.set(openDirectory)

# Defining Covert() to convert PDF file and save the file as images and display the last saved image
def Convert():
    # Fetching and storing the name of the input pdf along with the path
    input_file_path_name = filePath.get()
    # Storing the destination path and name for images
    image_path = os.path.dirname(os.path.abspath(input_file_path_name))
    image_name = os.path.basename(input_file_path_name.split(".")[0])
    # Converting the pdf to image using the convert_from_path with the file name as argument
    pages = fitz.open(input_file_path_name)
    pages_count = len(pages)
    for page in range(len(pages)):
        # Render page to an image
        pix = pages[page].get_pixmap(matrix=mat)
        # Store image as a PNG
        pix.save(image_path + "/" + image_name + "-" + str(page) + ".png")
    # Opening the last saved image using the open() of Image class which takes image as argument
    saved_image = Image.open(image_path + "/" + image_name + "-" + str(pages_count-1)+".png")
    # Resizing the image for display purpose
    imageResize = saved_image.resize((640, 480), Image.LANCZOS)
    # Creating object of PhotoImage() class to display the frame
    saved_image = ImageTk.PhotoImage(imageResize)
    # Configuring the label to display the frame
    root.imageLabel.config(image=saved_image)
    # Keeping a reference
    root.imageLabel.photo = saved_image

# Creating object of tk class
root = tk.Tk()
# Setting the title, window size, background color
# and disabling the resizing property
root.title("PDF2IMAGE")
root.geometry("670x670")
root.resizable(False, False)
root.configure(background = "tan4")
# Creating tkinter variables
destPath = StringVar()
filePath = StringVar()
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
