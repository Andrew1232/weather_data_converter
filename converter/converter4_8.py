import os
path=os.path.dirname(__file__)+"\\rez4_5"
pathrez=os.path.dirname(__file__)+"\\rez4_6"
files=os.listdir(path)



for y in files:
    print(y)
    file=open(path+"\\"+y,"r")
    filex=open(pathrez+"\\"+y,"w")
    for x in file: 
        y=x.rstrip().replace("', '",",")[1:-1]
        y=y.replace("'","").replace('"','')
        y=y.replace("''","")
        filex.write(y)
        filex.write("\n")
    file.close()
    filex.close()

# for y in files:
#     print(y)
#     file=open(path+"\\"+y,"r")
#     filex=open(pathrez+"\\"+y,"w")
    # for x in file: 
    #     x=x.rstrip().replace(" ","")
    #     x.replace("''","")
    #     filex.write(x)
    #     filex.write("\n")
#     print(file.readline().rstrip().replace("', '",",")[1:-1])
#     file.close()
#     filex.close()
#     break