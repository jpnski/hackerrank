#! /bin/python3

# set to get unique values in array
# sorted function to list in ascending order
# index second to last

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    print(sorted(set(arr))[-2])
