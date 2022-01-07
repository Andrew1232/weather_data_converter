# x1
# x2
# x3
# visufailusaraksts      stationList

# tuksarinda(visufailu saraksts bet visi ieraksti ir tusi listi)    tuksaRinda

# visufailubeigupunkti      beigas

# dienusarskstsstring   gadaDienas
# dienusarakstscipars   dienuSkaits
# celsuzievaddatiem     path
# celsuzizvaddatiem

import itertools
import os

path=os.path.dirname(__file__)+"\\data"
pathrez=os.path.dirname(__file__)+"\\rez"
N=''


file=open(os.path.dirname(__file__)+"\\stationList.txt","r")                #izveido stationList staciju sarakstu
stationList=file.read()[2:-2].replace("'","").replace(" '","").split(", ")
file.close()
# print(stationList)

tuksaRinda=[]
for x in stationList:
    tuksaRinda.append(['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])
# print(tuksarinda)['', '', '', '', '', '', '', '', '', '', '', '', '', '']

beigas=[]
for x in stationList:
    beigas.append(1)        # 1, jo pirmā rinda ir nosaukumi
# print(beigas)


counter=0


subfolders=os.listdir(path)

for fold in subfolders:              #katram gadam (katram apakšfolderim folderī dati)
    if counter<17:
        counter+=1
        print(fold)

        gads=str(fold)
        if int(gads)%4==0:#nosaka gada dienu sarakstu 01-01,01-02 un sienu skaitu gadā
            x="\\garaisgads.txt"
            dienuSkaits=366
        else:
            x="\\isaisgads.txt"
            dienuSkaits=365


        file=open(os.path.dirname(__file__)+x)      
        gadaDienas=file.read().replace("'","").replace(" '","")[1:-1].split(", ")
        file.close()
        


        filex=open(pathrez+"\\"+gads+".csv","w")
        for x in range(dienuSkaits):    #katrai gada dienai
            print(x)
            

            datums=gadaDienas[x]       # datums ir '01-01' formātā
            rinda=tuksaRinda.copy()
            diena=datums[3:]
            menes=datums[:2]
            for y in stationList:       #katrai stacijai
                try:

                    file=open(path+"\\"+gads+"\\"+y)
                    r=stationList.index(y)
                    k=beigas[r]
                    for i,line in enumerate(file):               #izvēlas pēdējo pārbaudīto tā faila rindu
                        if i == k :

                            line=line[:-1]
                            line=line.replace(', ',' ')
                            line=line.split(',')

                            datumsStacijai=line[1][6:-1]
                            if datumsStacijai == datums:
                                beigas[r]+=1 
                                dati=[]

                                x=float(line[6][1:-1])
                                if x==9999.9:
                                    x=N 
                                dati.append(x) # TEMP   

                                x=float(line[8][1:-1])
                                if x==9999.9:
                                    x=N
                                dati.append(x) # DEWP  

                                x=float(line[10][1:-1])
                                if x==9999.9:
                                    x=N     
                                dati.append(x)# SLP  

                                x=float(line[12][1:-1])
                                if x==999.9:
                                    x=N      
                                dati.append(x)# STP 

                                x=float(line[14][1:-1])
                                if x==999.9:
                                    x=N
                                dati.append(x)# VISIB 

                                x=float(line[16][1:-1])
                                if x==999.9:
                                    x=N      
                                dati.append(x)# WDSP

                                x=float(line[18][1:-1])
                                if x==999.9 :
                                    x=N        
                                dati.append(x)# MXSPD    

                                x=float(line[19][1:-1])
                                if x==999.9:
                                    x=N
                                dati.append(x)# GUST  

                                x=float(line[20][1:-1])
                                if x==9999.9:
                                    x=N
                                dati.append(x)# MAX 

                                x=float(line[22][1:-1])
                                if x==9999.9:
                                    x=N     
                                dati.append(x)# MIN     

                                x=float(line[24][1:-1])
                                if x==99.99:
                                    x=N 
                                dati.append(x)# PRCP 

                                x=line[25][1:-1]
                                if x=="H":
                                    x=0
                                elif x=="A":
                                    x=1
                                elif x=="B":
                                    x=2
                                elif x=="C":
                                    x=3
                                elif x=="D":
                                    x=4
                                elif x=="E":
                                    x=5
                                elif x=="F":
                                    x=6
                                elif x=="G":
                                    x=7
                                elif x=="I":
                                    x=N   
                                dati.append(x)      # PRCP ATR burti jāpārveido par cipariem

                                x=float(line[26][1:-1])
                                if x==999.9:
                                    x=0
                                dati.append(x)#    SNDP

                                x=(int(line[27][1]))#   FRSHTT  fog
                                dati.append(x)
                                x=(int(line[27][2]))#   FRSHTT  rain or drizzle
                                dati.append(x)
                                x=(int(line[27][3]))#   FRSHTT  snow or ice pellets
                                dati.append(x)
                                x=(int(line[27][4]))#   FRSHTT  hail
                                dati.append(x)
                                x=(int(line[27][5]))#   FRSHTT  thunder
                                dati.append(x)
                                rinda[r]=dati
                                dati=[]
                                
                except FileNotFoundError:
                    a=1
                except:
                    print("err")

                    
                    

            flat_ls = list(itertools.chain(*rinda))
            flat_ls.insert(0,int(menes))
            flat_ls.insert(0,int(diena))
            filex.write(str(flat_ls)[1:-1].replace("''",""))
            filex.write("\n")
        filex.close()
    else:
        break
# print(flat_ls)
# print(beigas)# ja rāda 366 isajā gadā vai 367 garajā gadā tad ir visi ieraksti

