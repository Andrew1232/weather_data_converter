import os
file=open(os.path.dirname(__file__)+"\\missing_no.txt","r")
rinda=file.read()[1:-1]
finda=rinda.split(", ")
binarais=[]
counter=0
for x in finda:
    if int(x)>700:
        
        binarais.append(1)
    else:
        counter+=1
        binarais.append(0)
file.close()
print(counter)
file2=open(os.path.dirname(__file__)+"\\binarais.txt","w")
file2.write(str(binarais)[1:-1])
file2.close()