import sys


def input_data():
    n = int(sys.stdin.readline())
    meetings = [[0, 0]]
    for _ in range(n):
        time, cost = map(int, sys.stdin.readline().split())
        meetings.append((time - 1, cost))
    return n, meetings


def solve(n, meetings):
    dp = [[0] * (n + 1) for _ in range(n + 2)]
    for i in range(n, 0, -1):
        if i + meetings[i][0] > n:  # time over
            continue

        end_meeting = i + meetings[i][0]
        dp[i][end_meeting] = meetings[i][1]

        for j in range(end_meeting + 1, n + 1):
            dp[i][j] = max(dp[i][end_meeting] + dp[j][n], dp[i + 1][j], dp[i][j - 1])

    print(dp[1][n])


if __name__ == '__main__':
    n, meetings = input_data()
    solve(n, meetings)
