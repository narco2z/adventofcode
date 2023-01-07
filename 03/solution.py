import os

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def read_input(file):
    path = str(os.path.realpath(__file__)).replace("solution.py", "")
    with open(path + file) as f:
        return [
            str(set(line[len(line)//2:]).intersection(set(line[:len(line)//2])))[2]
            for line in f.read().split("\n")
            ]

def solve(file):
    x = 0
    for i in file:
        if i.islower():
            x = x + alphabet.index(i) + 1
        else:
            x = x +alphabet.index(i.lower()) + 27
    return x
print(solve(read_input("input.txt")))
