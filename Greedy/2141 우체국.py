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
import sys
N = int(sys.stdin.readline())
candidate_list = []
mid_point=0

for _ in range(N) :
    x,a = map(int,sys.stdin.readline().split())
    mid_point += x
    candidate_list.append([x,a])
candidate_list.sort()

mid_point = mid_point / N
short_vil = [i for i in candidate_list if i[0] < mid_point]
long_vil = [i for i in candidate_list if i[0] >= mid_point]

def find_max_people(seq) :
    global max_people
    global max_seq
    if seq[1] >= max_people :
        max_people = seq[1]
        max_seq = seq
    return 0

max_seq = []
max_people = 0
if len(short_vil) > len(long_vil) : # 작은 값이 많은 경우
    galbage = list(map(find_max_people,short_vil))
elif len(short_vil) < len(long_vil) : # 큰 값이 많은 경우
    galbage = list(map(find_max_people,long_vil))
else: # 두 값이 같은 경우
    galbage = list(map(find_max_people,candidate_list))

print(max_seq[0])
# def find_point(seq) :
#     global max_seq
#     return abs(seq[0]-max_seq[0])*seq[1]
#
# print(sum(map(find_point,candidate_list)))