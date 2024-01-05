import os
from pathlib import Path
from PIL import Image
import shutil
import random
import xml.etree.ElementTree as ET
import cv2

if __name__ == '__main__':
    data = Path('/Users/work/Data/Planes/') 
    split =  data  / 'ImageSets' / 'Main' / 'train.txt'
    img_source = data / 'JPEGImages'
    destination = data  / 'Train'
    
    os.mkdir(destination = data  / 'Train')
    with open(split, 'r') as file:
        for i in file:
            img =  img_source   /  (i.replace('\n', '') + '.jpg')
            shutil.move(img, destination)

    split =  data  / 'ImageSets' / 'Main' / 'test.txt'
    destination = data / 'Test'

    os.mkdir(destination)
    with open(split, 'r') as file:
        for i in file:
            img =  img_source /   (i.replace('\n', '') + '.jpg')
            shutil.move(img, destination)
