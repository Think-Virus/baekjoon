"""
문제
    자연수 N과 정수 K가 주어졌을 때 이항 계수  binom{N}{K}를 구하는 프로그램을 작성하시오.

이항 계수란?
    주어진 집합에서 원하는 개수만큼 순서 없이 뽑는 조합의 개수
    nCk = nPk / k! = n! / (n-k)! * k!
"""
import sys


def input_data():
    n, k = map(int, input().split())
    return n, k


def solve():
    n, k = input_data()
    dp = [1, 1]

    def combination(n, k):
        result = factorial(n) / (factorial(n - k) * factorial(k))
        return int(result)

    def factorial(n: int) -> int:
        if n < len(dp):
            return dp[n]
        else:
            dp.append(n * factorial(n - 1))
        return dp[n]

    result = combination(n, k)
    print(result)


if __name__ == '__main__':
    solve()
