"""
문제
    수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다.
    김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.
    참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
    수강신청 대충한 게 찔리면, 선생님을 도와드리자!

입력
    첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)
    이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)

출력
    강의실의 개수를 출력하라.

3
1 3
2 4
3 5

7
1 3
2 4
1 5
3 6
2 5
2 3
4 5
---
접근법
    목표 : 최소 강의실 사용
    방법 : 최대한 겹치는 강의 없이 배치 하는 것
        - 1차 추론
            - 끝나는 시간이 빠른 순으로 정렬 -> O(NlogN)
            - 0 ~ 가장 마지막 end 시간까지 순회 -> O(N)
                - 현재 시간에 필요한 강의실의 개수 확인 -> O(N)
                - Max 값 도출 -> O(1)
                -> O(N^2)인데, 최대 200,000 * 10^9의 N이 될 수 있으므로 폐기
        - 2차 추론
            - 끝나는 시간이 빠른 순으로 개발이 가능한가??
                - 불가능 -> 같은 시간에 어떤 수업이 있는지 알 수 없을듯
                    - [1,3] [2,3] [2,4] [1, 5] 이렇게 있으면 처음에 무조건 교실 2개가 필요한데, 이를 알아차릴 수 없음
                -> 시작 시간이 빠른 순으로 정렬!! -> O(NlogN)
            - 의식의 흐름
                - class 중 가장 먼저 시작하는 걸 확인 [S0, E0]
                - room은 우선 1개
                - 만약에 다음 수업 [S1, E1]이 있을 때, E0이 S1보다 작으면 room은 반환되었을 테니 -1
                - S1이 E0보다 작으면 Room이 하나 더 필요 +1
                - 문제는 만약 이미 수업이 room이 2개라면?
                    [1, 3], [1, 5], [3, 5]
                    Step 1.
                        room_class = [1, 3]
                        left_classes = [1, 5] [3, 5]
                        max_room = 1
                        cur_room = 1
                    Step 2.
                        room_class = [1, 3] [1, 5]
                        left_classes = [3, 5]
                        max_room = 2
                        cur_room = 2
                    Step 3.
                        room_class = [1, 5] [3, 5]
                        left_classes = []
                        max_room = 2
                        cur_room = 2
                - pseudo 코드
                left_classes = [...]
                left_class sort in order of class's start time
                room_class = [left_class.pop(0)]
                max_room = 0
                for new_start, new_end in left_classes:
                    room_class = list(filter(left_classes, key=lambda x:x[1]>new_start))
                    room_class.append([new_start, new_end])
                    cur_room = len(room_class)
                    if cur_room > max_room:
                        max_room = cur_room
                print(max_room)


"""
import sys


def input_data() -> list[list[int]]:
    n = int(sys.stdin.readline())
    classes = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: (x[0], x[1]))
    return classes


def solve():
    classes = input_data()

    def print_max_room(all_classes):
        left_classes = all_classes[1:]
        room_classes = [all_classes[0]]
        max_room = 0

        for start, end in left_classes:
            room_classes = list(filter(lambda x: x[1] > start, room_classes))
            room_classes.append([start, end])
            cur_room = len(room_classes)
            if cur_room > max_room:
                max_room = cur_room
        print(max_room)

    print_max_room(classes)


if __name__ == '__main__':
    solve()
