"""
문제
    외판원 순회 문제는 영어로 Traveling Salesman problem (TSP) 라고 불리는 문제로 computer science 분야에서 가장 중요하게 취급되는 문제 중 하나이다.
    여러 가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자.1번부터 N번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다. (길이 없을 수도 있다)
    이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다. 단, 한 번 갔던 도시로는 다시 갈 수 없다.
    (맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외) 이런 여행 경로는 여러 가지가 있을 수 있는데, 가장 적은 비용을 들이는 여행 계획을 세우고자 한다.
    각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다. W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다.
    비용은 대칭적이지 않다. 즉, W[i][j] 는 W[j][i]와 다를 수 있다. 모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다.
    경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0이라고 하자.
    N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.

입력
    첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 16) 다음 N개의 줄에는 비용 행렬이 주어진다.
    각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다. W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.
    항상 순회할 수 있는 경우만 입력으로 주어진다.

출력
    첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
---
    1시간 10분간 고민해봤지만 각이 안 나옴
---
    이전에 해답 봤음
    DFS 이해가 부족하여 복습하고 다시 시도
"""
import sys


def input_data():
    n = int(sys.stdin.readline())
    edges = build_graph(n)

    return n, edges


def build_graph(n):
    edges = [[] for _ in range(n)]
    for i in range(n):
        edges[i] = list(map(int, sys.stdin.readline().split()))
    return edges


def solve():
    n, edges = input_data()
    dp = [[-1 for _ in range(1 << n)] for _ in range(n)]

    def _dfs(x, visited):
        if visited == (1 << n) - 1:  # 마지막 마을까지 도착한 것
            # 처음으로 돌아가는 비용만 확인하면 됨
            if edges[x][0]:  # 돌아갈 수 있는 경우
                return edges[x][0]
            else:  # 돌아갈 수 없는 경우
                return -1

        if dp[x][visited] != -1:  # 이미 계산이 된 경우
            return dp[x][visited]

        for i in range(1, n):  # 0번째 도시부터 시작했으므로, 1번째 도시부터 모든 도시 탐방
            if not edges[x][i]:  # x번째 도시에서 i번째 도시로 가는 길이 없는 경우, skip
                continue
            if visited & (1 << i):  # 이미 방문한 도시라면, skip
                """
                ex)
                    visited : 111 => 0번 도시부터 1,2번째 도시까지 방문하고 1번째 도시로 돌아가는 비용 계산됨
                    - i : 1 -> 1 << 1 = 10 -> 이미 1번째 도시는 방문했었으므로 다시 볼 필요 없음
                    - i : 3 -> 1 << 3 = 1000 -> 3번째 도시는 방문한 적이 없으므로 계산 필요
                """
                continue

            _dfs_cost = _dfs(i, visited | (1 << i))

            if _dfs_cost == -1:  # 길이 끊어져있는 경우
                continue
            else:
                _dfs_cost += edges[x][i]
                dp[x][visited] = min(dp[x][visited], _dfs_cost) if dp[x][visited] != -1 else _dfs_cost

        return dp[x][visited]

    print(_dfs(0, 1))


if __name__ == '__main__':
    solve()
