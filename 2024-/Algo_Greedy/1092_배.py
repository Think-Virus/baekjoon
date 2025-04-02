import sys
import heapq
from collections import deque


def input_data():
    n = int(sys.stdin.readline())
    cranes = []
    for crane in map(int, sys.stdin.readline().split()):
        heapq.heappush(cranes, -1 * crane)
    m = int(sys.stdin.readline())
    boxes = deque(sorted(list(map(int, sys.stdin.readline().split())), reverse=True))

    return cranes, boxes


def solve(cranes, boxes):
    spent_minutes = 0

    lightest_box = boxes[-1]
    usable_cranes = []
    while cranes:
        crane = heapq.heappop(cranes)
        if -1 * crane >= lightest_box:
            heapq.heappush(usable_cranes, crane)

    if not usable_cranes:
        print(-1)
        return

    while boxes:
        passed_cranes = []

        while usable_cranes:
            crane = -1 * heapq.heappop(usable_cranes)

            if not boxes:
                break

            if crane >= boxes[0]:
                boxes.popleft()
                heapq.heappush(passed_cranes, -1 * crane)
            else:
                lightest_box = boxes[-1]

                if crane >= lightest_box:
                    boxes.pop()
                    heapq.heappush(passed_cranes, -1 * crane)

        usable_cranes = passed_cranes
        spent_minutes += 1

    print(spent_minutes)


if __name__ == '__main__':
    cranes, boxes = input_data()
    solve(cranes, boxes)
