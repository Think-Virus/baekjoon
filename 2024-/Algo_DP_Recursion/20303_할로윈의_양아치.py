"""
Python3 -> 시간초과
PyPy3 -> 정답
"""

import sys
from collections import deque


def solve():
    n, m, k = map(int, sys.stdin.readline().split())
    candies = [0] + list(map(int, sys.stdin.readline().split()))
    friends_connection = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        friend1, friend2 = map(int, sys.stdin.readline().split())
        friends_connection[friend1].append(friend2)
        friends_connection[friend2].append(friend1)

    # BFS
    queue = deque()
    visited = [False] * (n + 1)
    groups = []

    for i in range(1, n + 1):
        curr_group = [0, 0]
        if visited[i]:
            continue
        else:
            queue.append(i)
            visited[i] = True
            while queue:
                curr_friend = queue.popleft()
                curr_group[0] += 1
                curr_group[1] += candies[curr_friend]
                for friend in friends_connection[curr_friend]:
                    if visited[friend]:
                        continue
                    visited[friend] = True
                    queue.append(friend)
            groups.append(curr_group)

    dp = [0] * k
    for group_size, group_candy in groups:
        if group_size >= k:
            continue

        for j in range(k - 1, group_size - 1, -1):
            dp[j] = max(dp[j], dp[j - group_size] + group_candy)

    print(dp[k - 1])


if __name__ == "__main__":
    solve()
