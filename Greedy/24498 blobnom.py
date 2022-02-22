# 블롭들은 심심해서 서로를 이용해 N개의 탑을 만들었다. 각 탑의 높이는 그 탑에 있는 블롭의 수와 같다.
# 1. 처음과 마지막이 아닌 탑 중 하나를 선택한다. 단, 선택한 탑과 인접한 두 탑의 높이가 모두 1 이상이어야 한다.
# 2. 선택한 탑과 인접한 두 탑에 있는 블롭을 한 마리씩 각각 땅에 내려놓는다. 즉, 인접한 두 탑의 높이가 모두 1만큼 감소한다.
# 3. 땅에 내려놓은 두 마리의 블롭 중 하나의 블롭만 1.에서 선택한 탑에 쌓는다. 즉, 선택한 탑의 높이가 1만큼 증가한다.
# 이 과정에서 이전에 인접하지 않았던 두 탑이 새롭게 인접하게 되지는 않는다. 채완이를 위해 만들 수 있는 가장 높은 탑의 높이를 구해 주자.

"""
In :
4
1 3 2 2
Out :
4

예상 풀이 로직
-> 처음과 마지막이 아닌 탑들에서 선택한 탑 좌/우 중 작은 것과 합들 중 가장 큰 값 들을 list로 구해서 max 값을 표출
"""
import sys

N = int(sys.stdin.readline())
A_list = list(map(int, sys.stdin.readline().split()))
B_list = list(enumerate(A_list))[1:-1]  # idx 저장
Result_list = []


def solve(tup):
    idx = tup[0]
    val = tup[1]
    add_val = min(A_list[idx - 1], A_list[idx + 1])
    Result_list.append(val + add_val)
    return tup


tmp = list(map(solve, B_list))
print(max(Result_list))
