import os
path=os.path.dirname(__file__)+"\\data"
datasubfolders=os.listdir(path)
datasetStations=[]
for subfolder in datasubfolders:   #for all subfolders in the folder data
    print(subfolder)
    dictionary={}
    folder=path+"\\"+subfolder
    faili=os.listdir(folder)
    for file in faili:                              #katram failam subfolderī
        file_size = os.path.getsize(folder+"\\"+file)
        dictionary[file]=file_size
    for x in dictionary:
        if dictionary[x]>=60000 and x not in datasetStations:
            datasetStations.append(x)

file=open(os.path.dirname(__file__)+"\\stationList.txt","w")
file.write(str(datasetStations))
file.close()