# N개의 강의가 있다. 우리는 모든 강의의 시작하는 시간과 끝나는 시간을 알고 있다.
# 이때, 우리는 최대한 적은 수의 강의실을 사용하여 모든 강의가 이루어지게 하고 싶다.
# 물론, 한 강의실에서는 동시에 2개 이상의 강의를 진행할 수 없고, 한 강의의 종료시간과 다른 강의의 시작시간이 겹치는 것은 상관없다.
# 필요한 최소 강의실의 수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 강의의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N개의 줄에 걸쳐 각 줄마다 세 개의 정수가 주어지는데,
# 순서대로 강의 번호, 강의 시작 시간, 강의 종료 시간을 의미한다. 강의 번호는 1부터 N까지 붙어 있으며, 입력에서 꼭 순서대로 주어지지 않을 수 있으나 한 번씩만 주어진다.
# 강의 시작 시간과 강의 종료 시간은 0 이상 10억 이하의 정수이고, 시작 시간은 종료 시간보다 작다.

"""
정답 코드 확인
두개의 heapq를 사용하여 풀이했다.
먼저 강의 정보를 입력받으면서 heapq를 사용하여 강의 시작시간을 기준으로 오름차순 정렬한다.
그리고 강의 시작시간이 빠른 순서대로 강의실을 배정한다.
배정된 강의는 table 리스트에 저장하며,
heapq를 사용하여 강의 종료시간을 기준으로 오름차순으로 정렬하며 현재 배정된 강의실 중
강의가 가장 빨리 끝나는 강의의 종료시간과 강의실을 배정할 강의의 시작시간을 비교하여
배정할 강의의 시작시간이 종료시간보다 크거나 같다면 해당 강의실을 이용할 수 있기 때문에 table에 추가하고, 종료된 강의는 table에서 제거한다.
만약 배정할 강의의 시작시간이 종료시간보다 작다면 추가로 강의실을 배정해야 하기 때문에 배정할 강의를 table리스트에 추가한다.
n개의 강의만큼 반복하면 table리스트의 길이는 강의에 필요한 최소 강의실 수가 된다.
"""
import sys
import heapq

input = sys.stdin.readline
pq = []
n = int(input())
table = []

for i in range(n):
    idx, s, e = map(int, input().split())
    heapq.heappush(pq, (s, e, idx))

for i in range(n):
    s, e, idx = heapq.heappop(pq)
    if len(table) == 0:
        heapq.heappush(table, (e, s, idx))
        continue

    te, ts, tidx = heapq.heappop(table)

    if te > s:
        heapq.heappush(table, (te, ts, tidx))
    heapq.heappush(table, (e, s, idx))

print(len(table))