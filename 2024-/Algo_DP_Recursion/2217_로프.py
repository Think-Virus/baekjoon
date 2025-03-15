import sys
import heapq


def input_data():
    n = int(sys.stdin.readline())
    ropes = []
    for _ in range(n):
        heapq.heappush(ropes, int(sys.stdin.readline()))

    return n, ropes


def solve(n, ropes):
    max_weight = 0
    for i in range(n, 0, -1):
        min_ropes = heapq.heappop(ropes)
        max_weight = max(max_weight, min_ropes * i)
    print(max_weight)


if __name__ == '__main__':
    n, ropes = input_data()
    solve(n, ropes)
