from re import A
import pandas as p
from scipy.stats import skew 

#from  pycm import * 
######################################
def ReadDataSet(filename):
        d= p.read_csv(filename, sep='/')
        return d

def colonnes(d,roll=[],pitch=[],yaw=[]):

        lignes=d.values 

        dataset = lignes.tolist()
        for x in range (len(dataset)):
            roll.append(dataset[x][0])
            pitch.append(dataset[x][1])
            yaw.append(dataset[x][2])
        return roll,pitch,yaw
        #################
def WriteFilePre(filename, instance):
            
        with open(filename,'a') as f:
                  for i in range(0,len(instance)-1):
                        f.write(str(instance[i])+",")
                  f.write(str(instance[len(instance)-1]))    
                  f.write("\n")
                  f.close()
        print("****ADD Instance : success !")
a=0
print("\n********************Debut ******************\n1 : right mouvement\n0 : wrong mouvement")
while a==0 :
        d = ReadDataSet(r'C:\Users\THINK PRO\Desktop\PFE FINAL\Collecte des données\moves\2 off.txt')
        file=int(input("__________________________\nreponse = "))
        
        l= list(colonnes(d,[],[],[]))
        print("\n")
        move=[]
        move.append(max(l[0]))
        move.append(max(l[1]))
        move.append(max(l[2]))
        move.append(min(l[0]))
        move.append(min(l[1]))
        move.append(min(l[2]))
        move.append(sum(l[0])/len(l[0]))
        move.append(sum(l[1])/len(l[1]))
        move.append(sum(l[2])/len(l[2]))
        move.append(max(l[0])-min(l[0]))
        move.append(max(l[1])-min(l[1]))
        move.append(max(l[2])-min(l[2]))
        move.append(skew(l[0]))
        move.append(skew(l[1]))
        move.append(skew(l[2]))
        if (file==1):
                move.append("1")
                a=1
        elif(file==0):
                        move.append("0")
                        a=1
        else: 
                print('error : choose : ___________________ \n0 : for wrong mouvement \n1 : for right mouvement ')
                a=0

print(move)
WriteFilePre(r'C:\Users\THINK PRO\Desktop\PFE FINAL\csv files\Train1.csv',move)



