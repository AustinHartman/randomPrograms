import webbrowser
def domSearch():
    print("It needs to be a .com")
    site = input("What website should be opened?\n")
    newSite = site.replace(" ", "")
    link = "https://www." + newSite + ".com"
    webbrowser.open(link)

domSearch()