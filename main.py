#! /usr/local/bin/python3

from random import randint

from lsa_f import lsa
from lsa_f import lpt
from msa_f import msa

Tasks = [2, 7, 1, 3, 2, 6, 2, 3, 6, 2, 5]
T2 = []
T3 = []
for i in range(0,50):
    T2.append(randint(1, 5))
    T3.append(randint(1,10))
'''
print(lsa(Tasks, 3))
print(lsa(T2, 3))
print(lsa(T3, 3))

print(lpt(Tasks, 3))
print(lpt(T2, 3))
print(lpt(T3, 3))

print(msa(Tasks, 3))
print(msa(T2,3))
print(msa(T3,3))
'''

msa_T1 = msa(Tasks, 3)
#msa_T2 = msa(T2, 3)
#msa_T3 = msa(T3, 3)

lsa_T1 = lsa(Tasks, 3)
lsa_T2 = lsa(T2, 3)
lsa_T3 = lsa(T3, 3)

lpt_T1 = lpt(Tasks, 3)
lpt_T2 = lpt(T2, 3)
lpt_T3 = lpt(T3, 3)
'''
for i in range(0,3):
    print(msa_T1[i])
    #print(msa_T2[i])
    #print(msa_T3[i])
    print("//////")

    print(lsa_T1[i])
    #print(lsa_T2[i])
    #print(lsa_T3[i])
    print("//////")

    print(lpt_T1[i])
    #print(lpt_T2[i])
    #print(lpt_T3[i])
    print("//////")
    print("------")
'''


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
    return [lsa(taches, machines), lpt(taches, machines), msa(taches, machines)]  


def affichage_instance(instance):
    print("Instance : machines = "+str(instance[0])+" | tâches = "+str(instance[1]))
    print()


def get_algorithm_result(result):
    return max([sum(x) for x in result.values()])


def affichage_resultats(results):
    print('Borne inférieure "maximum" = ' )
    print('Borne inférieure "moyenne" = ' )
    print('Résultat LSA = ' + str(get_algorithm_result(results[0])) )
    print('Résultat LPT = ' + str(get_algorithm_result(results[1])) )
    print('Résultat MSA = ' + str(get_algorithm_result(results[2])) )

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
                affichage_instance(instance)
            
                resultats = appel_algorithmes(instance[1],instance[0])
                affichage_resultats(resultats)
            except FileNotFoundError:
                print("Fichier inconnu, veuillez entrer un nom de fichier valide")
          

        # Chargement instance au clavier
        elif choix == "2" :
            instance = input('Instance : ')
            instance = transformation_instance(instance)
            affichage_instance(instance)
           
            resultats = appel_algorithmes(instance[1],instance[0])
            affichage_resultats(resultats)

        # Génération d'instance            
        elif choix == "3" :
            m = input("m : ")
            n = input("n : ")
            k = input("k : ")
            minVal = input("min : ")
            maxVal = input("max : ")
            print()

            instances = generation_instances(int(m),int(n),int(k),int(minVal),int(maxVal))
            for instance in instances:
                affichage_instance(instance)


        # Quitter le programme
        elif choix == "4" :
            end = True

        else :
            print("Choix incorrect")

        print()
        print("    -----------    ")
        print()


main()