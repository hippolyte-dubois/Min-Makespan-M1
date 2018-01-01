#! /usr/local/bin/python3

def msa(T, m):
    """
    In:
    - T, an int array of size n
    - m, the number of machines
    Out:
    - a dictionnary of (int, int array) of size m
    Complexity: O(n + m + n/m)
    """
    maxed = sum(T)/m
    tasks = []
    machines = {}
    i = 0
    while i < len(T):
        sumed = T[i]
        tasks.append([T[i]])
        i += 1
        while i < len(T) and sumed + T[i] <= maxed :
            sumed += T[i]
            tasks[len(tasks) - 1].append(T[i])
            i += 1

    for j in range(0,m):
        machines[j] = []    
    i = 0
    for t in tasks:        
        machines[i]=t
        i += 1
        i = i % m
    return machines