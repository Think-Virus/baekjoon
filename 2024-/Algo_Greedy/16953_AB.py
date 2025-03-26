def solve():
    a, b = map(int, input().split())

    cnt = 0
    while a != b:
        if b % 10 == 1:
            b = b // 10
        elif b % 2 == 0:
            b = b // 2
        else:
            print(-1)
            return

        cnt += 1
        if a > b:
            print(-1)
            return

    print(cnt + 1)


if __name__ == '__main__':
    solve()
