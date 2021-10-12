import os
import cv2 as cv
import shutil

def resize(path, resize_factor):
    imgs = os.listdir(path)

    # Try deleting existing folder and creating new empty one
    try:
        shutil.rmtree(path + "resize_" + str(resize_factor))
    except:
        print(path + "resize_" + str(resize_factor) + " directory does not exist")
    os.mkdir(path + "resize_" + str(resize_factor))

    print("Resizing images from: ", path)
    for im in imgs:
        if im.startswith(".DS") or im.startswith("resize"):
            continue
        img = cv.imread(path + im)
        dim = (int(img.shape[1] * resize_factor), int(img.shape[0] * resize_factor))
        resized = cv.resize(img, dsize=dim, interpolation=cv.INTER_AREA)
        cv.imwrite(path + "resize_" + str(resize_factor) + "/resized_" + im, resized)
    
resize("positives/", 0.2)
