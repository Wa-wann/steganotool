from PIL import Image


def hideText(imagePath: str, text: str):
    baseImage = Image.open(imagePath)
    imageName = imagePath.split("/")
    modifiedImageName = f"new_{imageName[-1]}"
    text = text
    bytesText = "".join(f"{ord(i):08b}" for i in text)
    print(f"datalength : {len(bytesText)}")

    if isDataTooLong(bytesText, baseImage) == True:
        print("your image is too small to hide this")
    else:
        baseImage.save(f"new_{imageName[-1]}", "PNG")
        newImage: Image.Image = Image.open(modifiedImageName)
        width = newImage.width
        height = newImage.height
        i = 0
        imagePixels = newImage.load()
        for x in range(width):
            for y in range(height):
                tempPixel = list(imagePixels[x, y])
                for k in range(0, 3):
                    if i < len(bytesText):

                        tempBits = bin(tempPixel[k])
                        newBits = tempBits[:-1] + bytesText[i]
                        tempPixel[k] = int(newBits, 2)
                        i = i + 1
                    else:
                        break
                imagePixels[x, y] = tuple(tempPixel)
        newImage.save(modifiedImageName)


def unhideText(imagePath: str, bitsLenght: int = None):
    secret = ""
    image: Image.Image = Image.open(imagePath)
    imageValues = image.load()
    width, height = image.size

    if bitsLenght == None:
        for x in range(width):
            for y in range(height):
                tempPixel = list(imageValues[x, y])
                for k in range(0, 3):
                    tempBits = bin(tempPixel[k])
                    secret = secret + tempBits[-1]
    else:
        i = 0
        for x in range(width):
            for y in range(height):
                tempPixel = list(imageValues[x, y])
                for k in range(0, 3):
                    if i < bitsLenght:
                        tempBits = bin(tempPixel[k])
                        secret = secret + tempBits[-1]
                        i = i + 1

    secret = decode_binary_string(secret)
    f = open("secret.txt", "w+")
    f.write(secret)


def decode_binary_string(string):
    return ''.join(chr(int(string[i * 8:i * 8 + 8], 2)) for i in range(len(string) // 8))


def showImage(image: Image.Image):
    image.show()


def isDataTooLong(binaryText: str, image: Image.Image):
    if (image.width * image.height * 3 < len(binaryText)):
        return True
    else:
        return False
