import sys
import heapq


def input_data():
    t = int(sys.stdin.readline())
    test_cases = []
    for _ in range(t):
        n = int(sys.stdin.readline())
        scores = []
        for _ in range(n):
            heapq.heappush(scores, list(map(int, sys.stdin.readline().split())))

        test_cases.append((n, scores))

    return test_cases


def solve(test_cases):
    for n, scores in test_cases:
        result = 1
        limit_score = heapq.heappop(scores)[1]

        while scores:
            curr_score = heapq.heappop(scores)[1]
            if curr_score < limit_score:
                result += 1
                limit_score = curr_score
        print(result)


if __name__ == '__main__':
    test_cases = input_data()
    solve(test_cases)
