# 6줄 패키지를 살 수도 있고, 1개 또는 그 이상의 줄을 낱개로 살 수도 있다.
# 끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고, 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격,
# 낱개로 살 때의 가격이 주어질 때, 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램
# N은 100보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수

# 정답 로직
# 경우의 수가 3개 있음
# 1. 세트로만 사서 가격이 초과하는 경우
# 2. 세트와 개수 혼합해서 사는 경우
# 3. 낱개로만 사는 경우

import sys
N, M = map(int,sys.stdin.readline().split())

Min_set_price,Min_one_price = map(int,sys.stdin.readline().split())
for i in range(1,M) :
    tmp_set_price,tmp_one_price = map(int,sys.stdin.readline().split())
    if tmp_set_price < Min_set_price : # 가장 낮은 가격의 set 인덱스 찾기
        Min_set_price = tmp_set_price
    if tmp_one_price < Min_one_price : # 가장 낮은 가격의 one 인덱스 찾기
        Min_one_price = tmp_one_price

Count_six = N // 6
Count_one = N - 6*Count_six

# Case 1
if N%6 == 0 : #6으로 딱 떨어지는 경우
    Case_1_price = Count_six*Min_set_price
else:
    Case_1_price = (Count_six+1) * Min_set_price

# Case 2
Case_2_price = Count_six*Min_set_price + Count_one*Min_one_price

# Case 3
Case_3_price = N*Min_one_price

print(min(Case_1_price,Case_2_price,Case_3_price))
