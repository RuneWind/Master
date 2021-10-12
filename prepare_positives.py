import pandas as pd
from shutil import copyfile
import cv2 as cv
import os


bb_data = pd.read_csv("bounding_box_data.csv")
os.remove("object detection/info.dat")
f = open("object detection/info.dat", "a+")

pic_count = 0
for i in range(0, len(bb_data), 5):
    # Stop when 120 images are approved
    if pic_count >= 200:
        break

    x = bb_data.loc[:, "x"][i]
    y = bb_data.loc[:, "y"][i]-4
    w = bb_data.loc[:, "width"][i]+6
    h = bb_data.loc[:, "height"][i]+6

    date = bb_data.loc[:, "timestamp"][i].split("T")[0]
    date = "-".join((str(date[:4]), str(date[4:6]), str(date[6:])))

    # Show image and determine if the weigher is visible
    img = cv.imread("/Volumes/Data/data/raw/firefly/camera-images/0a-92-5e-29-ec-a2/" + date + "/" + bb_data.loc[:, "timestamp"][i] + "_infrared_image.png")
    img = cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 1)
    cv.imshow("box check", img)
    
    k = cv.waitKey(0)
    cv.destroyWindow("box check")
    cv.waitKey(1)

    # Break loop if key pressed is "q"
    if k == ord("q"):
        break
    
    # If key pressed is not "s", continue to next picture
    if k != ord("s"):
        continue
    
    else:
        pic_count += 1
        # Write information about positive images to info.dat file
        f.write("positives/" + bb_data.loc[:, "timestamp"][i] + "_infrared_image.png")
        f.write("\t1\t" + str(x) + "\t" + str(y) + "\t" + str(w) + "\t" + str(h) + "\n")

        # Copy file from external hard drive to positives folder
        copyfile("/Volumes/Data/data/raw/firefly/camera-images/0a-92-5e-29-ec-a2/" + date + "/" + bb_data.loc[:, "timestamp"][i] + "_infrared_image.png",
            "object detection/positives/" + bb_data.loc[:, "timestamp"][i] + "_infrared_image.png")
        print("Saved ", pic_count, " pictures")

f.close()