import heapq


def solve():
    n, k = map(int, input().split())
    total_number = input()

    def fill_result(s_index, f_index, rest):
        if f_index - s_index < 0:
            print(0)
            return None

        r_result = [''] * n

        if f_index - s_index < rest:
            r_result[s_index:f_index + 1] = total_number[s_index:f_index + 1]
            return r_result, s_index - 1, rest - (f_index - s_index)

        while rest != 0:
            number_order = []
            for i, number in enumerate(total_number[s_index:f_index + 1]):
                heapq.heappush(number_order, (-1 * int(number), i + s_index))
            rest -= 1

            curr_max_num, curr_i = heapq.heappop(number_order)
            r_result[curr_i] = -1 * curr_max_num
            if rest == 0:
                return r_result, curr_i, rest

            fill_result_set = fill_result(curr_i + 1, f_index, rest)
            if fill_result_set:
                r_result[curr_i + 1:f_index + 1] = fill_result_set[0][curr_i + 1:f_index + 1]
                f_index = fill_result_set[1]
                rest = fill_result_set[2]
            else:
                f_index -= 1

        return r_result, f_index, rest

    result = fill_result(0, n - 1, n - k)[0]
    print(*result, sep='')


if __name__ == '__main__':
    solve()
