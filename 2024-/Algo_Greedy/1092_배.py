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

    if not usable_cranes or boxes[0] > -1 * usable_cranes[0]:
        print(-1)
        return

    while boxes:
        curr_usable_cranes = []

        while usable_cranes:
            passed_boxes = deque()
            crane = -1 * heapq.heappop(usable_cranes)
            if not boxes:
                break

            if crane >= boxes[0]:
                boxes.popleft()
                heapq.heappush(curr_usable_cranes, -1 * crane)
            else:
                while boxes:
                    curr_box = boxes.popleft()
                    if crane >= curr_box:
                        heapq.heappush(curr_usable_cranes, -1 * crane)
                        break
                    else:
                        passed_boxes.append(curr_box)
            if passed_boxes:
                boxes = passed_boxes + boxes

        usable_cranes = curr_usable_cranes
        spent_minutes += 1

    print(spent_minutes)


if __name__ == '__main__':
    cranes, boxes = input_data()
    solve(cranes, boxes)
