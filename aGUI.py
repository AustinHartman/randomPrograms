import tkinter
window = tkinter.Tk()
window.title("Boring GUI")
window.geometry("480x480")
button1 = tkinter.Button(window, text="Button 1")
button2 = tkinter.Button(window, text="Button 2")
button1.pack()
button2.pack()
window.mainloop()

