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
    print("Case {}: {}".format(Cnt,_case[2]-_case[1]*(_case[2]//_case[1])+_case[0]*(_case[2]//_case[1])))
