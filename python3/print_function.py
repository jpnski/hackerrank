#! /bin/python3

# print() parameters:
# *obj, sep, end, file, flush
#   *range() prints parameters of range
#       1, input, is string of 1 to n
#   sep separates each character of string with no whitespace
#       else will print each character separated by 1 space

if __name__ == '__main__':
    n = int(input())

    def print_fn(n):
        print(*range(1, n + 1), sep="")

    print_fn(n)
