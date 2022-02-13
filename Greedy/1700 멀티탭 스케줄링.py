# 1. 이후에 사용할 콘센트는 최대한 그대로 놓는 게 좋음
# 2. 처음에 꽂혀 있어야 하는 항목들은 바로 분류
# 3. 꽂혀있는 항목들의 count 실행
from collections import deque

"""
2 7
2 3 2 3 1 2 7
"""

import sys
N, K = map(int, sys.stdin.readline().split())  # ex) 2 7
Result = 0

def Check_common(seq1,seq2):
    diff = list(seq1-seq2) # 다시 사용하지 않는 제품 확인
    if diff :
        return diff[0]
    else :
        return False

Order_list = list(map(int,sys.stdin.readline().split()))
Power_socket_list = Order_list[:N]
Order_list = deque(Order_list[N:]) # deque 자료형으로 변환

for _ in range(K-N):
    Product = Order_list.popleft()

    if Product in Power_socket_list : # 이미 꽂혀있는 경우
        continue
    else : # 다시 꽂힐 일이 없는 프로덕트 확인
        tmp = Check_common(set(Power_socket_list), {Product}|set(Order_list))
        if tmp : # 다시 꽂힐 일이 없는 제품이 있을 경우 (제품 번호는 0은 없기 때문에 그냥 이렇게 적어도 괜찮음)
            Power_socket_list.remove(tmp) # 이미 꽂혀있는 제품 중 가장 마지막에 사용하는 제품 제거
            Power_socket_list.append(Product) # 새로운 제품 꽂기
            Result += 1
        else: # 다시 꽂힐 일이 있는 제품의 경우
            tmp_max = (Power_socket_list[0],Order_list.index(Power_socket_list[0]))
            for i in Power_socket_list[1:] : # 가장 마지막에 사용하는 제품 확인
                if tmp_max[1] < Order_list.index(i) :
                    tmp_max = (i,Order_list.index(i))
            Power_socket_list.remove(tmp_max[0]) # 이미 꽂혀있는 제품 중 가장 마지막에 사용하는 제품 제거
            Power_socket_list.append(Product) # 새로운 제품 꽂기
            Result += 1
print(Result)



# from collections import defaultdict
#
# N, K = map(int, sys.stdin.readline().split())  # ex) 2 7
# Order_dict = defaultdict(list)
# Power_socket_list = []
# idx = 0
#
# for i in sys.stdin.readline().split() :
#     if idx >= N :
#         Order_dict[int(i)].append(idx)
#     else:
#         Power_socket_list.append(int(i)) # 콘센트 리스트 -> 최대 크기는 N으로
#     idx += 1
#
# print(Power_socket_list)
# print(Order_dict)
#
# print(max(list(Order_dict.values()), key= lambda x : Order_dict.get(tuple(x)) in Power_socket_list))
# for Key in Order_dict.keys() :
#     if Key in Power_socket_list : # 이미 소켓에 꽂혀 있을 경우
#         continue
#     else :
#         max_order = max()