N = int(input())
time_list = []
result = 0
# 답 보고 확인한 코드
for i in range(N) :
    time_list.append(list(map(int, input().split(" "))))
time_list.sort(key=lambda x:(x[1],x[0]))

cnt = 1
end_time = time_list[0][1]
for i in range(1, N):
    if time_list[i][0] >= end_time:
        cnt += 1
        end_time = time_list[i][1]
print(cnt)

#출처: https://suri78.tistory.com/26 [공부노트]

# 시도했으나 정리하지 못한 코드
# while time_list :
#     print()
#     print(time_list)
#     print("____________________________")
#     tmp_list =copy.deepcopy(time_list)
#     for k in tmp_list :
#         for j in tmp_list :
#             print(tmp_list)
#             print(j)
#             print(tmp_list.index(j))
#             if j[0] < k[1] and j != k :
#                 del tmp_list[tmp_list.index(j)]
#     if len(tmp_list) > result :
#         result = len(tmp_list)
#     print(tmp_list)
#     time_list = time_list[1:]
# print(result)
#
#
#
#     _count = 1
#     for _ in range(length_time) :
#          max_value =
#          if var_pass > length_time :
#              break
#          for k in time_list[var_pass+1:] :
#                  var_pass += 1
#                  if k[0] >= time_list[var_pass][1] :
#                          _count += 1
#                          break
#     result_list.append(_count)
#
#
# print(max(result_list))

# 시간 오버
# while time_list :
#     length_time = len(time_list)
#     var_pass = 0
#     _count = 1
#     for j in range(length_time) :
#          j = var_pass
#          if j > length_time :
#              break
#          for k in time_list[j+1:] :
#                  var_pass += 1
#                  if k[0] >= time_list[j][1] :
#                          _count += 1
#                          break
#     result_list.append(_count)
#     time_list = time_list[1:]
# print(max(result_list))

# 접근 방식 자체가 틀림
# time_list.sort(key = lambda x:x[2])
# print(time_list)
# var_end = time_list[0][1]
# length_list = len(time_list)
# while length_list -1 :
#     for j in range(length_list-1) :
#         if var_end <= time_list[j+1][0] :
#             var_end = time_list[j+1][1]
#             length_list -= 1
#             result_list.append(time_list.pop(j))
#             break
#
# print(result_list)

