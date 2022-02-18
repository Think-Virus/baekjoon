# 일직선 상의 마을에 여러 채의 집이 위치
# 이중에서 특정 위치의 집에 특별히 한 개의 안테나를 설치
# 효율성을 위해 안테나로부터 모든 집까지의 거리의 총 합이 최소가 되도록 설치
# 이 때 안테나는 집이 위치한 곳에만 설치할 수 있고, 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능
# 집들의 위치 값이 주어질 때, 안테나를 설치할 위치를 선택하는 프로그램을 작성
# 첫째 줄에 안테나를 설치할 위치의 값을 출력한다. 단, 안테나를 설치할 수 있는 위치 값으로 여러 개의 값이 도출될 경우 가장 작은 값을 출력한다.

"""
절대값을 이용하면 될라나?
ex)
In :
4
5 1 7 9

Out :
5
"""
import sys
N = int(sys.stdin.readline())
Position_list = list(map(int,sys.stdin.readline().split()))
Position_list.sort()

def find_length(val1,val2) :
    return abs(val1-val2)

while True :
    if N < 3 :
        print(Position_list[0])
        break

    mid_idx = N // 2
    Check_list = []
    for i in range(-1,2,1) :
        criterion = Position_list[mid_idx + i]
        tmp_sum = 0
        for postion in Position_list :
            tmp_sum += find_length(criterion,postion)
        Check_list.append((criterion,tmp_sum))
    Check_list.sort(key= lambda x:(x[1],x[0]))
    print(Check_list[0][0])
    break
