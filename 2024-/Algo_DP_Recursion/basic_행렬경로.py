"""
문제 : n x n 행렬
    - 왼쪽 위에서 시작해 한 칸씩 이동하면서 오른쪽 아래까지 도달하는 경로
    - (1,1) -> (n,n) 경로 중 가장 높은 값
    - 경로의 합 : 방문한 카에 있는 수들을 더한 값
    - 이동 규칙
        - 오른쪽이나 아래쪽으로만 이동 가능함
        - 외쪽, 위쪽, 대각선 이동은 허용하지 않음

접근 :
    c_ij에 접근하는 방법은 둘 뿐임
        1. c_(i-1)j에서 오른쪽으로 접근 ->
        2. c_i(j-1)에서 아래로 접근 ↓
    즉, c_ij = matrix[i,j] + max(c_(i-1)j, c_i(j-1))
"""
import random
import time

# N = 4
# MATRIX = [
#     [6, 7, 12, 5],
#     [5, 3, 11, 18],
#     [7, 17, 3, 3],
#     [8, 10, 14, 9],
# ]

N = 5
MATRIX = [[random.randint(0, 50) for _ in range(N)] for _ in range(N)]

"""
# 재귀적 접근
    c_ij = matrix[i,j] + max(c_(i-1)j,c_i(j-1))
    위에서 c_(i-1)j와 c_i(j-1)을 매번 함수를 호출해서 확인함
"""


def findPathRecursion(x, y) -> int:
    if x == -1 or y == -1:
        return 0
    right_access_points = findPathRecursion(x - 1, y)
    down_access_points = findPathRecursion(x, y - 1)
    return MATRIX[x][y] + (right_access_points if right_access_points > down_access_points else down_access_points)


"""
# 동적프로그래밍
    c_ij = matrix[i,j] + max(c_(i-1)j,c_i(j-1))
    위에서 c_(i-1)j와 c_i(j-1)을 미리 저장해놓고 찾아오는 방식
"""


def findPathDynamic() -> int:
    path_matrix = [[0 for w in range(N + 1)] for h in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            path_matrix[i][j] = MATRIX[i - 1][j - 1] + max(path_matrix[i - 1][j], path_matrix[i][j - 1])

    return path_matrix[-1][-1]


def main():
    print("start")
    start = time.time()
    print(f"Recursion \n결과 : {findPathRecursion(N - 1, N - 1)}\n실행 시간 : {time.time() - start:.4f}")
    start = time.time()
    print(f"Dynamic \n결과 : {findPathDynamic()}\n실행 시간 : {time.time() - start:.4f}")


if __name__ == '__main__':
    main()
