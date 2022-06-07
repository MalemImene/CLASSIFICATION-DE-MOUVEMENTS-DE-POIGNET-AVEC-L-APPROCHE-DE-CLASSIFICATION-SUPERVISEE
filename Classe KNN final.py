import pandas as p
import random
import math
import time
import operator

class KNN:
      # Dans la class chaque fonction doit contenir "self" correpons a l'objet (passe en parametre)
      #Quant on applle une fonction a l'interieur d'une fonction on mis NOMCLASS.NOMMETHOD(self)
      #version 0.0 1/04/2022  
      #version 0.1 10/04/2022  
      #version 1.0 14/04/2022 
      #version 1.1 15/04/2022 
      #version 1.2 17/04/2022 
      #version 1.3 23/04/2022
      #version 2.0 10/05/2022
      #version 2.1 11/05/2022
      ####################################################################
      def Dataset(self , filename,dataset=[]):
         
            # Lire la dataset
            d=p.read_csv(filename, sep=',')
            # transformation des lignes de la dataset en liste
            lignes=d.values
            dataset = lignes.tolist()
            # Affichage de la longeur de la dataset
            print("la longeur du Dataset = ",len(dataset))
            # Info sur les dataset
            print("\n******************** Informations sur les attributs du dataset *******************\n")
            info=d.info()
            print("\n**********************************************************\n\n")  
            return dataset
      
      #############################################
       #la soustraction d'un attribut par attribut se fait d'une maniere automatique entre les deux ligne , ici line veut dire element
      def distanceEcludienne(self,line1 , line2 , length):
         distance=0         
         for x in range(length):
               if (type(line1[x]) == str) | (type(line2[x]) == str) :
                     if line1[x]==line2[x] :
                           distance=0
                     else:
                           distance=1
               else:
                      distance += pow((line1[x]-line2[x]),2)
                      
         return math.sqrt(distance)
         
      #############################################     
      def VoisinKNN(self,instanceTest , trainingSet , k):
            distance = []
    
            # dans le length de test on met -1 psk le test ne contient pas de classe(label)
            length = len(instanceTest) -1

            #calculer la distance entre chaque nouvelle instance et les element de train dataset
            #puis ajouter le resultat dans une liste contenant "l'instance, la distance et l'indice de l'instance"
            for x in range(len(trainingSet)):
                dist = KNN.distanceEcludienne(self,instanceTest,trainingSet[x],length)
                distance.append((trainingSet[x],dist,x))

                
            #faire le tri selon la distance du plus petite au plus grande distance    
            distance.sort(key=operator.itemgetter(1))
            
            voisins=[]
            IndiceDist=[]
            #Garder que les K premières instances dans la liste "voisins" et la distance avec l'indice dans la liste "IndiceDist"
            for x in range (k):
                voisins.append(distance[x][0])
                #IndiceDist contient la distance , et l'indice de l'element
                IndiceDist.append((distance[x][2],distance[x][1]))
            

            #voisinKNN retourn un enregistrement de deux listes voisins et IndiceDist
            return voisins,IndiceDist

      ##Divide dataset into trainingSet and testSet

      ##########################################################################################
      def DivideDataset(self ,filename , split , trainingDataset=[] , testSet=[]):
            d=p.read_csv(filename, sep=',')
            # X dans les ligne et Y dans les colonne
            lignes=d.values
            dataset = lignes.tolist()
            #choisir un nombre aléatoirement pour diviser le dataset en train et test
            for x in range (1,len(dataset)):
                    a = random.random()
                    if a < split:
                        trainingDataset.append(dataset[x])
                    else:
                        testSet.append(dataset[x])
             #le résultat c'est un enregistrement de deux liste.                    
            return trainingDataset,testSet
      
      ###### ici voisins c'est une liste qui contient toute les voisins (comme des elements)######################################
      def ClassifyF (self,K,trainingDataset , testSet,predected_liste ):
            
                      
            #pour chaque instance faire
            for x in range (len(testSet)):
      
                  #former l'ensemble des K voisins
                  v=KNN.VoisinKNN(self,testSet[x] , trainingDataset , K)
                  voisins=v[0]

                  #declarer un dictionnaire (enregistrement cle:valeur)**VoisinOccurance={'normal':3}
                  VoisinOccurance = {}
                  #pour chaque voisin determiner le nombre d'occurrence de chaque classe
                  for y  in range (len(voisins)):
                        #voisins[x][-1] le x correspond a la ligne et le -1 (modulo) c la classe
                        ClasseChoisie = voisins[y][-1]
                        if ClasseChoisie in VoisinOccurance:
                              VoisinOccurance[ClasseChoisie]+=1
                        else:
                              VoisinOccurance[ClasseChoisie]=1
                                
                           
                  VoisinOccSorted = sorted(VoisinOccurance.items(),key=operator.itemgetter(1),reverse=True)
                  testSet[x][-1]=VoisinOccSorted[0][0]
                  predected_liste.append(testSet[x])
                 
                 # print("L'instance = ",testSet[x])
                 # print("classe actuelle=",testSet[x][len(testSet[x])-1])
                 # print("Prediction =",testSet[x][-1])
            
            return predected_liste
            


      ###### ici voisins c'est une liste qui contient toute les voisins (comme des elements)######################################
      def ClassifyU (self,K,trainingDataset , unlabelledDS,filename):
            
            #pour chaque instance faire
            for x in range (len(unlabelledDS)):
                                    
                  #former l'ensemble des K voisins
                  v=KNN.VoisinKNN(self,unlabelledDS[x] , trainingDataset , K)
                  voisins=v[0]

                  #declarer un dictionnaire (enregistrement cle:valeur)**VoisinOccurance={'normal':3}
                  VoisinOccurance = {}
                  #pour chaque voisin determiner le nombre d'occurrence de chaque classe
                  for y  in range (len(voisins)):
                        #voisins[x][-1] le x correspond a la ligne et le -1 (modulo) c la classe
                        ClasseChoisie = voisins[y][-1]
                        if ClasseChoisie in VoisinOccurance:
                              VoisinOccurance[ClasseChoisie]+=1
                        else:
                              VoisinOccurance[ClasseChoisie]=1
                                
                           
                  VoisinOccSorted = sorted(VoisinOccurance.items(),key=operator.itemgetter(1),reverse=True)
                  print("L'instance = ",unlabelledDS[x])
                  print("classe actuelle=",unlabelledDS[x][-1])
                  unlabelledDS[x][-1]=VoisinOccSorted[0][0]                  
                  print("Prediction =",unlabelledDS[x][-1])
                  data=KNN.WriteFile( self, filename,unlabelledDS[x])
                        
            return unlabelledDS
      
      ###############################################################
      def ClassifyI (self,trainingDataset , instance,K):
            #print("***********Classification à base d'une Instance*******************")
            #former l'ensemble des K voisins
            v=KNN.VoisinKNN(self,instance , trainingDataset , K)
            voisins=v[0]
            VoisinOccurance = {}
            #pour chaque voisin determiner le nombre d'occurrence de chaque classe
            for y  in range (len(voisins)):
                  #voisins[x][-1] le x correspond a la ligne et le -1 on travaille par modulo il correspond a la derniere case(c'est la classe)
                  #VoisinOccurance contient le nombre d'occurrence de chaque classe dans l'ensemble "voisin"
                  ClasseChoisie = voisins[y][-1]
                  if ClasseChoisie in VoisinOccurance:
                        VoisinOccurance[ClasseChoisie]+=1
                  else:
                        VoisinOccurance[ClasseChoisie]=1

            VoisinOccSorted = sorted(VoisinOccurance.items(),key=operator.itemgetter(1),reverse=True)
            print('\nla classe est:',VoisinOccSorted[0][0])
            for x in range(len(instance)):
                  if(x == (len(instance)-1)):        
                        instance[x]=VoisinOccSorted[0][0]
                        
            return VoisinOccSorted[0][0],v[1]

      ###################################################################
      def WriteFile( self, filename, instance):
            
            with open(filename,'a') as f:
                  for i in range(0,len(instance)-1):
                        f.write(str(instance[i])+",")
                  f.write(str(instance[len(instance)-1]))    
                  f.write("\n")
                  f.close()
            print("****ADD Instance : success !")
      ####################################################################
      def classes(self,dataset):
            actual=[]
            classe=[]
            
            for x in range(len(dataset)):
                  actual.append(dataset[x][-1])

            actual.sort()
            
            classe.append(actual[0])
            for x in range(len(actual)-1):
                  if actual[x]!=actual[x+1] :
                        classe.append(actual[x+1])
                  
            return classe
      ####################################################################
      def getlist_class(self,dataset,liste):
            for x in range(len(dataset)):
                  liste.append(dataset[x][-1])
            return liste

      ####################################################################
      def conf_matrix(self,test,classified_l,train): 
            
              
            actual=KNN.getlist_class(self,test,[])
            predicted=KNN.getlist_class(self,classified_l,[])

            classes=KNN.classes(self,train)
            a=classes[0]
            b=classes[1]

            FN=0
            FP=0
            TN=0
            TP=0
            
            for x in range(len(actual)):

                  if actual[x]==a and predicted[x]==a :
                        TP=TP+1
                  if actual[x]==a and predicted[x]==b :
                        FN=FN+1
                  if actual[x]==b and predicted[x]==b :
                        TN=TN+1
                  if actual[x]==b and predicted[x]==a :
                        FP=FP+1
                  
                  
            return TP,FP,TN,FN   
      
      ################################################################
      def print_CM(self,TP,FP,TN,FN,dataset ):
            classes=KNN.classes(self,dataset)
            print("*****************Matrice de confusion******************\n")
            print("                  Actual\n")
            print("                  a\t b\n")
            print("             a\t ",TP,"\t",FP,"      a=",classes[0])
            print("predicted\n")
            print("             b\t ",FN,"\t",TN,"     b=",classes[1],'\n')

      #######################################################################
      def mesure_de_qualité(self,TP,FP,TN,FN ):
            
            accuracy=(TP+TN)/(TP+TN+FP+FN)
            
            precision=TP/(TP+FP)
            
            rappel=TP/(TP+FN)
            
            f_mesure=(2*precision*rappel)/(precision+rappel)
            print("\n************les mesures de qualité *********")
            
            print("accuracy=",accuracy)
            print("precision=",precision)
            print("rappel=",rappel)            
            print("f_mesures=",f_mesure)

            return accuracy,precision,rappel,f_mesure
      #######################################################################
      def ADDInstnace( self, train, instance):
            train.append(instance)
            return train    

      #######################################################################
      def ClassifyInc(self, train, test,K,predicted):
             
            for i in range(len(test)):          

                  instance_actual= test[i]
                  x=instance_actual[-1]

                  instance= KNN.ClassifyI(self, train, test[i],K)

                  if x != instance[0] :
                        if x == 1 :
                              instance_actual.pop(-1)
                              instance_actual.append(0)
                              #instance_actual[len(instance_actual)-1]="0"
                        elif x == 0:
                              instance_actual.pop(-1)
                              instance_actual.append(1)
                              #instance_actual[len(instance_actual)-1]="1"
                        else:
                              print("invalid test")                               
                        KNN.ADDInstnace(self,train,instance_actual)                        
                        KNN.WriteFile(self,r'.\csv files\train.csv',instance_actual) 
                        print("success")

                  predicted.append(instance_actual)
            
            return predicted


