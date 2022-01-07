import os
# path_station=os.path.dirname(__file__)+"\\data"
path=os.path.dirname(__file__)+"\\rez2"
pathrez=os.path.dirname(__file__)
files=os.listdir(path)


file=open(os.path.dirname(__file__)+"\\stationList.txt","r")
stationList=file.read()[2:-2].replace("'","").replace(" '","").split(", ")
file.close()


visasdienas=0
for x in files: #katram gadam
    gads=int(x[:-4])
    if gads%4==0:#nosaka gada dienu sarakstu 01-01,01-02 un sienu skaitu gadā      
        dienuSkaits=366
    else:
        dienuSkaits=365
    visasdienas=visasdienas+dienuSkaits
print("dienas")


saraksts=[]
for x in stationList:
    for y in range(18):  #cik daudz variables ir katrai stacijai
        saraksts.append(visasdienas)
print(len(saraksts))
# print("saraksts")

for x in files:      #for every year(visiem apstrādātajiem failiem)
    print(x)
    file=open(path+"\\"+x,"r")
    counter=0
    for y in file:    #for every line aka every recorded day
        print(counter)
        counter+=1
        y=y.strip()
        y=y.split(",")
        list_of_indexes = []
        item_to_find = ''
        for (index, item) in enumerate(y):#pārbauda vai ir '' un ja ir tad to pieskaita attiecīgajā vietā sarakstā
            if item != item_to_find:
                list_of_indexes.append(index)       
        for (index,item) in enumerate(list_of_indexes):
            try:
                saraksts[item]-=1
            except:
                a=1



    # print(len(saraksts))
    
    file.close()
    filerez=open(pathrez+"\\missing_no.txt","w")
    filerez.write(str(saraksts))
    filerez.close()
# print(saraksts)


filerez=open(pathrez+"\\missing_no.txt","w")
filerez.write(str(saraksts))
filerez.close()