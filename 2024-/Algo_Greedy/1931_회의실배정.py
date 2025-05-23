"""
문제
    한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
    각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
    단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
    회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

입력
    첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다.
    둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
    시작 시간과 끝나는 시간은 2^31-1보다 작거나 같은 자연수 또는 0이다.

출력
    첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
---
접근
    어떤 식으로 선택해야 할까?
    1 4
    2 10
    3 4
    4 7
    1. 시작 시간이 빠른 순으로 (1,4) (4, 7)
    2. 종료 시간이 빠른 순으로 (1,4)
    3. 소요 시간이 가장 작은 순으로 (3,4) (4,7)
        -> 이것이 맞을 것 같음
        -> 아니었음
        반례 :
            1 2
            1 3
            4 6
            5 6
            9 10
            7 9
            10 10
            3
            but 최대 4개까지 가능함
    ---
    How?
        - 각 시간 별로 cell을 만들어서 한다? -> 메모리 초과 일어날 것
        - 짧은 순으로 계속 해서 비교한다? -> N^2가 되는데.. 입력 크기가 10^5니까.. 결국 10^10이 돼서 안된다고 봐야할 듯 (10^8~10^9까지 가능)
        - 사이에 있는 값들을 제거 하는 식으로 가도... filter로 하면 결국은 N^2로 될라나 ㅇㅇ



"""
import sys


def solve():
    n = int(sys.stdin.readline())
    meetings = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: (x[1], -x[0]))
    end = meetings[0][1]
    cnt = 1
    for meeting in meetings[1:]:
        if end <= meeting[0]:
            end = meeting[1]
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    solve()
