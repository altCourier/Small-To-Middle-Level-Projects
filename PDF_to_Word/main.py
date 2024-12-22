# Importing modules and libraries
import os
from tkinter import *
from tkinter import filedialog, messagebox
import webbrowser
from pdf_to_word import *
from pdf2docx import Converter
import aspose.words as aw

# Initializing the window
root = Tk()
root.title("Converter")
root.geometry("1000x600")
root.resizable(False,False)
root.config(bg="light gray")

# Closing Box
close_image = PhotoImage(file="assets/close.png")
myClose_image = Label(root, image=close_image, bg="light gray")
myClose_image.place(x = 940, y = 20)
myClose_image.bind("<Button 1>", lambda event: exit())
myClose_image.bind("<Enter>", lambda event: myClose_image.config(cursor="hand2"))
myClose_image.bind("<Leave>", lambda event: myClose_image.config(cursor="arrow"))
myClose_image.bind("<Escape>", lambda event: exit())
myClose_image.focus_set()

# Title 
title = Label(root, text="PDF-Word & Word-PDF Conventer", font=("Palatino",24,"bold"), bg="#A9A9A9")
title.place(x=170, y=15)

# Headline
headline = Label(root, text="Choose suitable options for your needs", bg="light gray", font=("Times New Roman",16,"bold"))
headline.place(x=170, y=70)

# Logo
def openGit():
    webbrowser.open("https://github.com/altCourier")
logo = PhotoImage(file="assets/logo.png")
myLogo = Label(root, image=logo,bg ="light gray")
myLogo.bind("<Button 1>", lambda event: openGit())
myLogo.bind("<Enter>", lambda event: myLogo.config(cursor="hand2"))
myLogo.bind("<Leave>", lambda event: myLogo.config(cursor="arrow"))
myLogo.place(x=30,y=13)

# Arrow
def easterEgg():
    messagebox.showinfo(title="Easter Egg Found.", message= "Yurtta sulh cihanda sulh!")
arrow_image = PhotoImage(file="assets/arrow.png")
arrow = Label(root, image=arrow_image, bg="white")
arrow.place(x=480,y=260)
arrow.bind("<Button 1>", lambda event: easterEgg())

# Update Input Directory
def update_inputDir(dir):
    global newInput_dir
    newInput_dir = dir
    dirBox_input.config(text=dir)

# Update Output Directory
def update_outputDir(dir):
    global newOutput_dir
    newOutput_dir = dir
    dirBox_output.config(text=dir)

# PDF Box Input
pdf_image = PhotoImage(file="assets/pdf.png")
pdf_input = Label(root, image=pdf_image, bg = "white")
pdf_input.place(x=160, y=240)
pdf_input.bind("<Button 1>", lambda event: update_inputDir(choose_pdf_file()))

# Word Box Input
word_image = PhotoImage(file="assets/word.png")
word_input = Label(root,image=word_image, bg= "white")
word_input.place(x=320,y=240)
word_input.bind("<Button 1>", lambda event: update_inputDir(choose_doc_file()))

# Output Box
output_image = PhotoImage(file="assets/Output.png")
output = Label(root,image=output_image)
output.place(x=640,y=240)
output.bind("<Button 1>", lambda event: update_outputDir(outputDirectory()))

# Input Directory
dirBox_input = Label(root, text="No file selected", font=("Palantino",16,"bold"), bg="white", wraplength=260)
dirBox_input.place(x=160,y=380)

# Output Directory
dirBox_output = Label(root, text="No output directory selected", font=("Palantino",16,"bold"), bg="white", wraplength=260)
dirBox_output.place(x=640, y=380)

# Convert Button
convert_image = PhotoImage(file="assets/convert.png")
convert = Label(root, image=convert_image, bg="white")
convert.place(x=430,y=450)
convert.bind("<Button 1>", lambda event: process_conversion(newInput_dir,newOutput_dir))

# Main loop
root.mainloop()