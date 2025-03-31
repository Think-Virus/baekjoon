import heapq


def solve():
    n, k = map(int, input().split())
    total_number = input()
    number_order = []

    for i, number in enumerate(total_number):
        heapq.heappush(number_order, (int(number), i))

    for _ in range(k):
        print(heapq.heappop(number_order))


if __name__ == '__main__':
    solve()
