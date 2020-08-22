"""
CP1404/CP5632 - Practical
hex_colours.py
"""
COLOUR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine": "#7fffd4", "azure": "f0ffff",
                "beige": "#f5f5dc", "bisque": "#ffe4c4", "black": "#000000", "blanchedalmond": "#ffebcd",
                "blue": "#0000ff", "burlywood": "#deb887"}

colour = input("Enter a colour name: ")

while colour != "":
    print("The code for {0} is {1}".format(colour, COLOUR_CODES.get(colour)))
    colour = input("Enter a colour name: ")
