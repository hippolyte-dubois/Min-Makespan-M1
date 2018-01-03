#! /usr/local/bin/python3

from random import randint

from lsa_f import lsa
from lsa_f import lpt
from my_algo_f import my_algo


def generation_instances(m,n,k,minVal,maxVal):
    res = []
    for i in range(k):
        T=[]
        for j in range(n):
            T.append(randint(minVal,maxVal))
        res.append((m,T))
    return res


def transformation_instance(ligne):
    modifiedList = [int(x) for x in ligne.split(":")]
    machines = modifiedList.pop(0)
    tasks = modifiedList.pop(0)
    return (machines, modifiedList)


def lecture_fichier(fichier):    
    file  = open(fichier, "r")
    return transformation_instance(file.read())
   

def appel_algorithmes(taches, machines):
    return [lsa(taches, machines), lpt(taches, machines), my_algo(taches, machines)]  


def affichage_instance(instance):
    return("Instance : machines = "+str(instance[0])+" | tâches = "+str(instance[1])+'\n') 


def get_algorithm_result(result):
    return max([sum(x) for x in result.values()])


def affichage_resultats(instance,results):
    return('Borne inférieure "maximum" = Topt >= ' + str(max(instance[1])) +'\n'+
          'Borne inférieure "moyenne" = Topt >= ' + str(sum(instance[1])/instance[0]) +'\n'+    
          'Résultat LSA : '+str(get_algorithm_result(results[0])) +'\n'+   
          'Résultat LPT : '+str(get_algorithm_result(results[1])) +'\n'+  
          'Résultat MyAlgo : '+str(get_algorithm_result(results[2]))+ '\n' )



def main():
    end = False
    while not(end):
        print("Choisir un mode d'execution : ")
        print("1 : Charger une instance depuis un fichier")
        print("2 : Charger une instance au clavier")
        print("3 : Génération aléatoire d'instances")
        print("4 : Quitter le programme")

        choix = input()
        print()

        # Chargement depuis fichier
        if choix == "1" :
            fichier = input("Nom du fichier : ")
            try:
                instance = lecture_fichier(fichier)
                print(affichage_instance(instance))
            
                resultats = appel_algorithmes(instance[1],instance[0])
                print(affichage_resultats(instance,resultats))
            except FileNotFoundError:
                print("Fichier inconnu, veuillez entrer un nom de fichier valide")
          

        # Chargement instance au clavier
        elif choix == "2" :
            instance = input('Instance : ')
            instance = transformation_instance(instance)
            print(affichage_instance(instance))
           
            resultats = appel_algorithmes(instance[1],instance[0])
            print(affichage_resultats(instance,resultats))

        # Génération d'instance            
        elif choix == "3" :
            m = input("m : ")
            n = input("n : ")
            k = input("k : ")
            minVal = input("min : ")
            maxVal = input("max : ")
            filename = input("Nom du fichier de sauvegarde : ")

            instances = generation_instances(int(m),int(n),int(k),int(minVal),int(maxVal))

            fichierResultat = open(filename, "w")

            ratioLPT = 0
            ratioLSA = 0
            ratioMyAlgo = 0

            for instance in instances:
                fichierResultat.write(affichage_instance(instance)+'\n')
                resultats = appel_algorithmes(instance[1],instance[0])

                m1 = (max(sum(instance[1])/instance[0], max(instance[1])))

                ratioLSA += get_algorithm_result(resultats[0])/m1
                ratioLPT += get_algorithm_result(resultats[1])/m1
                ratioMyAlgo += get_algorithm_result(resultats[2])/m1

                fichierResultat.write(affichage_resultats(instance,resultats)+'\n')
                fichierResultat.write("     ----------------------------      \n\n")

            fichierResultat.write("ratio d’approximation moyen LSA = "+ str(ratioLSA/float(k))+'\n')
            fichierResultat.write("ratio d’approximation moyen LPT = "+ str(ratioLPT/float(k))+'\n')
            fichierResultat.write("ratio d’approximation moyen MyAlgo = "+ str(ratioMyAlgo/float(k))+'\n')

            fichierResultat.close()


        # Quitter le programme
        elif choix == "4" :
            end = True

        else :
            print("Choix incorrect")

        print()
        print("    -----------    ")
        print()


main()