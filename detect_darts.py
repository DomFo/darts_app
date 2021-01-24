#================================================================
#
#   File name   : detect_mnist.py
#   Author      : PyLessons
#   Created date: 2020-08-12
#   Website     : https://pylessons.com/
#   GitHub      : https://github.com/pythonlessons/TensorFlow-2.x-YOLOv3
#   Description : mnist object detection example
#
#================================================================
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import cv2
import numpy as np
import random
import time
import tensorflow as tf
from yolov3.yolov4 import Create_Yolo
from yolov3.utils import detect_image, detect_video, detect_realtime
from yolov3.configs import *

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.compat.v1.InteractiveSession(config=config)

video_path = os.path.join("darts", "videos")
videos = os.listdir(video_path)

for vid in videos:
    ID = random.randint(0, 5)
    label_txt = "darts/darts_test.txt"
    image_info = open(label_txt).readlines()[ID].split()
    image_path = os.path.join("darts", "darts_test", image_info[0])
    video_file = os.path.join(video_path, vid)

    yolo = Create_Yolo(input_size=YOLO_INPUT_SIZE, CLASSES=TRAIN_CLASSES)
    yolo.load_weights(f"./checkpoints/{TRAIN_MODEL_NAME}")  # use keras weights

    # detect_image(yolo, image_path, "darts_test.jpg", input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))
    detect_video(yolo, video_file, f'{video_file}_predicted.mp4', input_size=YOLO_INPUT_SIZE, CLASSES=TRAIN_CLASSES, show=False, rectangle_colors=(255, 0, 0))