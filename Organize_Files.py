import os, shutil
lis=[]
i=1
destinationdir='/Users/Your_Username/Desktop/Everthing'
while os.path.exists(destinationdir):
    destinationdir+=str(i)
    i+=1
os.makedirs(destinationdir)

lis=os.listdir('/Users/Your_Username/Desktop')
for x in lis:
    print(x)
    if x==__file__:
        continue
    shutil.move(x,destinationdir)