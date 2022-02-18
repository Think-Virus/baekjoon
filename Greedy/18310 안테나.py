# 1등 코드 공부
"""
n = int(input())
a = list(map(int,input().split()))

a.sort()

print(a[(n-1)//2])
-> 나는 중앙이 아니라 그 좌 우까지 확인해야 한다고 생각했는데, 굳이 그러지 않아도 된듯.. 중간값이 작게 나오는듯
WHY?
n이 홀수인 경우에는 당연히 중간값에서 각 점들과의 거리가 제일 가까움
n이 짝수일 때에는 중간값을 어디로 잡아야 할지 애매할 수 있는데 아래를 보면 이해하기가 편함
1 3 5 7 -> 이렇게 값이 주워졌을 때, (n-1)//2하면 idx 1임
idx 1일 때 거리를 생각하면
-> abs(1-3) + abs(3-3) + abs(5-3) + abs(7-3) = 2 + 0 + 2 + 4 = 8
저게 아닌 것 같으면 idx가 2일때를 생각하니까 그 경우도 보면
-> abs(1-5) + abs(3-5) + abs(5-5) + abs(7-5) = 4 + 2 + 0 + 2 = 8
즉, 덧셈의 순서만 바뀜
이거 생각해보면 수학적으로도 증명 가능
"""

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
