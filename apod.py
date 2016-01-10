import webbrowser
def apodImage():
    print("Date must be in this form: 160106 for January 6, 2016\n")
    date = input("Enter a date:")
    link = "http://apod.nasa.gov/apod/ap" + date + ".html"
    webbrowser.open(link)
apodImage()