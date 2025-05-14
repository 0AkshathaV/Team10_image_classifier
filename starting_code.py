#AI Image Classifier

import os
import numpy as np
import matplotlib.pyplot as plt

 from tensorflow.keras.models
from tensorflow.keras.models

import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.callbacks
import ModelCheckpoint, Early Stopping
from sklearn.metrics
import classification_report,confusion_matrix

IMG_SIZE = (128, 128)
BATCH_SIZE = 32
EPOCHS = 20
TRAIN_DIR = 'data/train'
VAL_DIR = 'data/val'
TEST_DIR = 'data/test'
MODEL_PATH = 'model.h5'

