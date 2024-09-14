import os
 
files = os.listdir("clutter")
i=1
for file in files:
    if file.endswith(".jpg"):
       print(file)
       os.rename(f"clutter/{file}",f"clutter/{i}.jpg")
       i=i+1