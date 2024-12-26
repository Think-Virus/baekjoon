#     +---+
#     | D |
# +---+---+---+---+
# | E | A | B | F |
# +---+---+---+---+
#     | C |
#     +---+
# 주사위는 위와 같이 생겼다. 주사위의 여섯 면에는 수가 쓰여 있다. 위의 전개도를 수가 밖으로 나오게 접는다.
# A, B, C, D, E, F에 쓰여 있는 수가 주어진다.
# 지민이는 현재 동일한 주사위를 N^3개 가지고 있다.
# 이 주사위를 적절히 회전시키고 쌓아서, N×N×N크기의 정육면체를 만들려고 한다. 이 정육면체는 탁자위에 있으므로, 5개의 면만 보인다.
# N과 주사위에 쓰여 있는 수가 주어질 때, 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램을 작성하시오.

"""
완벽한 하나의 공식이 있다고 생각했는데 아닌듯..
풀이법 :
3면이 보이는 주사위 : 4개
2면이 보이는 주사위 : (N-2)*4 + (N-1)*4
1면이 보이는 주사위 : (N-2)*(N-2) + (N-1)*(N-2)*4

-> 3면 최소 조합, 2면 최소조합, 1면 최소 값을 구해야 함
"""
N = int(input())
arr = list(map(int, input().split()))
ans = 0
min_lists = []
if N == 1:
    arr.sort()
    for i in range(5):
        ans += arr[i]
else:
    min_lists.append(min(arr[0], arr[5]))
    min_lists.append(min(arr[1], arr[4]))
    min_lists.append(min(arr[2], arr[3]))
    min_lists.sort()

    # 1, 2, 3 면의 주사위 최소값
    min1 = min_lists[0]
    min2 = min_lists[0] + min_lists[1]
    min3 = sum(min_lists)

    # 1, 2, 3 면의 주사위 개수
    n1 = 4 * (N - 2) * (N - 1) + (N - 2) ** 2
    n2 = 4 * (N - 1) + 4 * (N - 2)
    n3 = 4

    ans += min1 * n1
    ans += min2 * n2
    ans += min3 * n3
print(ans)