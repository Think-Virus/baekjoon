# N개의 스위치와 N개의 전구
# 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태
# i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다
# 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.
# 불가능한 경우에는 -1을 출력
"""
input :
3
000
010

output :
3
"""

""" 
시간제한이 2초라서 로직을 잘 짜야 할 것 같은데..
000
110
101
010
3개씩 분석하고?
"""

"""
문제풀이 아이디어 :
'최소한의 횟수'를 구해야 하므로 왼쪽 첫 전구부터 오른쪽 끝 전구까지 1번씩만 체크하며 뒤집을지 여부를 체크해주면 된다.
(왜냐면 이미 왼쪽에서 맞춰놨는데 오른쪽으로 넘어간 후에 또 왼쪽을 볼 필요는 없기 때문에)
(1) 첫 번째 전구를 기준으로 불을 바꿔줬을 때
(2) 첫 번째 전구를 기준으로 불을 바꿔주지 않을 때

문제 풀이 아이디어 요약
(1) 2번째 전구부터 끝 전구까지는 왼쪽 전구를 기준으로 불 바꿔주는 여부를 선택.
=> for문을 전구의 수만큼 돌리기

(2) 1번째 전구를 바꿔줬을 때/아닐 때
=> (1)을 2번 돌리기
=> 내 코드에서는 전구의 불을 바꿔주는 걸 1번, 바꿔주지 않는 것을 2번으로 했다.
"""

import sys
import copy

N = int(sys.stdin.readline().rstrip())
Now_in = list(map(int,list(sys.stdin.readline().rstrip())))
Want = list(map(int,list(sys.stdin.readline().rstrip())))
Impossible_check = False

if N == 1 : #N이 1일 경우는 바로 출력 가능
    if Now_in != Want :
        print(0)
    else:
        print(1)

for k in range(2) :
    Cnt = 0
    Now = copy.deepcopy(Now_in)
    if k == 0 and Now != Want : # (1) 첫 번째 전구를 기준으로 불을 바꿔줬을 때
        Cnt += 1
        Now[0],Now[1] = 1-Now[0],1-Now[1]

    for i in range(1,N) :
        if Now[i-1] != Want[i-1] :  #뒤집을지 여부 또한 가운데 전구가 아닌 왼쪽 전구를 기준으로 판단 -> why? : 결과와 맞춰줄 수 있는 마지막 기회이기 때문
            if i != N-1 :
                Cnt +=1
                Now[i-1], Now[i], Now[i+1] = 1-Now[i-1],1-Now[i], 1-Now[i+1]
            else: #가장 마지막
                Cnt +=1
                Now[i - 1], Now[i] = 1-Now[i-1],1-Now[i]
    if Now != Want:
        Impossible_check = True
    else:
        Impossible_check = False
        print(Cnt)
        break
if Impossible_check :
    print(-1)