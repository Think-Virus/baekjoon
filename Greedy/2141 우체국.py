# 수직선과 같은 일직선상에 N개의 마을이 위치해 있다. i번째 마을은 X[i]에 위치해 있으며, A[i]명의 사람이 살고 있다.
# 이 마을들을 위해서 우체국을 하나 세우려고 하는데, 그 위치를 어느 곳으로 할지를 현재 고민 중이다.
# 고민 끝에 나라에서는 각 사람들까지의 거리의 합이 최소가 되는 위치에 우체국을 세우기로 결정하였다. 우체국을 세울 위치를 구하는 프로그램을 작성하시오.
# 각 마을까지의 거리의 합이 아니라, 각 사람까지의 거리의 합임에 유의한다

"""
In :
3
1 3
2 5
3 3

Out :
2

사람 수가 우선일듯
-> 우체국의 위치가 x라고 했을 때 방정식을 구해보면
|(x-1)|*3 + |(x-2)|*5 + |(x-3)|*3 이게 최소값이 되는 거니까..
-> 일단 우체국은 마을에 있어야 하는 게 맞음 Why? 거리기 때문에.. 예를 들어서
극단적인 값을 잡아보자
In :
3
1 3
5 5
100 2
--> |(x-1)|*3 + |(x-5)|*5 + |(x-100)|*2

거리들의 평균값 구하고 그 값을 기준으로 작은 값이 많은지, 큰 값이 많은지 확인해서
작은 값이 많아다면 작은 값들 중에서 사람 수가 제일 많은 곳이 우체국의 위치고
큰값이 많다면 큰 값들 중에서 사람 수가 제일 많은 곳
"""

"""
정답 확인
1. 거리의 합이 최소가 되려면 우체국은 어느 한 마을 위치에 지어져야 함
2. 우체국이 있는 지점에서 왼쪽과 오른쪽에 있는 사람의 수는 같거나 그 차이가 최소가 되어야 함
"""
import sys

N = int(sys.stdin.readline())
village_list = []
total_people = 0

for _ in range(N):
    x, a = map(int, sys.stdin.readline().split())
    total_people += a
    village_list.append([x, a])
village_list.sort()

now_people = village_list[0][1]
pre_diff = abs(now_people - (total_people / 2))
for i in range(1,N) :
    now_people += village_list[i][1]
    now_diff = abs(now_people - (total_people / 2))
    if now_people > total_people // 2 :
        if now_diff > pre_diff :
            print(village_list[i-1][0])
            exit()
        else:
            print(village_list[i][0])
            exit()
    elif now_people == total_people :
        print(village_list[i][0])
        exit()