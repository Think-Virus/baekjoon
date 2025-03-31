import heapq


def solve():
    n, k = map(int, input().split())
    total_number = input()
    number_order = []
    result = [''] * n
    cnt = 0

    for i, number in enumerate(total_number):
        heapq.heappush(number_order, (-1 * int(number), i))

    while cnt != n - k:
        passed_list = []
        largest_num_index = number_order[0][1]
        while number_order:
            curr_num, curr_i = heapq.heappop(number_order)
            if curr_i >= largest_num_index:
                result[curr_i] = -1 * curr_num
                cnt += 1

                if cnt == n - k:
                    break
            else:
                heapq.heappush(passed_list, (int(curr_num), curr_i))
        number_order = passed_list
    print(*result, sep='')


if __name__ == '__main__':
    solve()
