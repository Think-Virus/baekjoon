import heapq


def solve():
    n = input()
    numbers = []
    is_zero = False
    for w in n:
        if w == "0":
            is_zero = True
        heapq.heappush(numbers, -1 * int(w))

    if not is_zero:
        print(-1)
    else:
        if sum(numbers) % 3 == 0:
            result = 0
            while numbers:
                curr = heapq.heappop(numbers) * (-1)
                result = result * 10 + curr

            print(result)
        else:
            print(-1)


if __name__ == '__main__':
    solve()
