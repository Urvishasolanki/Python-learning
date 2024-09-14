import os
folders=os.listdir("data")
print(folders)
print(os.getcwd())
os.chdir("/users")
for folder in folders:
    print(folder)
for folder in folders:
    print(os.listdir(f"{folder}"))