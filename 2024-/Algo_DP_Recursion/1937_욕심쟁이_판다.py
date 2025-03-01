"""
문제
    n × n의 크기의 대나무 숲이 있다. 욕심쟁이 판다는 어떤 지역에서 대나무를 먹기 시작한다. 그리고 그 곳의 대나무를 다 먹어 치우면 상, 하, 좌, 우 중 한 곳으로 이동을 한다.
    그리고 또 그곳에서 대나무를 먹는다. 그런데 단 조건이 있다. 이 판다는 매우 욕심이 많아서 대나무를 먹고 자리를 옮기면 그 옮긴 지역에 그 전 지역보다 대나무가 많이 있어야 한다.
    이 판다의 사육사는 이런 판다를 대나무 숲에 풀어 놓아야 하는데, 어떤 지점에 처음에 풀어 놓아야 하고,
    어떤 곳으로 이동을 시켜야 판다가 최대한 많은 칸을 방문할 수 있는지 고민에 빠져 있다. 우리의 임무는 이 사육사를 도와주는 것이다.
    n × n 크기의 대나무 숲이 주어져 있을 때, 이 판다가 최대한 많은 칸을 이동하려면 어떤 경로를 통하여 움직여야 하는지 구하여라.

입력
    첫째 줄에 대나무 숲의 크기 n(1 ≤ n ≤ 500)이 주어진다. 그리고 둘째 줄부터 n+1번째 줄까지 대나무 숲의 정보가 주어진다.
    대나무 숲의 정보는 공백을 사이로 두고 각 지역의 대나무의 양이 정수 값으로 주어진다. 대나무의 양은 1,000,000보다 작거나 같은 자연수이다.

출력
    첫째 줄에는 판다가 이동할 수 있는 칸의 수의 최댓값을 출력한다.

4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8
"""
import sys
sys.setrecursionlimit(100000)

def input_data():
    n = int(sys.stdin.readline())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    return n, graph


def solve(n, graph):
    dp = [[0] * n for _ in range(n)]

    def _dfs(x, y):
        can_go = []

        if dp[x][y] != 0:
            return dp[x][y]

        for dx in [-1, 1]:
            nx = x + dx
            if 0 <= nx < n and graph[nx][y] > graph[x][y]:
                can_go.append((nx, y))

        for dy in [-1, 1]:
            ny = y + dy
            if 0 <= ny < n and graph[x][ny] > graph[x][y]:
                can_go.append((x, ny))

        if not can_go:  # 더 이상 갈 곳이 없는 경우
            dp[x][y] = 1
            return dp[x][y]

        for nx, ny in can_go:
            dp[x][y] = max(dp[x][y], _dfs(nx, ny) + 1)
        return dp[x][y]

    max_move = 0
    for i in range(n):
        for j in range(n):
            max_move = max(max_move, _dfs(i, j))

    print(max_move)


if __name__ == '__main__':
    n, graph = input_data()
    solve(n, graph)
