import heapq


def solve():
    n, k = map(int, input().split())
    total_number = input()
    number_order = []
    result = [''] * n
    cnt = 0

    for i, number in enumerate(total_number):
        heapq.heappush(number_order, (-1 * int(number), i))

    largest_num_index = number_order[0][1]
    left = n - largest_num_index
    while cnt != n - k:
        curr_num, curr_i = heapq.heappop(number_order)
        if curr_i >= largest_num_index:
            result[curr_i] = -1 * curr_num
            cnt += 1
            left -= 1
        else:
            if n - k - cnt > left:
                largest_num_index = curr_i
                result[curr_i] = -1 * curr_num
                cnt += 1
                left = n - curr_i - cnt
    print(*result, sep='')


if __name__ == '__main__':
    solve()
