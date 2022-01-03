import os

file=open(os.path.dirname(__file__)+"\\rez6\\1980-2021gada_laikapstakli.csv","r")

filerez=open(os.path.dirname(__file__)+"\\rez6_5\\1980-2021gada_laikapstakli.csv","w")

count=0
tuksums=[]
for x in file: #katrai dienai
    # print(count)
    count+=1
    line=x.rstrip().split(",")
    counter=0
    for y in line:
        if y=='':
            counter+=1
    tuksums.append(counter)
    if counter<61121:
        rinda=x.rstrip()
        filerez.write(rinda)
        filerez.write("\n")
    else:
        print("neav")
file.close()
filerez.close()
print(tuksums)