########### Call Object ########################################"  
start_time = time.time()            
#cree un objet
Obj1=   KNN()

#pour utiliser la fct Dividedataset
#train,test = KNN.DivideDataset(Obj1,r'C:\Users\THINK PRO\Desktop\L3 ACAD\PFE\Code KNN (ClassifyI) les points\train.csv' , 0.5 , [] , [])

#-----------------Creer les dataset du train et test-------------------------------
train = KNN.Dataset(Obj1,r'C:\Users\THINK PRO\Desktop\PFE FINAL\csv files\traain.csv',[])
test= KNN.Dataset(Obj1,r'C:\Users\THINK PRO\Desktop\PFE FINAL\csv files\test.csv',[])

#-----------------effectuer un test en utilisant classifyF-------------------------
#print("***********Classification à base d'un fichier*******************")
predicted=[]
predicted = KNN.ClassifyF(Obj1, 9 , train , test,[])

#-----------------pour afficher la dataset avant et apres le traitement----------- 
#print(train)
#print("New trainTest After KNN Classification à base d'un fichier(train and test datasets)=",ClassifiedDataset)


#-----------------Classifier une instance en utilisant classifyI-----------------------
#instance=[10.54,20.68,89.17,2.11,7.35,-1.01,6.779679144385022,14.683903743315502,42.88208556149732,8.43,13.33,90.18,-0.3851264552017302,-0.21249758562933088,-0.009467223398892742,'']
#labelled_instance = KNN.ClassifyI(Obj1, train , instance,7)
#data = KNN.WriteFile(Obj1,r'C:\Users\THINK PRO\Desktop\L3 ACAD\PFE\Code KNN (ClassifyI) mouvements\classified_instances.csv',train, instance)

#---------Classifier un fichier d'instances en utilisant ClassifyU--------
#unlabelled_file= KNN.Dataset(Obj1,r'C:\Users\THINK PRO\Desktop\PFE FINAL\csv files\unlabelled.csv',[])
#labelled_file=KNN.ClassifyU(Obj1, 3 , train , unlabelled_file ,r'C:\Users\THINK PRO\Desktop\PFE FINAL\csv files\labelled.csv')

#------------------matrice de Confusion et mesures de qualité---------------------------
actual_liste= KNN.Dataset(Obj1,r'C:\Users\THINK PRO\Desktop\PFE FINAL\csv files\test.csv',[])
TP,FP,TN,FN = KNN.conf_matrix(Obj1,actual_liste,predicted,train)
KNN.print_CM(Obj1,TP,FP,TN,FN,train )
accuracy,precision,rappel,f_mesure=KNN.mesure_de_qualité(Obj1,TP,FP,TN,FN )


#-------------------------calcule du temps d'execution---------------------------------
print("\nTemps d execution : %s secondes ---" % (time.time() - start_time))