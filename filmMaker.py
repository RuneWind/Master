import cv2 as cv
import os
import glob
import pandas as pd


### FUNCTION DEFINITION
def pictures_to_video(pic_dir, bounding_box_df, pic_file_extension, fps):
    print("\n\033[1m\033[92m #### Convert images to video ####\033[0m\n")
    print("Loading files from: ", pic_dir)
    
    pic_list = sorted(glob.glob(pic_dir + "/*" + pic_file_extension))
    img_list = []
    for j in range(len(pic_list)):
        top_left = (bounding_box_df.loc[:, "x"][j], bounding_box_df.loc[:, "y"][j])
        buttom_right = (top_left[0] + bounding_box_df.loc[:, "width"][j], top_left[1] + bounding_box_df.loc[:, "height"][j])
        img = cv.imread(pic_list[j])
        
        if top_left == (0, 0):
            cv.putText(img, "NO WEIGHER", (20, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv.LINE_AA)
        else:
            img = cv.putText(img, "WEIGHER", (top_left[0], top_left[1]-8), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv.LINE_AA)
            img = cv.rectangle(img, top_left, buttom_right, (0, 0, 255), 2)
        
        height, width, layers = img.shape
        size = (width, height)
        img_list.append(img)
    

    video_name = pic_dir.split("/")[-2] + "_" + pic_dir.split("/")[-1] + ".avi"
    fourcc = cv.VideoWriter_fourcc(*"DIVX")
    out = cv.VideoWriter(video_name, fourcc, fps, size)


    for i in range(len(img_list)):
        out.write(img_list[i])
        print("Writing image ", i+1, " of ", len(img_list), end="")
        print("\r", end="")
    out.release()
    print("\nVideo saved as: ", video_name)



### FUNCTION CALL
picture_folder = "/Volumes/Data/data/raw/firefly/camera-images/0a-92-5e-29-ec-a2/2020-01-09"
bb_df = pd.read_csv("bounding_box_data.csv")
pictures_to_video(pic_dir=picture_folder, bounding_box_df=bb_df, pic_file_extension=".png", fps=12)