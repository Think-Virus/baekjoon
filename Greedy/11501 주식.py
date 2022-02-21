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

    Candidate_list = []
    Sum_val = 0
    tmp_start = 0
    for i in range(N) :
        Max_val = max(Price_list[tmp_start:])
        Max_idx = Price_list.index(Max_val)
        if Price_list[i] == Max_val : # Max 값에 왔을 때
            tmp_start = i+1
            Sum_val = Sum_val + Max_val*len(Candidate_list) - sum(Candidate_list)
            Candidate_list = []
        else:
            Candidate_list.append(Price_list[i])
    Test_result.append(Sum_val)

for j in range(T) :
    print(Test_result[j])