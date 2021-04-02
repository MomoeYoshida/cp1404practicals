"""
Create a program that allows you to look up hexadecimal colour codes.
"""

# Don't worry about matching the case
COLOUR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb", "cyan1": "#00ffff",
                "darkgoldenrod3": "#cd950c", "aquamarine1": "#7fffd4", "deeppink1": "#ff1493", "gold1": "#ffd700",
                "gray": "#bebebe", "pale": "#db7093"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print("The code for \"{}\": {}".format(colour_name, COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ").lower()
