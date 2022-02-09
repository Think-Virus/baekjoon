# 가방이 허락하는 무게에 최대한의 가격의 보석을 넣어야 함
import sys

N, K = map(int,sys.stdin.readline().rstrip().split())
zem_list = []
bag_list = []
price_sum = 0

for _ in range(N) :
    zem_list.append(list(map(int,sys.stdin.readline().rstrip().split()))) # 보석 정보 리스트에 저장 0 : 무게 / 1 : 가격
zem_list.sort(key=lambda x:x[1], reverse=True) # 가격 높은 순으로 정렬

for _ in range(K) :
    bag_list.append(int(sys.stdin.readline().rstrip()))

bag_list.sort() # 최대 무게 낮은 순으로 정렬
for bag in bag_list :
    idx = 0
    for M, V in zem_list:
        if M <= bag:  # 가방 안에 들어갈 수 있는 무게
            price_sum += V
            del zem_list[idx] #가방에 보석을 담았으니, 해당 보석은 제외
            break
        idx += 1
print(price_sum)

