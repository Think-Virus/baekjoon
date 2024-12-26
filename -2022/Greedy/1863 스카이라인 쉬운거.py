# 답 확인..
# y가 변하는 지점들을 확인하면서 stack에 넣거나 뺀다.
# y가 같다면 stack에 넣지 않고, stack의 top보다 작으면 건물의 개수(answer)를 1씩 증가시킨다.
# 마지막으로 stack에 남아 있는 값들을 꺼내면서 0보다 크면 건물의 개수를 1씩 증가시킨다.
import sys

input = sys.stdin.readline # 이런 식으로 input값을 넣을 수 있구나..

n = int(input().rstrip())

stack = []
answer = 0

for _ in range(n):
    y = int(input().rstrip().split()[1])
    while len(stack)>0 and stack[-1] >y: # y의 값이 작아졌으므로 +1하고 그 건물은 확인된 것이니 pop으로 제거 -> 마지막까지 확인
        answer+=1
        stack.pop()
    if len(stack)>0 and stack[-1] == y: # y가 같다면 결국 같은 건물이므로 그냥 continue
        continue
    stack.append(y)

while len(stack)>0:
    if stack[-1] >0: # 마지막으로 stack에 남음 건물 확인해서 0보다 클 경우에는 건물이 있다는 거니까.. 바로 확인
        answer+=1
    stack.pop()

print(answer)


# 낮아졌을 때 +1하는 방식을 사용했는데, 틀림.. 왜지???? -> 높이가 3,2,4,3인 값이 들어오면 출력은 3이나오는데 답은 4임 -> 중간에 있는 2가 씹힘..
# import sys
#
# N = int(sys.stdin.readline().rstrip())
# y_list = []
# pre_y = 0
# building_count = 0
# for i in range(N) :
#     y_list.append(int(sys.stdin.readline().rstrip().split()[1]))
# y_list.append(0) #끝
# for y in y_list :
#     if y < pre_y:
#         building_count += 1
#     pre_y = y
# print(building_count)

# set을 이용하는 방식은 212->이런 식으로 있을 때 2를 하나만 세서 안됨
# import sys
#
# N = int(sys.stdin.readline().rstrip())
# y_list = []
# idx_0_list = []
# pre_y = 0
# building_count = 0
# for i in range(N) :
#     y_list.append(int(sys.stdin.readline().rstrip().split()[1]))
#     if y_list[i] == 0 :
#         idx_0_list.append(i)
#
# # 건물 나누기
# pre_zero_position = 0
# for zero_position in idx_0_list :
#     building_group = y_list[pre_zero_position:zero_position]
#     pre_zero_position = zero_position+1
#     building_count += len(set(building_group))
#
# building_group = y_list[pre_zero_position:]
# building_count += len(set(building_group))
# print(building_count)


# 그냥 이렇게 했을 때의 문제는 3,2,1 -> 이런 순서일 때, 파악을 못함. 이걸 해결해야 함
# for y in y_list :
#     if y > pre_y:
#         building_count += 1
#     pre_y = y
# print(building_count)

# 건물 나눠서 하는 거 하려그랬는데, 아닌 거 같은데..
# N = int(sys.stdin.readline().rstrip())
# position_list = []
# idx_0_list = []
# building_count = 0
# pre_y = 0
# for i in range(N) :
#     position_list.append(sys.stdin.readline().rstrip().split())
#     if position_list[i][1] == '0' :
#         idx_0_list.append(i)
#
# # 건물 나누기
# pre_zero_position = 0
# for zero_position in idx_0_list :
#     building_group = position_list[pre_zero_position:zero_position]
#     pre_zero_position = zero_position+1
#
#     #building_group.sort(key=lambda x: x[1])
#     print(building_group)
#
#     for tmp_x,tmp_y in building_group :
#         if tmp_y in tmp_y_list :
# building_group = position_list[pre_zero_position:]
# print(building_group)

#각 건물 높이 별 범위를 구해야 할듯

# 1차 시도 -> 틀림
# import sys
#
# N = int(sys.stdin.readline().rstrip())
# y_set = set([])
# building_count = 0
# for _ in range(N) :
#     tmp_x,tmp_y = map(int,sys.stdin.readline().rstrip().split())
#     if not tmp_y :
#         building_count += len(y_set)
#         y_set = set([])
#         continue
#     y_set.add(tmp_y)
# building_count += len(y_set)
# print(building_count)