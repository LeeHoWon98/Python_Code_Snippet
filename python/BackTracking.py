import sys

n1, n2 = map(int, sys.stdin.readline().split())
numbers = []

def back():
    if len(numbers) == n2:
        print(" ".join(map(str, numbers)))
        return 
    for i in range(1, n1+1):
        if i not in numbers:
            numbers.append(i) 
            back()
            numbers.pop()
            
back()