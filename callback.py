from tkinter import *
import webbrowser
import math
import decimal

master = Tk()
master.title("Random Calculator")
master.maxsize(height=480, width=1080)
entryBox = Entry(master)
entryBox2 = Entry(master)
entryBox3 = Entry(master)

fib_nums = StringVar()
sphere_vol = StringVar()
sphere_surface_area = StringVar()


def sphere_volume():
    height = float(entryBox.get())
    radius = float(entryBox2.get())
    volume = math.pi * radius * height
    a = decimal.Decimal(volume)
    sphere_vol.set('The volume is: ' + str(round(a, 2)))


def sphere_sa():
    height = float(entryBox.get())
    radius = float(entryBox2.get())
    circ = math.pi * 2.0 * radius
    sa = (circ*height) + (math.pi * radius*radius * 2)
    a = decimal.Decimal(sa)
    sphere_surface_area.set('Surface area is: ' + str(round(a, 2)))

def fibonacci_sequence():
    limit = int(entryBox.get())
    sequence_list = [0]
    while len(sequence_list) < limit:
        if limit == 1:
            break
        elif len(sequence_list) == 1:
            sequence_list.append(1)
        else:
            sequence_list.append(sequence_list[-1] + sequence_list[-2])
    fib_nums.set('Here are ' + str(limit) + ' digits of Fibonacci: ' + str(sequence_list))


def domain_search():
    site = entryBox.get()
    newSite = site.replace(" ", "")
    link = "https://www." + newSite + ".com"
    webbrowser.open(link)

Label(master, text='A').grid(row=1)
entryBox.grid(row=1, column=1)
Label(master, text='B').grid(row=2)
entryBox2.grid(row=2, column=1)
Label(master, text='C').grid(row=3)
entryBox3.grid(row=3, column=1)

Button(master, text="Fib Nums: A=Number of nums", command=fibonacci_sequence).grid(row=4, column=1)
Label(master, textvariable=fib_nums).grid(row=4, column=2)
Button(master, text="Sphere Volume: A=height B=radius", command=sphere_volume).grid(row=5, column=1)
Label(master, textvariable=sphere_vol).grid(row=5, column=2)
Button(master, text="Sphere SA: A=height B=radius", command=sphere_sa).grid(row=6, column=1)
Label(master, textvariable=sphere_surface_area).grid(row=6, column=2)
Button(master, text="Open Site Entered", command=domain_search).grid(row=7, column=1)
Button(master, text="Quit", command=master.quit).grid(row=8, column=1)
mainloop()