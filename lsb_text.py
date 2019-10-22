from PIL import Image
import binascii
import re


class LsbText:
    def __init__(self, imagePath: str, text: str, ):
        self.baseImage = Image.open(imagePath)
        self.imageName = imagePath.split("/")
        self.modifiedImageName = f"new_{self.imageName[-1]}"
        self.text = text
        self.bytesText = "".join(f"{ord(i):08b}" for i in self.text)
        print(f"binarytext {self.bytesText}")

    def hideText(self):
        if self.isDataTooLong(self.bytesText, self.baseImage) == True:
            print("your image is too small to hide this")
        else:
            self.baseImage.save(f"new_{self.imageName[-1]}", "PNG")
            newImage: Image.Image = Image.open(self.modifiedImageName)
            self.width = newImage.width
            self.height = newImage.height
            i = 0
            imagePixels = newImage.load()
            for x in range(self.width):
                for y in range(self.height):
                    tempPixel = list(imagePixels[x, y])
                    for k in range(0, 3):
                        if i < len(self.bytesText):

                            tempBits = bin(tempPixel[k])
                            newBits = tempBits[:-1] + self.bytesText[i]
                            tempPixel[k] = int(newBits, 2)
                            i = i + 1
                        else:
                            break
                    imagePixels[x, y] = tuple(tempPixel)
            newImage.save(self.modifiedImageName)

    def unhideText(self, imagePath: str):
        secret = ""
        image: Image.Image = Image.open(imagePath)
        imageValues = image.load()
        width, height = image.size
        for x in range(width):
            for y in range(height):
                tempPixel = list(imageValues[x, y])
                for k in range(0, 3):
                    tempBits = bin(tempPixel[k])
                    secret = secret + tempBits[-1]
        secret = self.decode_binary_string(secret)
        f = open("secret.txt", "w+")
        f.write(secret)

    def decode_binary_string(self, string):
        return ''.join(chr(int(string[i * 8:i * 8 + 8], 2)) for i in range(len(string) // 8))

    def showImage(self, image: Image.Image):
        image.show()

    def isImageSizeEnought(self):
        pass

    def isDataTooLong(self, binaryText: str, image: Image.Image):
        if (image.width * image.height * 3 < len(binaryText)):
            return True
        else:
            return False
