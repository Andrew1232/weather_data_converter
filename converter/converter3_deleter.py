import os
path=os.path.dirname(__file__)+"\\rez2"
pathrez=os.path.dirname(__file__)+"\\rez3"
files=os.listdir(path)



file=open(os.path.dirname(__file__)+"\\binarais.txt","r")
binarais=file.read()
file.close()
binarais=binarais.split(", ")


def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)
list_of_num = []
list_of_indices = []


for (index, item) in enumerate(binarais):#pārbauda vai ir '' un ja ir tad to pieskaita attiecīgajā vietā sarakstā
    if int(item)==1:
        list_of_indices.append(index)


# file2=open(os.path.dirname(__file__)+"\\test.txt","w")
# file2.write(str(list_of_indices)[1:-1])
# file2.close()


# Remove elements from list_of_num at index 4,2 and 6





for y in files:# katram gadam folderī rez2
    print(y)
    file=open(path+"\\"+y,"r")
    filerez=open(pathrez+"\\"+y,"w")
    for x in file:  #katrai rindai jeb dienai katram gadam
        list_of_num=x.rstrip().split(",")
        delete_multiple_element(list_of_num, list_of_indices)
        filerez.write(str(list_of_num)[1:-1])
        filerez.write("\n")
    file.close()
    filerez.close()