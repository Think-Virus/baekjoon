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


def build_graph(n) -> list[list[int]]:
    edges = [[] for _ in range(n)]
    for i in range(n):
        edges[i] = list(map(int, sys.stdin.readline().split()))
    return edges


def solve():
    n, edges = input_data()
    INF = int(1e9)
    dp = [[-1 for _ in range(1 << n)] for _ in range(n)]

    # 마지막 DFS의 끝나는 지점 판별을 위한 if문 제거를 위해 미리 최종 경로 값 저장
    # 0번 노드를 마지막으로 방문해야 하므로 111..0 상태가 가장 마지막 상태 -> (1<<n)-2가 됨
    for i in range(1, n):
        if edges[i][0]:
            dp[i][(1 << n) - 2] = edges[i][0]
        else:
            dp[i][(1 << n) - 2] = INF

    def _dfs(x, visited):
        # 방문한 노드인 경우 DP값을 return
        if dp[x][visited] != -1:
            return dp[x][visited]

        for j in range(1, n):  # 0번째 도시부터 시작했으므로, 1번째 도시부터 모든 도시 탐방
            if not edges[x][j]:  # x번째 도시에서 i번째 도시로 가는 길이 없는 경우, skip
                continue
            if visited & (1 << j):  # 이미 방문한 도시라면, skip
                """
                ex)
                    visited : 111 => 0번 도시부터 1,2번째 도시까지 방문하고 1번째 도시로 돌아가는 비용 계산됨
                    - j : 1 -> 1 << 1 = 10 -> 이미 1번째 도시는 방문했었으므로 다시 볼 필요 없음
                    - j : 3 -> 1 << 3 = 1000 -> 3번째 도시는 방문한 적이 없으므로 계산 필요
                """
                continue

            if dp[x][visited] == -1:  # 처음 방문한 경우
                dp[x][visited] = _dfs(j, visited | (1 << j)) + edges[x][j]
            else:
                dp[x][visited] = min(dp[x][visited], _dfs(j, visited | (1 << j)) + edges[x][j])

        # 모든 반복문을 수행한 후에 dp의 값이 -1인 경우
        # 이 경우는 지금 상태 (now) 에서 1111..1(최종경로)로 가는 경우가 없다는 것을 의미한다.
        # 그러므로 -1이 아닌 INF를 저장해 줌으로써 방문했지만 경로가 없다는 것을 나타내준다.
        if dp[x][visited] == -1:
            return INF

        return dp[x][visited]

    print(_dfs(0, 0))


if __name__ == '__main__':
    solve()
