import cv2 as cv
import os

color_imgs = os.listdir("object detection/negatives/colors")

for img_name in color_imgs:
    if img_name.startswith(".") or img_name == "grays":
        continue
    print("Converting", img_name, "to grayscale...")
    img = cv.imread("object detection/negatives/colors/" + img_name)
    # cv.imshow("Test", img)
    # cv.waitKey(0)
    # cv.destroyWindow("Test")
    # cv.waitKey(1)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    out_file = "object detection/negatives/grays/" + img_name
    cv.imwrite(out_file, img)
