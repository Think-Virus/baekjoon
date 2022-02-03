# 1등 코드
import sys
In = sys.stdin.readline

def main():
    n = int(In())
    rope = [0] * 10001 #0으로 가득찬 리스트 생성
    for _ in range(n):
        rope[int(In())] += 1 # 각 로프 숫자에 맞는 인덱스에 +1
    m, s = 0, 0
    for x in range(10000,-1,-1):
        s += rope[x] # 값이 있는 거에서 갯수 +1하는 거
        m = max(m, x * s) # 값이 있는 위치가 로프가 갖고 있는 값임 즉, x가 로프가 갖고 있는 값임 -> 이후에 이전 값하고 max값 비교해서 m으로 돌림
    print(m)
main()

# # 답 참조함...
# N= int(input())
# ropes_list = []
# for _ in range(N) :
#     ropes_list.append(int(input()))
# ropes_list.sort()
# w = 0
# for i in range(len(ropes_list)) :
#     if w < N*ropes_list[i] :
#         w = N*ropes_list[i]
#     N -= 1
# print(w)

# 시간초과
# ropes_list = []
# w_list = []
# for _ in range(N) :
#     ropes_list.append(int(input()))
# ropes_kind = list(set(ropes_list))
# ropes_list.sort()
# for i in ropes_kind :
#     idx = ropes_list.index(i)
#     w_list.append(i*(N-idx))
# print(max(w_list))

# 시간초과
# ropes_list = []
# w=0
# for _ in range(N) :
#     ropes_list.append(int(input()))
# ropes_list.sort(reverse=True)
# for i in ropes_list :
#     count = 0
#     for j in ropes_list :
#         if j < i :
#             break
#         count += 1
#     cal_w = i * count
#     if cal_w < w :
#         break
#     w = cal_w
# print(w)

# 시간초과
# ropes_list = []
# w=0
# for _ in range(N) :
#     ropes_list.append(int(input()))
# ropes_list.sort(reverse=True)
# for i in ropes_list :
#     count = 0
#     for j in ropes_list :
#         if j < i :
#             break
#         count += 1
#     cal_w = i * count
#     if cal_w > w :
#         w = cal_w
# print(w)

# 메모리 초과
# ropes_list = []
# w_list = []
# for i in range(N) :
#     ropes_list.append(int(input()))
# ropes_list.sort()
# def find_w(seq,w_seq) :
#     if seq :
#         w_seq.append(seq[0]*len(seq))
#         find_w(seq[1:],w_seq)
# find_w(ropes_list,w_list)
# print(max(w_list))
