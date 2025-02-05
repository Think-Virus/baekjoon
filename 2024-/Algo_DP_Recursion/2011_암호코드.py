"""
문제
    상근이와 선영이가 다른 사람들이 남매간의 대화를 듣는 것을 방지하기 위해서 대화를 서로 암호화 하기로 했다. 그래서 다음과 같은 대화를 했다.
    상근: 그냥 간단히 암호화 하자. A를 1이라고 하고, B는 2로, 그리고 Z는 26으로 하는거야.
    선영: 그럼 안돼. 만약, "BEAN"을 암호화하면 25114가 나오는데, 이걸 다시 글자로 바꾸는 방법은 여러 가지가 있어.
    상근: 그렇네. 25114를 다시 영어로 바꾸면, "BEAAD", "YAAD", "YAN", "YKD", "BEKD", "BEAN" 총 6가지가 나오는데,
        BEAN이 맞는 단어라는건 쉽게 알수 있잖아?
    선영: 예가 적절하지 않았네 ㅠㅠ 만약 내가 500자리 글자를 암호화 했다고 해봐.
        그 때는 나올 수 있는 해석이 정말 많은데, 그걸 언제 다해봐?
    상근: 얼마나 많은데?
    선영: 구해보자!
    어떤 암호가 주어졌을 때, 그 암호의 해석이 몇 가지가 나올 수 있는지 구하는 프로그램을 작성하시오.

입력
    첫째 줄에 5000자리 이하의 암호가 주어진다. 암호는 숫자로 이루어져 있다.

출력
    나올 수 있는 해석의 가짓수를 구하시오. 정답이 매우 클 수 있으므로, 1000000으로 나눈 나머지를 출력한다.
    암호가 잘못되어 암호를 해석할 수 없는 경우에는 0을 출력한다.
---
접근법
    ex) 11
    Type 1. 뒤에 숫자가 그냥 붙기 1 1
    Type 2. 이전 숫자와 합쳐지기 11
    
    dp[0][i] = dp[0][i - 1] + dp[1][i - 1]
    dp[1][i] = dp[0][i - 1] if cord[i - 1] * 10 + cord[i] <= 26 else 0
    ---
    Type 1에서 0인 경우를 제거하면 00인 경우도 안 생길 것
    100이 들어올 경우, 암호가 잘못되어 해석할 수 없음
    -> dp[0][i] dp[1][i] 모두 0이라면 break 후 0 출력
"""


def input_data():
    input_cord = input()
    if input_cord[0] == "-" or input_cord[0] == "0":
        return 0, []

    cord = [int(i) for i in input_cord]
    n = len(cord)
    return n, cord


def solve():
    n, cord = input_data()

    if n == 0 or n == 1:
        print(n)
        return

    def make_df(n, cord):
        dp = [[0 for _ in range(n)] for _ in range(2)]
        dp[0][0] = 1

        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + dp[1][i - 1] if cord[i] != 0 else 0
            dp[1][i] = dp[0][i - 1] if 0 < cord[i - 1] * 10 + cord[i] <= 26 else 0
        return dp

    dp = make_df(n, cord)
    print((dp[0][-1] + dp[1][-1]) % 1000000)


if __name__ == '__main__':
    while True:
        solve()
