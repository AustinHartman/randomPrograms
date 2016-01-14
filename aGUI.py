from tkinter import *
def decimalToBinary(x):

   if x > 1:
       decimalToBinary(x//2)
   print(x % 2, end = '')

#number = int(input("What is your number?\n"))
window = Tk()
window.title("Boring GUI")
window.geometry("480x480")
header = Label(window, text="This might become a basic calculator!")
quadForm = Button(window, text="Quadratic Formula")
binConv = Button(window, text="Binary Converter")
quit = Button(window, text="Quit", command=window.quit)
header.pack()
quadForm.pack()
binConv.pack()
quit.pack()
window.mainloop()

