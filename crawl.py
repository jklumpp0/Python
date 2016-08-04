#!/usr/bin/env python
import os
import sys
from PIL import Image
from db import DBImage, Database
import datetime

def ctime_to_datetime(ctime):
    return datetime.datetime.strptime(ctime, "%a %b %d %H:%M:%S %Y")

def get_exif_time(img):
    try:
        return img._getexif()[36867]
    except:
        return "1970:01:01 00:00:01"

def get_image(file):
    try:
        img = Image.open(file)
        width, height = img.size
        #print(img._getexif())
        ctime = datetime.datetime.fromtimestamp(os.path.getctime(file))
        exif_time = datetime.datetime.strptime(get_exif_time(img), "%Y:%m:%d %H:%M:%S")
        return DBImage(file, os.path.basename(file), width, height, ctime, exif_time)
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
