# -*- coding: utf-8 -*-
"""
Created on Wed May 17 21:02:25 2017

@author: wilkenshuang
"""

import os,cv2,random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
#import seaborn as sns

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.layers import Input, Dropout,Flatten,Convolution2D,MaxPool2D,Dense,Activation
from keras.optimizers import RMSprop
from keras.callbacks import ModelCheckpoint,Callback,EarlyStopping
from keras.utils import np_utils

Train_dir='data/train/'
Test_dir='data/test/'

rows=128
cols=128
channel=3

train_images=[Train_dir+i for i in os.listdir(Train_dir)]
train_dogs=[Train_dir+i for i in os.listdir(Train_dir) if 'dog' in i]
train_cats=[Train_dir+i for i in os.listdir(Train_dir) if 'cat' in i]
test_images=[Test_dir+i for i in os.listdir(Test_dir)]

train_images=random.sample(train_dogs,2000)+random.sample(train_cats,2000)
test_images=random.sample(test_images,500)

