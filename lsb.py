#!./env/bin/python3
import argparse
import lsb_text as lsb
import os
from argparse import RawTextHelpFormatter

__name__ = "__main__"
usageExample = """
Examples about how to use this module:\n

python lsb.py hide -f FILENAME -t TEXT
It hide TEXT inside the a NEW_FILENAME file

python lsb.py unhide -f FILENAME
It unhide data from FILENAME file to a secret.txt file

python lsb.py unhide -f FILENAME -s 120
It unhide only the first 120 bits from FILENAME file to a secret.txt file

"""

parser = argparse.ArgumentParser(description="Tool to hide and unhide data from a png image.", epilog=f"{usageExample}",
                                 formatter_class=RawTextHelpFormatter)
parser.add_argument("action", default=1, type=str,
                    help="hide or unhide. It is used to select if you hide or unhide a text into an image")
parser.add_argument("-f", "--file", type=str, help="path to the png image we are working on")
parser.add_argument("-t", "--text", type=str, help="text which will be hid in the image")
parser.add_argument("-s", "--size", type=int, help="print the size in bits of the data hid")

args = parser.parse_args()

if args.action == "hide":
    if os.path.isfile(args.file) == False:
        print(f"This image {args.file} doesn't exist")
    elif args.text == None:
        print("you should hide a text")
    else:
        lsb.hideText(args.file, args.text)
elif args.action == "unhide":
    if os.path.isfile(args.file) == False:
        print(f"This image {args.file} doesn't exist")
    else:
        if args.size != None and args.size > 0:
            lsb.unhideText(args.file, args.size)
        elif args.size == None:
            lsb.unhideText(args.file)
        else:
            print(f"selected size {args.size} isn't correct")

# text = "BBB"

# lsb.hideText("landscape.png",text)
# print(f"base : {}")
# lsb.unhideText("new_landscape.png")
