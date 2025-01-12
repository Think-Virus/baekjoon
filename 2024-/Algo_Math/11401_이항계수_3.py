"""
문제
    자연수 N과 정수 K가 주어졌을 때 이항 계수  binom{N}{K}를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

"""
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
        if n > len(dp):
            for i in range(len(dp), n + 1):
                dp.append(i*dp[i-1])
        return dp[n]

    combi = combination(n, k)
    result = combi % 1000000007
    print(result)


if __name__ == '__main__':
    solve()
