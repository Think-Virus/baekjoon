def input_data():
    n = int(input())
    milks = list(map(int, input().split()))

    return milks


def solve(milks):
    pre_milk = -1
    result = 0
    for milk in milks:
        if pre_milk == -1:
            if milk == 0:
                result += 1
                pre_milk = milk
        else:
            if pre_milk + 1 == milk:
                result += 1
                pre_milk = milk
            elif pre_milk == 2 and milk == 0:
                result += 1
                pre_milk = milk

    print(result)


if __name__ == '__main__':
    milks = input_data()
    solve(milks)
