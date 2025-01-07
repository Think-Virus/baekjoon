import sys

T = int(input())
data = [sum(list(map(int, list(sys.stdin.readline().split())))) for _ in range(T)]

for r in data:
    print(r)
