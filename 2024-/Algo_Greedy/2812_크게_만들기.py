def solve():
    n, k = map(int, input().split())
    total_number = input()
    stack = []

    for number in total_number:
        while stack and stack[-1] < number and k > 0:
            stack.pop()
            k -= 1
        stack.append(number)

    if k > 0:
        print(''.join(stack[:-k]))
    else:
        print(''.join(stack))


if __name__ == '__main__':
    solve()
