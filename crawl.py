#!/usr/bin/env python
import os
import sys
import exifread
from PIL import Image
from db import DBImage, Database
import datetime
import Cr2ImagePlugin

NO_MODEL = "NO_CAMERA"
class Exif(object):
    def __init__(self, filepath):
        with open(filepath, 'rb') as fd:
            self.exif = exifread.process_file(fd)

    @property
    def camera_model(self):
        try:
            return self.exif['Image Model'].printable
        except:
            return NO_MODEL

    @property
    def exif_time(self):
        try:
            return self.exif['EXIF DateTimeOriginal'].printable
        except:
            return "1970:01:01 00:00:01"

def get_image(file):
    try:
        img = Image.open(file)
        width, height = img.size
        ctime = datetime.datetime.fromtimestamp(os.path.getctime(file))
        exif = Exif(file)
        exif_time = datetime.datetime.strptime(exif.exif_time, "%Y:%m:%d %H:%M:%S")
        model = exif.camera_model
        return DBImage(file, os.path.basename(file), model, width, height, ctime, exif_time)
    except:
        print(sys.exc_info())
        return None

def crawl(folder = os.curdir): 
    db = Database()

    for root, dirs, files in os.walk(folder): 
        abs_files = [os.path.join(root, file) for file in files]
        img_files = [get_image(file) for file in abs_files]
 
        for image in filter(None, img_files):
            db.add(image)

if __name__ == '__main__':
    crawl(sys.argv[1])
