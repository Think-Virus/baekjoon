# 기다란 벤치 모양의 식탁에 사람들과 햄버거가 아래와 같이 단위 간격으로 놓여 있다.
# 사람들은 자신의 위치에서 거리가 K 이하인 햄버거를 먹을 수 있다.
# 식탁의 길이 $N$, 햄버거를 선택할 수 있는 거리 $K$, 사람과 햄버거의 위치가 주어졌을 때,
# 햄버거를 먹을 수 있는 사람의 최대 수를 구하는 프로그램을 작성하시오.

"""
In
20 1
HHPHPPHHPPHPPPHPHPHP

Out
8
"""

N,K = map(int,input().split())
N_str = input()
hamberger_position = [0 for i in range(N)]
person_position = [0 for i in range(N)]

ans = 0
for i,n in enumerate(N_str) :
    if n == 'H' :
        hamberger_position[i] = 1
    else :
        person_position[i] = 1

ans = 0
for i in range(N) :
    if person_position[i] == 1 :
        if i-K < 0 :
            start_K = 0
        else :
            start_K = i-K
        if 1 in hamberger_position[start_K : i+K+1] :
            ans += 1
            hamberger_position[start_K+hamberger_position[start_K : i+K+1].index(1)] = 0

print(ans)
