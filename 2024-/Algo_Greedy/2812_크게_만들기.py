import heapq


def solve():
    n, k = map(int, input().split())
    total_number = input()
    number_order = []
    result = [''] * n
    cnt = 0

    for i, number in enumerate(total_number):
        heapq.heappush(number_order, (-1 * int(number), i))

    start_index = number_order[0][1] + 1
    end_index = n - 1
    is_next = True

    while cnt != n - k:
        curr_num, curr_i = heapq.heappop(number_order)

        if result[curr_i]:
            continue

        if curr_i < start_index and not is_next:
            continue

        result[curr_i] = -1 * curr_num
        cnt += 1

        if cnt == n - k:
            break

        start_index = curr_i + 1
        tmp_heapq = []
        if n - k - cnt >= end_index - start_index + 1:
            for i in range(start_index, end_index + 1):
                result[i] = total_number[i]
                cnt += 1

                if cnt == n - k:
                    break
            end_index = curr_i - 1
            is_next = True
        else:
            for i in range(start_index, end_index + 1):
                heapq.heappush(tmp_heapq, (-1 * int(total_number[i]), i))

            while tmp_heapq:
                tmp_num, tmp_i = heapq.heappop(tmp_heapq)
                if tmp_i < start_index:
                    continue

                result[tmp_i] = -1 * tmp_num
                cnt += 1
                if cnt == n - k:
                    break
                start_index = tmp_i + 1
            is_next = False
        start_index = curr_i + 1

    print(*result, sep='')


if __name__ == '__main__':
    solve()
