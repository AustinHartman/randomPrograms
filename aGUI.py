from tkinter import *

#All the functions used in GUI
def decimalToBinary(x):
   if x > 1:
       decimalToBinary(x//2)
   print(x % 2, end = '')

window = Tk()
window.title("Boring GUI")
window.geometry("480x480")

header = Label(window, text="This might become a basic calculator!")

value = Entry(window)

try:
    i = int(value.get())
except ValueError:
    pass
if int(value.get()) >= 0:
    i = int(value.get())
else:
    i = 0

quadForm = Button(window, text="Quadratic Formula")

binConv = Button(window, text="Binary Converter", command=decimalToBinary(i))

quit = Button(window, text="Quit", command=window.quit)

header.pack(fill=BOTH, padx=3, pady=3)
value.pack()
quadForm.pack(fill=BOTH, padx=3, pady=3)
binConv.pack(fill=BOTH, padx=3, pady=3)
quit.pack(fill=BOTH, padx=3, pady=3)
window.mainloop()

