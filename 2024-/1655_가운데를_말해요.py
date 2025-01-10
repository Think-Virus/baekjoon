"""
문제
백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다.
백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다.
만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다.
백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 백준이가 외치는 정수의 개수 N이 주어진다.
N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다.
그 다음 N줄에 걸쳐서 백준이가 외치는 정수가 차례대로 주어진다.
정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

출력
한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력한다.

input
7
1
5
2
10
-99
7
5

출력
1
1
2
2
2
2
5
---
접근법
트리를 사용해야 하지 않나 싶은데
그게 가장 속도가 빠르지 않나 싶음
"""
import math
import sys


def print_mid_value(inputs: list[int]) -> None:
    prev = [inputs[0]]
    print(inputs[0])
    for value in inputs[1:]:
        idx_mid = math.ceil(len(prev) / 2) - 1
        not_added = True
        if value > prev[idx_mid]:
            for j in range(idx_mid, len(prev)):
                if prev[j] > value:
                    prev.insert(j, value)
                    not_added = False
            if not_added:
                prev.append(value)
        else:
            for j in range(idx_mid, 0, -1):
                if prev[j] < value:
                    prev.insert(j, value)
                    not_added = False
            if not_added:
                prev.insert(0, value)
        idx_mid = math.ceil(len(prev) / 2) - 1
        # print(f"idx : {idx_mid}, prev : {prev}")
        print(prev[idx_mid])
    return


def main():
    n = int(sys.stdin.readline())
    inputs = list(int(sys.stdin.readline()) for _ in range(n))
    print_mid_value(inputs)


if __name__ == "__main__":
    main()
