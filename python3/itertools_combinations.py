#! /bin/python3

from itertools import combinations

if __name__ == '__main__':
    S = input()
    
    def print_combination(n):
        str_list = (n.split(' ')[0]).upper()
        count = int(n.split(' ')[1])

        for i in range(1, count + 1):
            combines = (combinations(str_list, i))
            y = []
            for combination in combines:
                print(''.join(str(e) for e in combination))
                #y.append(combination)
            #y.sort()
            #print(''.join(str(e) for e in y))
    
    print_combination(S)

