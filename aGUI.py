from tkinter import *

window = Tk()
window.title("Calc")
window.geometry("480x480")
value = Entry(window)


i = value.get()


def callback(i):
    if i != int():
        i = int(value.get())

def decimalToBinary(x):
    callback()
    if x > 1:
        decimalToBinary(x//2)
    print(x % 2, end = '')



header = Label(window, text="This might become a basic calculator!")

# update = Button(window, text="Update", command=callback)

button = Button(window, text="Binary Converter", command=decimalToBinary)

quit = Button(window, text="Quit", command=window.quit)

value.pack()
header.pack(fill=BOTH, padx=3, pady=3)
# update.pack(fill=BOTH, padx=3, pady=3)
button.pack(fill=BOTH, padx=3, pady=3)
quit.pack(fill=BOTH, padx=3, pady=3)
mainloop()

