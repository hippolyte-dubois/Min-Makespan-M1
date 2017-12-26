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
        res.append((T,m))
    return res

def main():
    end = False
    while not(end):
        print("Choisir un mode d'execution : ")
        print("1 : Charger une instance depuis un fichier")
        print("2 : Charger une instance au clavier")
        print("3 : Génération aléatoire d'instances")
        print("4 : Quitter le programme")

        choix = input()

        if choix == "1" :
            None

        elif choix == "2" :
            None

        elif choix == "3" :
            m = input("m : ")
            n = input("n : ")
            k = input("k : ")
            minVal = input("min : ")
            maxVal = input("max : ")

            instances = generation_instances(int(m),int(n),int(k),int(minVal),int(maxVal))
            print(instances)


        elif choix == "4" :
            end = True

        else :
            print("Choix incorrect")
        print()
        print("    -----------    ")
        print()


main()