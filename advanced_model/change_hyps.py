import sys

f = open("yolov5/data/hyps/hyp.scratch.yaml", "r")
list_of_lines = f.readlines()
list_of_lines[5] = "lr0: {lr}\n".format(lr=sys.argv[1])
list_of_lines[8] = "weight_decay: {wd}\n".format(wd=sys.argv[2])
f.close()
f = open("yolov5/data/hyps/hyp.scratch.yaml", "w")
f.writelines(list_of_lines)
f.close()