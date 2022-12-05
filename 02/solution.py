import os
from collections import Counter

def read_input(file):
    path = str(os.path.realpath(__file__)).replace("solution.py", "")
    with open(path + file) as f:
        return [pairs for pairs in f.read().split("\n")] 

def solution(file):
    cn = Counter(file)
    result = 0
    won = ('A Y', 'B Z', 'C X')
    draw = ('A X', 'B Y', 'C Z')
    for i in cn:
        if i in won:
            result = result + (cn[i] * 6)
        elif i in draw:
            result += (cn[i] * 3)
    for i in file:
        if "X" in i:
            result += 1
        elif "Y" in i:
            result += 2
        else:
            result += 3
    return result

def solution2(file):
    cn = Counter(file)
    result = 0
    for i in cn:
        if 'Z' in i:
            if 'A' in i:
                result += 8 * cn[i]
            elif 'B' in i:
                result += 9 * cn[i]
            else:
                result += 7 * cn[i]
        elif 'Y' in i:
            if 'A' in i:
                result += 4 * cn[i]
            elif 'B' in i:
                result += 5 * cn[i]
            else:
                result += 6 * cn[i]
        else:
            if 'A' in i:
                result += 3 * cn[i]
            elif 'B' in i:
                result += 1 * cn[i]
            else:
                result += 2 * cn[i]
    return result


print(solution(read_input("input.txt")))
print(solution2(read_input("input.txt")))
