#! /bin/python3

if __name__ == '__main__':
    n = int(input())     
    nested_list = [] 
    
    for i in range(n):
        name = input()
        score = float(input())
        nested_list.append([name, score])

    scores = list(set(nested_list[i][1] for i in range(n)))
    scores.sort() 

    names = [i[0] for i in nested_list if i[1] == scores[1]]
    names.sort() 

    for name in names:
        print(name)
