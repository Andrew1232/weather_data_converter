import os


path=os.path.dirname(__file__)+"\\rez6_5"
files=os.listdir(path)



file=open(path+"\\"+files[0])
line=file.readline()
file.close()
line=line.split(",")
garums=len(line)


summa=[]
for x in line:
    summa.append(0)


counter=0
for x in files:# katram gadam
    print(x)
    file=open(path+"\\"+x)
    for r in file:  #katrai dienai
        print(counter)
        counter+=1
        line=r.rstrip().split(",")
        for y in range(garums):  #katram mērījumam (y ir mērījuma indekss)
            try:
                
                summa[y]+=float(line[y])
            except:
                continue


    file.close()

vidējais=[]
for x in summa:
    vidējais.append(x/counter)
    




# print(counter)
file2=open(os.path.dirname(__file__)+"\\vidējais.txt","w")
file2.write(str(vidējais)[1:-1])
file2.close()


