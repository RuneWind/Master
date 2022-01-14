from gwf import Workflow
import pandas as pd

gwf = Workflow()

def train(optimizer, i):
    inputs = []
    outputs = []
    options = {"memory": "16g",
                "walltime": "12:00:00",
                "account": "speciale_YOLOv5",
                "gres": "gpu:1"}
    
    spec = """
    conda activate yolo
    python yolov5/train.py --img 640 --batch 20 --epochs 200 --data ./yolov5/YOLOv5-Master-1/data.yaml --cfg ./yolov5/models/yolov5s.yaml --weights '' --name YOLOv5s_{i}_results --nosave{optim}""".format(i = i, optim=" --adam" if optimizer == "adam" else "")

    return inputs, outputs, options, spec

#############################################################################################
hyparam = pd.read_csv("hyperparameters.csv", sep=";")

for i in range(len(hyparam)):
    f = open("yolov5/data/hyps/hyp.scratch.yaml", "r")
    list_of_lines = f.readlines()
    list_of_lines[5] = "lr0: {lr}".format(lr=hyparam["learning_rate"][i])
    list_of_lines[8] = "weight_decay: {wd}".format(wd=hyparam["weight_decay"][i])
    f.close()
    f = open("yolov5/data/hyps/hyp.scratch.yaml", "w")
    f.writelines(list_of_lines)
    f.close()

    gwf.target_from_template("YOLOv5s_" + str(i).zfill(2), train(hyparam["optimizer"][i], i))