import heapq

def throw(positions,bird_char,bird_number,n):
    a,b = bird_char[bird_number]
    un = positions[bird_number]
    if bird_number == 0:
        positions[bird_number] = b*positions[bird_number+1] - un
    elif bird_number == n-1:
        positions[bird_number] = a*positions[bird_number-1] - un
    else:
        positions[bird_number] = a*positions[bird_number-1] + b*positions[bird_number+1] - un
    return positions

def combinations(a,b,n,special_bird):
    bird_char = [(1, 1)] * n
    bird_char[special_bird] = (a, b)
    final = [[1] * n]
    bird_positions_queue = [[1]*n]
    while bird_positions_queue:
        new_bird_positions = heapq.heappop(bird_positions_queue)
        for bird_number in range(n):
            potential_new_combination = throw(new_bird_positions,bird_char,bird_number,n)
            if potential_new_combination not in final:
                print(final)
                final.append(potential_new_combination.copy())
                heapq.heappush(bird_positions_queue,potential_new_combination.copy())
    return final

def special_bird(a,b,n):
    foo = []
    for i in range(n):
        foo.append(combinations(a,b,n,i))
    return foo

print(special_bird(2,1,3))
#combinations(2,1,3)

#faire en sorte que le special bird reste le même entre deux essais !

