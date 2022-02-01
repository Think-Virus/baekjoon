# 답 코드 -> 내 거랑 로직은 같은데 차이가 뭘까?
import sys

T = int(input())  # 테스트케이스

for i in range(0, T):
    Cnt = 1
    people = []

    N = int(input())
    for i in range(N):
        Paper, Interview = map(int, sys.stdin.readline().split())
        people.append([Paper, Interview])

    people.sort()  # 서류 기준 오름차순 정렬
    Max = people[0][1]

    for i in range(1, N):
        if Max > people[i][1]:
            Cnt += 1
            Max = people[i][1]

    print(Cnt)

# 틀림
import sys
T = int(input())
for _ in range(0,T) :
    N = int(input())
    score_list = []
    result = 1
    for _ in range(N) :
        score_list.append(list(map(int,sys.stdin.readline().split())))
    score_list.sort()
    val_1 = score_list[0][1]
    for i in range(1,N):
        if score_list[i][1] < val_1 :
            val_1 = score_list[i][1]
            result += 1
print(result)



# 틀림
# import sys
# T = int(input()) #케이스 개수
# for _ in range(T) :
#     N = int(input())  # 지원자 숫자
#     score_list = []
#     result = 0
#     for _ in range(N) :
#         score_list.append(tuple(map(int,sys.stdin.readline().split()))) # 튜플을 사용하면 리스트에 비히 더 메모리 용량을 아끼고 퍼포먼스를 향상시키는데 도움이 됨
#     score_list.sort()
#     val_1 = score_list[0][1]
#     for i in range(N):
#         if score_list[i][1] <= val_1 :
#             val_1 = score_list[i][1]
#             result += 1
# print(result)

# 시간 초과
# import sys
# T = int(input()) #케이스 개수
# for _ in range(T) :
#     N = int(input())  # 지원자 숫자
#     score_list = []
#     count = 0
#     for _ in range(N) :
#         score_list.append(tuple(map(int,sys.stdin.readline().split()))) # 튜플을 사용하면 리스트에 비히 더 메모리 용량을 아끼고 퍼포먼스를 향상시키는데 도움이 됨
#     score_list.sort()
#     for i in range(1,N) :
#         for j in range(i,-1,-1) :
#             if score_list[j][1]<score_list[i][1] :
#                 count += 1
#                 break
#     print(N - count)