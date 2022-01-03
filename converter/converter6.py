import os


path=os.path.dirname(__file__)+"\\rez5"
pathrez=os.path.dirname(__file__)+"\\rez6"
files=os.listdir(path)




filerez=open(pathrez+"\\1980-2021gada_laikapstakli.csv","w")

counter=0
for x in files:# katram gadam
    file=open(path+"\\"+x)
    if counter==0:
        rinda1=file.readline().rstrip() 
        counter+=1
    for y in file:#katrai dienai
        
        rinda2=y.rstrip()
        filerez.write(rinda1+","+rinda2)
        filerez.write("\n")
        rinda1=rinda2
    file.close()
filerez.close()

    




