# 가방이 허락하는 무게에 최대한의 가격의 보석을 넣어야 함
import sys
from collections import defaultdict

N, K = map(int,sys.stdin.readline().rstrip().split())
zem_list = []
bag_dict = defaultdict(list)
price_sum = 0

for _ in range(N) :
    zem_list.append(list(map(int,sys.stdin.readline().rstrip().split()))) # 보석 정보 리스트에 저장 0 : 무게 / 1 : 가격
zem_list.sort(key=lambda x:x[1], reverse=True) # 가격 높은 순으로 정렬

for _ in range(K) :
    # 그냥 바로 bag이랑 비교할 경우의 문제점 -> 겁나 큰 가방이 들어왔는데 그냥 1짜리만 델꼬 갈 수 있음
    bag = int(sys.stdin.readline().rstrip())
    idx = 0
    for M, V in zem_list:
        if M <= bag:  # 가방 안에 들어갈 수 있는 무게
            bag_dict[bag].append((M,V)) # 조건을 통과하는 값 저장
        idx += 1

del_list = []
bag_dict = dict(sorted(bag_dict.items()))
for key in bag_dict :
    for del_item in del_list : # 이미 사용한 요소 삭제
        if bag_dict[key].count(del_item) != 0 :
            bag_dict[key].remove(del_item)
    price_sum += bag_dict[key][0][1]
    del_list.append(bag_dict[key][0])

print(price_sum)

