import os
from pathlib import Path
from PIL import Image
import shutil
import random
import xml.etree.ElementTree as ET
import cv2

if __name__ == '__main__':


    data = Path('/Users/work/Data/Planes/archive') 
    split =  str(data) + r'/ImageSets/Main/train.txt'
    xml_source = str(data) +r'/Users/work/Data/Planes/archive/Lables'
    destination = str(data) + r'/Users/work/Data/Planes/archive/Train'

    with open(split, 'r') as f:
        for i in f:
            print(xml_source + r'/' +  i.replace('\n', '') + '.jpg')
            img =  xml_source + r'/' +  i.replace('\n', '') + '.txt'
            shutil.move(img, destination)

    split = str(data) + r'/Users/work/Data/Planes/archive/ImageSets/Main/test.txt'
    destination = str(data) + r'/Users/work/Data/Planes/archive/Test'

    with open(split, 'r') as f:
        for i in f:
            print(xml_source + r'/' +  i.replace('\n', '') + '.jpg')
            img =  xml_source + r'/' +  i.replace('\n', '') + '.txt'
            shutil.move(img, destination)
