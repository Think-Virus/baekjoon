def solve():
    s = input()
    pre_w = ""
    simple_s = ""
    for w in s:
        if w != pre_w:
            simple_s += pre_w
            pre_w = w
    simple_s += pre_w

    cnt_zero = 0
    cnt_one = 0

    for w in simple_s:
        if w == "0":
            cnt_zero += 1
        else:
            cnt_one += 1

    print(min(cnt_zero, cnt_one))


if __name__ == '__main__':
    solve()
