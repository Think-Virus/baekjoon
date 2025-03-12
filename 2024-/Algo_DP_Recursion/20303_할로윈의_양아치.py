import sys


class FriendCandyGraph:
    def __init__(self, root, candy):
        self.root = root
        self.friends = []
        self.size = 1
        self.candies = candy

    def add(self, friend, candy):
        self.friends.append(friend)
        self.size += 1
        self.candies += candy

    def is_included(self, friend):
        return friend in self.friends


def solve():
    n, m, k = map(int, sys.stdin.readline().split())
    candies = [0] + list(map(int, sys.stdin.readline().split()))
    graphs: list[FriendCandyGraph] = []
    for _ in range(m):
        friend1, friend2 = map(int, sys.stdin.readline().split())

        is_new_group = True
        for graph in graphs:
            if graph.root == friend1:
                graph.add(friend2, candies[friend2])
                is_new_group = False
                break
            if graph.root == friend2:
                graph.add(friend1, candies[friend1])
                is_new_group = False
                break
            if graph.is_included(friend1):
                graph.add(friend2, candies[friend2])
                is_new_group = False
                break
            if graph.is_included(friend2):
                graph.add(friend1, candies[friend1])
                is_new_group = False
                break

        if is_new_group:
            new_group = FriendCandyGraph(friend1, candies[friend1])
            new_group.add(friend2, candies[friend2])
            graphs.append(new_group)

    graph_size = len(graphs)

    dp = [[0] * k for _ in range(graph_size + 1)]

    for _i, graph in enumerate(graphs):
        i = _i + 1
        group_size = graph.size
        group_candy = graph.candies

        if group_size >= k:
            continue

        for j in range(group_size):
            dp[i][j] = dp[i - 1][j]
        for j in range(group_size, k):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - group_size] + group_candy)

    print(dp[graph_size][k - 1])


if __name__ == "__main__":
    solve()
