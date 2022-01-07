import os

iepr_diena=[]
file=open(os.path.dirname(__file__)+"\\rez6_5\\1980-2021gada_laikapstakli.csv","r")
lin=file.readline().rstrip().split(",")
for x in lin:
    iepr_diena.append('')



file=open(os.path.dirname(__file__)+"\\rez6_5\\1980-2021gada_laikapstakli.csv","r")
filerez=open(os.path.dirname(__file__)+"\\rez7\\1980-2021gada_laikapstakli.csv","w")

counter=0
for x in file:#katrai dienai
    print(counter)
    counter+=1
    line=x.rstrip().split(",")
    for (index,item) in enumerate(line):
        try:
            float(item)
        except:
            line[index]=iepr_diena[index]
    filerez.write(str(line).replace("', '",",")[2:-2]+"\n")
    iepr_diena=line

file.close()
filerez.close()