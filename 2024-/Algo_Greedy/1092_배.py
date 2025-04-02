import sys
import heapq


def input_data():
    n = int(sys.stdin.readline())
    cranes = []
    for crane in map(int, sys.stdin.readline().split()):
        heapq.heappush(cranes, crane)
    m = int(sys.stdin.readline())
    boxes = []
    for box in map(int, sys.stdin.readline().split()):
        heapq.heappush(boxes, box)

    return cranes, boxes


def solve(cranes, boxes):
    spent_minutes = 0
    while boxes:
        tmp_cranes = cranes[:]

        while tmp_cranes:
            crane = heapq.heappop(tmp_cranes)

            if not boxes:
                break

            if crane >= boxes[0]:
                heapq.heappop(boxes)

        spent_minutes += 1

    print(spent_minutes)


if __name__ == '__main__':
    cranes, boxes = input_data()
    solve(cranes, boxes)
