# 파이프에서 물이 새는 곳은 신기하게도 가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샌다
# 길이가 L인 테이프를 무한개 가지고 있다.
# 항승이는 테이프를 이용해서 물을 막으려고 한다. 항승이는 항상 물을 막을 때, 적어도 그 위치의 좌우 0.5만큼 간격을 줘야 물이 다시는 안 샌다고 생각한다.
# 물이 새는 곳의 위치와, 항승이가 가지고 있는 테이프의 길이 L이 주어졌을 때, 항승이가 필요한 테이프의 최소 개수를 구하는 프로그램을 작성
# 테이프를 겹쳐서 붙이는 것도 가능
# 물이 새는 곳의 개수 N과 테이프의 길이 L

# Case 1 : 1개의 구멍만 막는 경우
# Case 2 : L의 길이가 길어서 인접한 2개의 구멍을 막는 경우
import sys

N,L = map(int,sys.stdin.readline().split())
Position_list = list(map(int,sys.stdin.readline().split()))
Position_list.sort()

tmp_sum = 0  # tmp_sum 초기화
Start_idx = 0
End_idx = 0
Cnt = 0
while len(Position_list) > 1 :
    End_idx += 1
    if End_idx == len(Position_list) :
        break
    tmp_sum = Position_list[End_idx]-Position_list[Start_idx]+1
    if tmp_sum > L:  # Case 1
        Cnt += 1
        del Position_list[Start_idx:End_idx]
        Start_idx,End_idx = 0,0
        tmp_sum = 0
    else: # Case 2
        continue
if Position_list :
    Cnt += 1
print(Cnt)
