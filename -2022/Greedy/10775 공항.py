# 공항에는 G개의 게이트가 있으며 각각은 1에서 G까지의 번호를 가지고 있다.
# 공항에는 P개의 비행기가 순서대로 도착할 예정이며, 당신은 i번째 비행기를 1번부터 gi (1 ≤ gi ≤ G) 번째 게이트중 하나에 영구적으로 도킹하려 한다.
# 비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이후 어떤 비행기도 도착할 수 없다.

# 첫 번째 줄에는 게이트의 수 G (1 ≤ G ≤ 105)가 주어진다.
# 두 번째 줄에는 비행기의 수 P (1 ≤ P ≤ 105)가 주어진다.
# 이후 P개의 줄에 gi (1 ≤ gi ≤ G) 가 주어진다.
import sys
G_list = [0 for x in range(int(sys.stdin.readline()))]
P = int(sys.stdin.readline())
for _ in range(P):
    gi = int(sys.stdin.readline()) - 1
    G_list[gi] += 1

print(len(G_list)-G_list.count(0))