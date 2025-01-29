"""
문제
여행을 떠난 세준이는 지도를 하나 구하였다. 이 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다.
한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여 있으며, 각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능하다.

현재 제일 왼쪽 위 칸이 나타내는 지점에 있는 세준이는 제일 오른쪽 아래 칸이 나타내는 지점으로 가려고 한다.
그런데 가능한 힘을 적게 들이고 싶어 항상 높이가 더 낮은 지점으로만 이동하여 목표 지점까지 가고자 한다.
위와 같은 지도에서는 다음과 같은 세 가지 경로가 가능하다.

지도가 주어질 때 이와 같이 제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 지도의 세로의 크기 M과 가로의 크기 N이 빈칸을 사이에 두고 주어진다.
이어 다음 M개 줄에 걸쳐 한 줄에 N개씩 위에서부터 차례로 각 지점의 높이가 빈 칸을 사이에 두고 주어진다.
M과 N은 각각 500이하의 자연수이고, 각 지점의 높이는 10000이하의 자연수이다.

출력
첫째 줄에 이동 가능한 경로의 수 H를 출력한다. 모든 입력에 대하여 H는 10억 이하의 음이 아닌 정수이다.
---
접근법
    cond 1. 상하좌우로만 이동 가능 -> [i][j-1] [i][j+1] [i-1][j] [i+1][j]만 비교하면 됨
    cond 2. 항상 작은 곳으로만 이동 가능

    df[i][j] = max(df[i][j], df ([i][j-1] [i][j+1] [i-1][j] [i+1][j]) 중 가능한 방향만)
    if df[i][j]가 변경되면 df[i][j]에서 이동 가능한 항목들도 update...? -> 재귀가 될 것 같은데...
"""
import sys

sys.setrecursionlimit(10 ** 6)


def input_data():
    n, m = map(int, sys.stdin.readline().split())  # n : 세로 / m : 가로
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    return data, n, m


def solve():
    data, n, m = input_data()
    moves = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]
    visited = [[-1 for _ in range(m)] for _ in range(n)]

    def dfs(x, y):
        if x == n - 1 and y == m - 1:
            return 1

        if visited[x][y] != -1:
            return visited[x][y]

        visited[x][y] = 0

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if data[x][y] > data[nx][ny]:
                    visited[x][y] += dfs(nx, ny)

        return visited[x][y]

    print(dfs(0, 0))


if __name__ == '__main__':
    solve()
