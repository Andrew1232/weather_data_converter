import os


path=os.path.dirname(__file__)+"\\rez4_6"
pathrez=os.path.dirname(__file__)+"\\rez5"
files=os.listdir(path)




filerez=open(pathrez+"\\1980-2021gada_laikapstakli.csv","w")


for x in files:# katram gadam
    print(x)
    file=open(path+"\\"+x)
    for y in file:#katrai dienai
        rinda=y.rstrip()
        filerez.write(rinda)
        filerez.write("\n")
    file.close()
filerez.close()