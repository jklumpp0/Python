from PIL import Image, ImageFile
import sys
import traceback
import string
import rawpy

class Cr2ImageFile(ImageFile.ImageFile):
    format = "CR2"
    format_description = "Canon RAW Image"

    def _open(self):
        try:
            img = rawpy.imread(self.fp)
            self.mode = "RGB"
            self.size = (img.sizes.width, img.sizes.height)
        except:
            raise (SyntaxError, "Cannot process file.")

Image.register_open("CR2", Cr2ImageFile)
Image.register_extension("CR2", ".CR2")
Image.register_extension("CR2", ".cr2")

if __name__ == "__main__":
    img = Image.open('tst.cr2')
    print(img.size)
