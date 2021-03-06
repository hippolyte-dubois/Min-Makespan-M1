#! /usr/local/bin/python3

def first_available(machines):
    """
    In:
    - machines, a dictionnary of (int, int array)
    Out:
    - the id of the first available machine
    """
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
    - a dictionnary of (int, int array) of size m
    Complexity: O(n * m)
    """
    machines = {}
    for i in range(0, m):
        machines[i] = []
    for task in T:
        machines[first_available(machines)].append(task)
    return machines

def lpt(T, m):
    """
    In:
    - T, an int array of size n
    - m, the number of machines
    Out:
    - a dictionnary of (int, int array) of size m
    Complexity: O(n log n + n * m)
    """
    sorted_tasks = sorted(T,reverse=True) # Timsort algorithm O(n log n)
    return lsa(sorted_tasks, m)
