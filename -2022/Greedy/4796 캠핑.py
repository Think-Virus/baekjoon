# 캠핑장을 연속하는 P일 중, L일동안만 사용
# 강산이는 이제 막 V일짜리 휴가를 시작
# 강산이가 캠핑장을 최대 며칠동안 사용할 수 있을까?
"""
input :
5 8 20
5 8 17
0 0 0

result :
Case 1: 14
Case 2: 11
"""

# 틀린 것에 대한 반례 :
"""
2 8 20
0 0 0
answer : 6
my answer : 8
"""

import sys

Case_list = []
while True :
    tmp = list(map(int,sys.stdin.readline().split())) # L, P, V
    if tmp == [0,0,0] :
        break
    Case_list.append(tmp)

Cnt = 0
for _case in Case_list :
    Cnt += 1
    L = _case[0]
    P = _case[1]
    V = _case[2]

    if V - P*(V//P) >= L : #남은 일수보다 사용 가능한 기간이 작을 때
        print("Case {}: {}".format(Cnt, L * (V // P) + L))
    else :
        print("Case {}: {}".format(Cnt, V - P * (V // P) + L * (V // P)))


