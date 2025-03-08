"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
3 초	512 MB	13115	3111	2080	23.655%
문제
    상근이는 선영이와 걸어가다가 사탕 가게를 지나가게 되었다. 갑자기 상근이는 선영이에게 사탕이 얼마나 건강에 안 좋은지 설명하기 시작했다.
    선영이는 매우 짜증이 났고, 상근이에게 누가 더 건강이 안 좋아질 수 있는지 내기를 하자고 했다. 상근이는 내기를 그 즉시 받아들였다.
    두 사람은 같은 돈을 가지고 가게에 들어가서 사탕을 산다. 이때, 구매한 사탕의 칼로리가 더 큰 사람이 내기에서 이기게 된다.
    상근이는 잠시 화장실에 갔다온다고 핑계를 댄 뒤에, 노트북을 열고 사탕 가게의 시스템을 해킹하기 시작했다.
    이 시스템에는 현재 사탕 가게에 있는 사탕의 가격과 칼로리가 모두 등재되어 있다. 각 사탕의 개수는 매우 많기 때문에, 원하는 만큼 사탕을 구매할 수 있다.
    또, 사탕은 쪼갤 수 없기 때문에, 일부만 구매할 수 없다.
    사탕 가게에 있는 모든 사탕의 가격과 칼로리가 주어졌을 때, 어떻게 하면 칼로리의 합이 가장 크게 되는지를 구하는 프로그램을 작성하시오.

입력
    각 테스트 케이스의 첫째 줄에는 가게에 있는 사탕 종류의 수 n과 상근이가 가지고 있는 돈의 양 m이 주어진다. (1 ≤ n ≤ 5,000, 0.01 ≤ m ≤ 100.00)
    m은 항상 소수점 둘째자리까지 주어진다.
    다음 n개 줄에는 각 사탕의 칼로리 c와 가격 p가 주어진다. (1 ≤ c ≤ 5,000, 0.01 ≤ p ≤ 100.00)
    c는 항상 정수, p는 항상 소수점 둘째자리이다.입력의 마지막 줄에는 '0 0.00'이 주어진다.

출력
    각 테스트 케이스에 대해서, 상근이가 돈 m을 가지고 구매할 수 있는 가장 높은 칼로리를 출력한다.

2 8.00
700 7.00
199 2.00
3 8.00
700 7.00
299 3.00
499 5.00
0 0.00

Python3 -> 시간 초과
PyPy3 -> 틀림 -> 부동 소수점 처리가 문제일 것으로 추측됨
"""
import sys


def input_data():
    test_cases = []
    n, price_limit = map(float, sys.stdin.readline().split())

    while price_limit != 0.00:
        candy_infos = []
        for _ in range(round(n)):
            calorie, price = map(float, sys.stdin.readline().split())
            calorie = round(calorie)
            price = round(price * 100)
            candy_infos.append((calorie, price))

        test_cases.append([round(n), round(price_limit * 100), candy_infos])
        n, price_limit = map(float, sys.stdin.readline().split())

    return test_cases


def solve(test_cases):
    for n, price_limit, candy_infos in test_cases:
        dp = [0] * (price_limit + 1)

        for calorie, price in candy_infos:
            for i in range(price, price_limit + 1):
                dp[i] = max(dp[i], dp[i - price] + calorie)

        print(max(dp))


if __name__ == "__main__":
    test_cases = input_data()
    solve(test_cases)
