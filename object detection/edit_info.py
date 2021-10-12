import math
resize_factor = 0.2

f = open("info.dat", "r")

content = f.readlines()
f.close()

w = open("info.dat", "w")
for line in content:
    line = line.split("\t")
    for i in range(2, len(line)):
        line[i] = str(math.ceil(int(line[i]) * resize_factor))
    line = "\t".join(line)
    w.write(line + "\n")

w.close()
    
