#!/usr/bin/env python
import os
import sys
from PIL import Image
from db import DBImage, Database

def get_image(file):
    try:
        img = Image.open(file)
        width, height = img.size
        return DBImage(file, os.path.basename(file), width, height)
    except:
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
