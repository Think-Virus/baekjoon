# 항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 모든 크레인은 동시에 움직인다!
# 각 크레인은 무게 제한이 있다. 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성

"""
작은 것부터 들었을 때의 로직 반례
3
6 8 9
9
1 2 3 4 5 6 7 8 9
-> 내림차순으로 도전
"""

"""
정답 코드 확인
무거운 화물을 들 수 있는 크레인에게 무거운 화물을 옮기게 하자! 만 기억하면 쉽게 풀리는 문제. 
무게 제한이 높은 크레인에게 현재 남아 있는 화물 중 가장 무거운 것을 들게 해야 모든 박스를 옮기는 최소 시간이 나온다.
"""
import sys
N = int(input())
Crane_list = map(int, sys.stdin.readline().split()) # 크레인 별 무게 제한
M = int(input())
Box_list = map(int, sys.stdin.readline().split()) # 화물 별 무게

# 무게 제한과 화물 무게 전부 내림차순으로 정렬
Crane_list = sorted(Crane_list, reverse=True)
Box_list = sorted(Box_list, reverse=True)

# 무게 제한이 제일 높은 크레인도 제일 무거운 화물을 들 수 없는 경우
if Box_list[0] > Crane_list[0] :
    print(-1)
    exit()

answer = 0
# 화물이 전부 옮겨질 때까지
while len(Box_list) > 0:
    answer += 1
    # 무게제한을 돌면서 옮길 수 있는 화물을 옮김
    for l in Crane_list:
        for j in range(len(Box_list)):
            if l >= Box_list[j]: # 화물을 옮길 수 있으면
                del Box_list[j]
                break
print(answer)