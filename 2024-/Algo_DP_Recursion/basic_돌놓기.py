"""
- 3 x n 테이블에 각 숫자가 적혀있다
- 제한 조건을 만족하는 방법으로 돌을 놓아 돌이 놓인 곳의 수의 합을 최대로 한다
- 제한 조건
    - 가로나 세로에 인접한 두 칸에 동시에 돌이 놓일 수 없다
    - 각 열에는 적어도 하나 이상의 돌을 놓는다

접근 방법
    한 열에 돌을 놓을 수 있는 방법
        Type 1. 1
                0
                0
                ---
        Type 2. 0
                1
                0
                ---
        Type 3. 0
                0
                1
                ---
        Type 4. 1
                0
                1
                ---
    각 타입에 따라 이전에 올 수 있는 타입이 다름
    Type 1 : Type 2, Type 3 가능
    Type 2 : Type 4 가능
    Type 3 : Type 1, Type 2 가능
    Type 4 : Type 2 가능

결론
    c_ip : i열이 패턴 p로 놓일 때, 최고 점수
    w_ip : i열이 패턴 p로 놓일 때, i열에 돌이 놓인 곳의 점수의 합

    c_ip =
        • w_1p if i = 1
        • w_ip + max(c_(i-1)q) if i > 1 [q는 p일 경우 이전에 가능한 타입들]
"""
import random
import time
from enum import Enum, auto

N = 100
# MATRIX = [
#     [6, 7, 12, -5, 5, 3, 11, 3],
#     [-8, 10, 14, 9, 7, 13, 8, 5],
#     [11, 12, 7, 4, 8, -2, 9, 4],
# ]

MATRIX = [[random.randint(-100,100) for _ in range(N)] for _ in range(3)]

class PType(Enum):
    P1 = auto()
    P2 = auto()
    P3 = auto()
    P4 = auto()


def getValuePType(i, ptype):
    if ptype == PType.P1:
        return MATRIX[0][i]
    elif ptype == PType.P2:
        return MATRIX[1][i]
    elif ptype == PType.P3:
        return MATRIX[2][i]
    elif ptype == PType.P4:
        return MATRIX[0][i] + MATRIX[2][i]


# Recursion
def pebbleRecursion():
    max_var = float('-inf')
    for p in PType:
        tmp = _pebbleRecursion(N - 1, p)
        max_var = max(max_var, tmp)
    return max_var


def _pebbleRecursion(i, current_p) -> int:
    if i == 0:
        return getValuePType(i, current_p)
    else:
        if current_p == PType.P1:
            return getValuePType(i, current_p) + max(_pebbleRecursion(i - 1, PType.P2), _pebbleRecursion(i - 1, PType.P3))
        elif current_p == PType.P2:
            return getValuePType(i, current_p) + _pebbleRecursion(i - 1, PType.P4)
        elif current_p == PType.P3:
            return getValuePType(i, current_p) + max(_pebbleRecursion(i - 1, PType.P1), _pebbleRecursion(i - 1, PType.P2))
        elif current_p == PType.P4:
            return getValuePType(i, current_p) + _pebbleRecursion(i - 1, PType.P2)


# Dynamic
"""
    c_ip =
        • w_1p if i = 1
        • w_ip + max(c_(i-1)q) if i > 1 [q는 p일 경우 이전에 가능한 타입들]
    c_(i-1)q를 저장하고 불러오는 방식
"""


def pebbleDynamic():
    pebble_matrix = [
        [0] * (N + 1) for _ in range(4)
    ]

    for i in range(1, N + 1):
        pebble_matrix[0][i] = getValuePType(i - 1, PType.P1) + max(pebble_matrix[1][i - 1], pebble_matrix[2][i - 1])
        pebble_matrix[1][i] = getValuePType(i - 1, PType.P2) + pebble_matrix[3][i - 1]
        pebble_matrix[2][i] = getValuePType(i - 1, PType.P3) + max(pebble_matrix[0][i - 1], pebble_matrix[1][i - 1])
        pebble_matrix[3][i] = getValuePType(i - 1, PType.P4) + pebble_matrix[1][i - 1]

    return max([pebble_matrix[j][N] for j in range(4)])

start = time.time()
print(f"Recursion : (결과){pebbleRecursion()} (소요 시간){time.time()-start:0.6f}")
start = time.time()
print(f"Dynamic : (결과){pebbleDynamic()} (소요 시간){time.time()-start:0.6f}")
