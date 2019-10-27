# steganotool

The aims of this tool is to hide and unhide text from a png image.

```positional arguments:
  action                hide or unhide. It is used to select if you hide or unhide a text into an image

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  path to the png image we are working on
  -t TEXT, --text TEXT  text which will be hid in the image
  -s SIZE, --size SIZE  print the size in bits of the data hid

Examples about how to use this module:

python lsb.py hide -f FILENAME -t TEXT
It hide TEXT inside the a NEW_FILENAME file

python lsb.py unhide -f FILENAME
It unhide data from FILENAME file to a secret.txt file

python lsb.py unhide -f FILENAME -s 120
It unhide only the first 120 bits from FILENAME file to a secret.txt file
```

![Base image](landscape.png)
```bash
python lsb.py hide -f landscape.png -t "Nobody can't find me if nobody know I'm using lsb method"
```
![Modified image](new_landscape.png)

```bash
python lsb.py unhide -f new_landscape.png -s 448
```

```
result : secret.txt
Nobody can't find me if nobody know I'm using lsb method
```