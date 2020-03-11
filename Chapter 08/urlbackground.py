import turtle
import urllib.request
import os


dowloaded = False

def mouseclick(x, y):
    global downloaded
    if not dowloaded:  # Download image only if not yet downloaded
        # Web URL for the image
        source = "http://tecfa.unige.ch/guides/utils/example.gif"
        # Retrieve the image and store in a file named smileyface.gif
        urllib.request.urlretrieve(source, "smileyface.gif")
        # Set background image
        turtle.bgpic("smileyface.gif")
        # Delete the dowloaded image file
        os.remove("smileyface.gif")  
        # Note that we already downloaded the image so we do not 
        # attempt to download it again
        downloaded = True


# Turn off animation
turtle.tracer(0)
turtle.hideturtle()
# Register the mouseclick function callback
turtle.onscreenclick(mouseclick)
# Enter the graphical framework event processing loop
turtle.mainloop()
