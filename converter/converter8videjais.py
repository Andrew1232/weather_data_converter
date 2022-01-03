import os

file=open("vidējais.txt","r")
rinda=file.read()
videjie=rinda.rstrip().split(", ")
file.close()


file=open(os.path.dirname(__file__)+"\\rez7\\1980-2021gada_laikapstakli.csv","r")
filerez=open(os.path.dirname(__file__)+"\\rez8\\1980-2021gada_laikapstakli.csv","w")

counter=0
for x in file:#katrai dienai
    print(counter)
    counter+=1
    line=x.rstrip().split(",")
    for (index,item) in enumerate(line):
        try:
            float(item)
        except:
            line[index]=videjie[index]
    filerez.write(str(line).replace("', '",",")[2:-2]+"\n")



file.close()
filerez.close()