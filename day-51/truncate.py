with open('sample.txt','w') as f:
    f.write('hellow world!:')
    f.truncate(5)
    with open('sample.txt','r') as f:
        print(f.read())

