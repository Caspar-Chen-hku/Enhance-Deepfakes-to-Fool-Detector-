import os
import copy
import numpy as np
import shutil
import random

TRAIN_DIR = "data/train"
VAL_DIR = 'data/test'

SRC_DIR = 'fewshot_face_translation_GAN/newly_generated'
REAL_SRC = "img_align_celeba"

VAL_REAL = os.path.join(VAL_DIR, "real")
VAL_FAKE = os.path.join(VAL_DIR, "fake")
TRAIN_REAL = os.path.join(TRAIN_DIR, "real")
TRAIN_FAKE = os.path.join(TRAIN_DIR, "fake")

num = 0
for file in os.listdir(SRC_DIR):
    real = file.split('.')[0].split('_')[0]+'.jpg'
    i = random.randint(0,8)
    if i == 0:
        shutil.copy(os.path.join(SRC_DIR, file), VAL_FAKE)
        shutil.copy(os.path.join(REAL_SRC, real), VAL_REAL)
    else:
        shutil.copy(os.path.join(SRC_DIR, file), TRAIN_FAKE)
        shutil.copy(os.path.join(REAL_SRC, real), TRAIN_REAL)
    num+=1
    if num%100 == 0:
        print("copied %d images", num)
print("completed copying")

