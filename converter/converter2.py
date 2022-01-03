import os
path=os.path.dirname(__file__)+"\\rez"
pathrez=os.path.dirname(__file__)+"\\rez2"
files=os.listdir(path)



for y in files:
    print(y)
    file=open(path+"\\"+y,"r")
    filex=open(pathrez+"\\"+y,"w")
    for x in file: 
        x=x.rstrip().replace(" ","")
        x.replace("''","")
        filex.write(x)
        filex.write("\n")
    file.close()
    filex.close()