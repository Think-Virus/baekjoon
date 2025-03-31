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
        curr_num, curr_i = heapq.heappop(number_order)

        result[curr_i] = -1 * curr_num
        cnt += 1

        tmp_heap = []
        while number_order:
            tmp_num, tmp_i = heapq.heappop(number_order)
            if tmp_i < curr_i:
                heapq.heappush(tmp_heap, (tmp_num, tmp_i))
            else:
                result[tmp_i] = -1 * tmp_num
                cnt += 1
                if cnt == n - k:
                    break
        number_order = tmp_heap

    print(*result, sep='')


if __name__ == '__main__':
    solve()
