import torch
import os
import shutil
from ultralytics import YOLO
import time
import dingpy


import time



sound_file = '/Users/work/Documents/oven.mp3'

start_time = time.time()

model = YOLO('yolov8n.pt') # Nano model
# Training on mac book
model.to('mps')
model.train(data='config.yaml', epochs=5, device='mps')

end_time = time.time()

# Calculate the elapsed time
print()
print('Time:', (end_time - start_time) /  3600 ) 


dingpy.ding(path = '/Users/work/Documents/oven.mp3' )
