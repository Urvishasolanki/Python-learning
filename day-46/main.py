import os
if(not os.path.exists("data")):
    os.mkdir("data")
# create data directari directories
for i in range(0,100):
    os.mkdir(f"day{i+1}")
    