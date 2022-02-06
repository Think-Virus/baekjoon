# - 고도가 변하는 지점들을 모두 체크하면서, Stack 자료구조를 이용한다.
# - 고도가 같다면 그대로 가면되고, 고도가 낮다면 건물의 개수가 추가되어야 한다.
import sys

class Stack():
    def __init__(self):
        self.stack = [50002]

    def add(self,val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def is_not_empty(self):
        return bool(self.stack)

    def peek(self):
        return self.stack[-1]

    def get(self,idx):
        return self.stack[idx]


N = int(sys.stdin.readline().rstrip())
y_list = []
stack = Stack()
pre_y = 0
building_count = 0
for _ in range(N) :
    y_list.append(int(sys.stdin.readline().rstrip().split()[1]))

for i in range(N) :
    while (stack.is_not_empty() and stack.peek() > y_list[i]) :
        building_count += 1
        stack.pop()

    if (stack.is_not_empty() and stack.peek() == y_list[i]) :
        continue

    stack.add(y_list[i])

print(building_count)


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