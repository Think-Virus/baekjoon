"""
1. 주식 하나를 산다.
2. 원하는 만큼 가지고 있는 주식을 판다.
3. 아무것도 안한다.
위 행동 중 하나만 함

날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산하기

max값 이후에는 다음 max값 확인해서 해야 함
max값 이전까지는 계속 구매해도 괜찮음
"""
import sys
T = int(sys.stdin.readline())
Test_result = []
for _ in range(T) :
    N = int(sys.stdin.readline())
    Price_list = list(map(int,sys.stdin.readline().split()))

    if Price_list == sorted(Price_list, reverse=True):
        Test_result.append(0)
        continue

    Candidate_list = []
    Sum_val = 0
    while Price_list :
        Max_val = max(Price_list)
        Max_idx = Price_list.index(Max_val)
        Sum_val = Sum_val + Max_val * len(Price_list[:Max_idx]) - sum(Price_list[:Max_idx])
        Price_list = Price_list[Max_idx+1:]
    Test_result.append(Sum_val)

for j in range(T) :
    print(Test_result[j])