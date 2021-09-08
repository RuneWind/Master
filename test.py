import pandas as pd
import os
import cv2 as cv

pic_dir = "/Volumes/Data/data/raw/firefly/camera-images/0a-92-5e-29-ec-a2/2019-12-25"
images = os.listdir(pic_dir)
img = cv.imread(pic_dir + "/" + images[0])
print(img.shape)