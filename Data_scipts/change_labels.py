import os
from pathlib import Path
from PIL import Image
import shutil
import random
import xml.etree.ElementTree as ET
import cv2

def convert_xml_to_yolo(xml_file, img_width, img_height, class_mapping):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    yolo_lines = []

    for obj in root.findall('object'):
        class_name = obj.find('name').text
        if class_name in class_mapping:
            class_idx = class_mapping[class_name]
            bbox = obj.find('bndbox')
            x_min = float(bbox.find('xmin').text)
            y_min = float(bbox.find('ymin').text) 
            x_max = float(bbox.find('xmax').text) 
            y_max = float(bbox.find('ymax').text) 
                                                                    
            x_center = (x_min + x_max) / (2.0 * img_width)
            y_center = (y_min + y_max) / (2.0 * img_height)
            width = (x_max - x_min) / img_width
            height = (y_max - y_min) / img_height
            
            '''
            # Calculate YOLO coordinates (normalized)
            x_center = x_center / img_width
            y_center = y_center / img_height
            width = width / img_width
            height = height / img_height 
            '''

            yolo_line = f"{class_idx} {x_center} {y_center} {width} {height}\n"
            yolo_lines.append(yolo_line)

    return yolo_lines


# Class mapping (replace with your class mapping)
class_mapping = {
    'A1' : 0, 'A2' : 1, 'A3' : 2, 'A4' : 3, 'A5' : 4, 'A6' : 5, 'A7' : 6,
    'A8' : 7, 'A9' : 8, 'A10' : 9, 'A11' : 10, 'A12' : 11, 'A13' : 12,
    'A14' : 13, 'A15' : 14, 'A16' : 15, 'A17' : 16, 'A18' : 17, 'A19' : 18
}

if __name__ == '__main__':
    data_dir =  Path(r'/Users/work/Data/Planes')
    xml_dir = data_dir / 'Annotations' / 'Horizontal Bounding Boxes' 
    # Iterate through XML files in the directory
    for xml_filename in os.listdir(xml_dir):
        if xml_filename.endswith('.xml'):
            xml_path = os.path.join(xml_dir, xml_filename)
            xml_name = xml_filename.replace('.xml', '') 

            if os.path.exists(data_dir / 'Test' /  f'{xml_name}.jpg'):
                image = cv2.imread(str(data_dir / 'Test' / f'{xml_name}.jpg'))
                img_height, img_width, _ = image.shape
                output_dir = data_dir / 'Test'

            else:
                image = cv2.imread(str(data_dir / 'Train' / f'{xml_name}.jpg'))
                img_height, img_width, _ = image.shape
                output_dir = data_dir / 'Train'

            yolo_lines = convert_xml_to_yolo(xml_path, img_width, 
                                            img_height, class_mapping
                                            )

            # Create a corresponding YOLO format file
            yolo_filename = os.path.splitext(xml_filename)[0] + '.txt'
            yolo_path = os.path.join(output_dir, yolo_filename)

            # Save the YOLO annotation lines to the output file
            with open(yolo_path, 'w') as yolo_file:
                yolo_file.writelines(yolo_lines)
