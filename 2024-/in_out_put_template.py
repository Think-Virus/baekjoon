# 공백을 기준으로 구분된 데이터를 입력 받을 떄
data = list(map(int, input().split()))

# 공백을 기준으로 구분된 데이터가 많지 않다면 
a, b, c = map(int, input().split())

# 빠른 입력
import sys

# 공백으로 구분된 2개 숫자 입력 받기
N, M = map(int, sys.stdin.readline().split())

# 2차원 리스트 입력 받기
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()

# 출력
answer = 5
print(f"정답은 {answer} 입니다.")

result = [1, 2, 3]

# 기본적인 리스트 출력시
print(result)
# [1,2,3]

# for loop으로 원소를 하나씩 출력
for i in range(len(result)):
    print(result[i], end=' ')
# 1 2 3

# 리스트의 원소를 언패킹 시켜서 출력
print(*result)
# 1 2 3

# N x M 리스트 초기화 ex) 해당 좌표에 방문 체크하는 배열
# 입력
"""
5 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
"""

m = 3
n = 2
visited = [[False]*m for _ in range(n)]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]