"""
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	42039	13651	9943	33.429%

문제
    우리는 스마트폰을 사용하면서 여러 가지 앱(App)을 실행하게 된다. 대개의 경우 화면에 보이는 ‘실행 중’인 앱은 하나뿐이지만 보이지 않는 상태로 많은 앱이 '활성화'되어 있다.
    앱들이 활성화 되어 있다는 것은 화면에 보이지 않더라도 메인 메모리에 직전의 상태가 기록되어 있는 것을 말한다.
    현재 실행 중이 아니더라도 이렇게 메모리에 남겨두는 이유는 사용자가 이전에 실행하던 앱을 다시 불러올 때에 직전의 상태를 메인 메모리로부터 읽어 들여 실행 준비를 빠르게 마치기 위해서이다.
    하지만 스마트폰의 메모리는 제한적이기 때문에 한번이라도 실행했던 모든 앱을 활성화된 채로 메인 메모리에 남겨두다 보면 메모리 부족 상태가 오기 쉽다.
    새로운 앱을 실행시키기 위해 필요한 메모리가 부족해지면 스마트폰의 운영체제는 활성화 되어 있는 앱들 중 몇 개를 선택하여 메모리로부터 삭제하는 수밖에 없다.
    이러한 과정을 앱의 ‘비활성화’라고 한다.
    메모리 부족 상황에서 활성화 되어 있는 앱들을 무작위로 필요한 메모리만큼 비활성화 하는 것은 좋은 방법이 아니다.
    비활성화된 앱들을 재실행할 경우 그만큼 시간이 더 필요하기 때문이다. 여러분은 이러한 앱의 비활성화 문제를 스마트하게 해결하기 위한 프로그램을 작성해야 한다
    현재 N개의 앱, A1, ..., AN이 활성화 되어 있다고 가정하자. 이들 앱 Ai는 각각 mi 바이트만큼의 메모리를 사용하고 있다.
    또한, 앱 Ai를 비활성화한 후에 다시 실행하고자 할 경우, 추가적으로 들어가는 비용(시간 등)을 수치화 한 것을 ci 라고 하자.
    이러한 상황에서 사용자가 새로운 앱 B를 실행하고자 하여, 추가로 M 바이트의 메모리가 필요하다고 하자.
    즉, 현재 활성화 되어 있는 앱 A1, ..., AN 중에서 몇 개를 비활성화 하여 M 바이트 이상의 메모리를 추가로 확보해야 하는 것이다.
    여러분은 그 중에서 비활성화 했을 경우의 비용 ci의 합을 최소화하여 필요한 메모리 M 바이트를 확보하는 방법을 찾아야 한다.

입력
    입력은 3줄로 이루어져 있다. 첫 줄에는 정수 N과 M이 공백문자로 구분되어 주어지며,
    둘째 줄과 셋째 줄에는 각각 N개의 정수가 공백문자로 구분되어 주어진다.
    둘째 줄의 N개의 정수는 현재 활성화 되어 있는 앱 A1, ..., AN이 사용 중인 메모리의 바이트 수인 m1, ..., mN을 의미하며,
    셋째 줄의 정수는 각 앱을 비활성화 했을 경우의 비용 c1, ..., cN을 의미한다
    단, 1 ≤ N ≤ 100, 1 ≤ M ≤ 10,000,000이며, 1 ≤ m1, ..., mN ≤ 10,000,000을 만족한다.
    또한, 0 ≤ c1, ..., cN ≤ 100이고, M ≤ m1 + m2 + ... + mN이다.

출력
    필요한 메모리 M 바이트를 확보하기 위한 앱 비활성화의 최소의 비용을 계산하여 한 줄에 출력해야 한다.
---
접근 방법 자체가 틀리진 않았지만, 부족했음
---
정답 참조
https://wooono.tistory.com/603
"""
import sys


def input_data():
    n, goal_reduce_memory = map(int, sys.stdin.readline().split())
    memories = [0] + list(map(int, sys.stdin.readline().split()))
    costs = [0] + list(map(int, sys.stdin.readline().split()))

    return n, goal_reduce_memory, memories, costs


def solve(n, goal_reduce_memory, memories, costs):
    dp = [[0] * (sum(costs) + 1) for i in range(n + 1)]
    result = sum(costs)

    for i in range(1, n + 1):
        curr_memory = memories[i]
        curr_cost = costs[i]
        for j in range(sum(costs) + 1):
            if j < curr_cost:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - curr_cost] + curr_memory)
                if dp[i][j] >= goal_reduce_memory:
                    result = min(result, j)

    print(result)


if __name__ == '__main__':
    n, goal_reduce_memory, memories, costs = input_data()
    solve(n, goal_reduce_memory, memories, costs)
