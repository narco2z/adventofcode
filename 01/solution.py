import os

def read_input(file):
    path = str(os.path.realpath(__file__)).replace("solution.py", "")
    with open(path + file) as f:
        return [
            sum(int(cals) for cals in elf.split("\n")) 
            for elf in f.read().split("\n\n")
            ]

def solve(cals):
    return max(cals), sum(sorted(cals, reverse=True)[:3])

print(solve(read_input("input.txt")))