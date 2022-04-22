import queue
predecessors = {}

def throw(positions,bird_char,bird_number,n):
    a,b = bird_char[bird_number]
    un = positions[bird_number]
    if bird_number == 0:
        positions[bird_number] = b*positions[bird_number+1] - un
    elif bird_number == n-1:
        positions[bird_number] = a*positions[bird_number-1] - un
    else:
        positions[bird_number] = a*positions[bird_number-1] + b*positions[bird_number+1] - un
    predecessors[''.join(str(positions))] = bird_number+1
    return positions

def combinations(a,b,n,special_bird):
    bird_char = [(1, 1)] * n
    bird_char[special_bird] = (a, b)
    final = [[1] * n]
    bird_positions_queue = queue.LifoQueue()
    bird_positions_queue.put([1]*n)
    while not bird_positions_queue.empty():
        new_bird_positions = bird_positions_queue.get()
        for bird_number in range(n):
            potential_new_combination = throw(new_bird_positions,bird_char,bird_number,n)
            if potential_new_combination not in final:
                final.append(potential_new_combination.copy())
                bird_positions_queue.put(potential_new_combination.copy())
    return final

def special_bird(a,b,n):
    foo = []
    for i in range(n):
        foo.append(["L'oiseau spécial de paramètre a,b se trouve en position",i+1])
        for element in combinations(a,b,n,i):
            if element not in foo:
                foo.append(element)
                foo.append([predecessors[''.join(str(element))]])
    return foo

a = int(input("entrez a [mettez 1 par défaut]"))
b = int(input("entrez b [mettez 1 par défaut]"))
n = int(input("entrez n (supérieur ou égale à 2)"))
print(special_bird(a,b,n))
