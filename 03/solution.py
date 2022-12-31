import os

def read_input(file):
    path = str(os.path.realpath(__file__)).replace("solution.py", "")
    with open(path + file) as f:
        return [
            str(set(line[len(line)//2:]).intersection(set(line[:len(line)//2])))[2]
            for line in f.read().split("\n")
            ]

def solve(file):
    return file
print(solve(read_input("test.txt")))
