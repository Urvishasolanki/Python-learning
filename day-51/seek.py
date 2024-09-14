with open('file1.txt','r') as f:
    print(type(f))
    f.seek(10)
    #move to the 10th byte in the file
    data=f.read(5)
    print(data)
