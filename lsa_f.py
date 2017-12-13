#! /usr/local/bin/python3

def first_available(machines):
    i = 0
    min_id = 0
    min_value = sum(machines[0])
    for m in machines.values():
        v = sum(m)
        if v < min_value:
            min_id = i
            min_value = v
        i = i + 1
    return min_id

def lsa(T, m):
    """
    In:
    - T, an int array of size n
    - m, the number of machines
    Out:
    - an array of array of int of size m
    """
    machines = {}
    for i in range(0,m):
        machines[i] = []
    for task in T:
        machines[first_available(machines)].append(task)
    return machines

