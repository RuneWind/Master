from gwf import Workflow
import pandas as pd

gwf = Workflow()

def test(i):
    inputs = ["/home/runewind/speciale_YOLOv5/yolov5/yolov5/runs/train/YOLOv5s_{i}_results/weights/last.pt".format(i=str(i).zfill(2))]
    outputs = ["/home/runewind/speciale_YOLOv5/yolov5/yolov5/runs/detect/exp/YOLOv5s_{i}_".format(i=str(i).zfill(2))]
    options = {"cores": "1",
                "memory": "8g",
                "walltime": "12:00:00",
                "account": "speciale_YOLOv5"}
    
    spec = """
    source /home/runewind/miniconda3/etc/profile.d/conda.sh
    conda activate yolo
    python detect --weights yolov5/runs/train/YOLOv5s_{i}_results/weights/last.pt --img 640 conf 0.5 --source /home/runewind/speciale_YOLOv5/yolov5/yolov5/YOLOv5-Master-1/test/images""".format(i=str(i).zfill(2))

    return inputs, outputs, options, spec

for i in range(18):
    gwf.target_from_template("YOLOv5s_" + str(i).zfill(2) + "_test", test(i))