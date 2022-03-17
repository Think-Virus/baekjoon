# 0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.
# 행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)
# 첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.
# 첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.

"""
위에서 아래로, 왼쪽에서 오른쪽으로 간다고 했을 때, 3x3의 1행과 1열이 마지막으로 변경 가능한 지점이니 이걸 확인하면 될 듯
-> 둘 중 하나라도 값이 다르면 뒤집기


왼쪽 열을 확인할 수 있는 횟수는 M을 3으로 나누고 (몫-1)*3 + (나머지+1)
위쪽 행을 확인할 수 있는 횟수는 N을 3으로 나누고 (몫-1)*3 + (나머지+1)

위와 같은 과정으로 다 뒤집었는데도 서로 다르면 -1 출력

위쪽 행만 확인해도 괜찮을 듯
"""


"""
안될 듯
반례 :
5 5
00000
00000
00000
00000
00000
00000
00000
00111
00111
00111

00000
00000
10010
10010
10010

-> 왼쪽 열하고 위쪽 행이 둘 다 다를 때만 뒤집어야 할까?
만약 그랬을 때 안될만한 예시는?
"""
import sys

N, M = map(int, sys.stdin.readline().split())
A_list = []
B_list = []

for _ in range(N):
    A_list.append(list(map(int,list(sys.stdin.readline().rstrip()))))
for _ in range(N):
    B_list.append(list(map(int,list(sys.stdin.readline().rstrip()))))

if A_list == B_list :
    print(0)
    exit()

if N < 3 or M < 3:
    print(-1)
    exit()

def map_reverse(val) :
    return (val+1)%2

def reverse_3x3(seq,r,c) :
    tmp = []
    for row in seq[r:r+3] :
        tmp_row = row[:c]+list(map(map_reverse,row[c:c+3])) + row[c+3:]
        tmp.append(tmp_row)
    return seq[:r]+tmp+seq[r+3:]

Cnt = 0
for i in range((N // 3 - 1) * 3 + N % 3 + 1):  # i : 위쪽 행
    for j in range((M // 3 - 1) * 3 + M % 3 + 1):  # j : 왼쪽 열, 컴프리헨션 사용해서 확인하면 될듯
        if A_list[i][j:j + 3] != B_list[i][j:j + 3] and (A_list[i][j]!=B_list[i][j] or A_list[i+1][j]!=B_list[i+1][j] or A_list[i+2][j]!=B_list[i+2][j]):  # 위쪽 행과 왼쪽 열 확인
            # 뒤집는 연산 함수 필요
            B_list = reverse_3x3(B_list,i,j)
            Cnt += 1
            continue
if A_list == B_list :
    print(Cnt)
else:
    print(-1)