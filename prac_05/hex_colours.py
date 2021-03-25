"""
Create a program that allows you to look up hexadecimal colour codes.
"""

COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "cyan1": "#00ffff",
                "DarkGoldenrod3": "#cd950c", "aquamarine1": "#7fffd4", "DeepPink1": "#ff1493", "gold1": "#ffd700",
                "gray": "#bebebe", "pale": "#db7093"}


colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\": {}".format(colour_name, COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")
