"""
문제
    두 마리의 백조가 호수에서 살고 있었다. 그렇지만 두 마리는 호수를 덮고 있는 빙판으로 만나지 못한다.
    호수는 행이 R개, 열이 C개인 직사각형 모양이다. 어떤 칸은 얼음으로 덮여있다.
    호수는 차례로 녹는데, 매일 물 공간과 접촉한 모든 빙판 공간은 녹는다.
    두 개의 공간이 접촉하려면 가로나 세로로 닿아 있는 것만 (대각선은 고려하지 않는다) 생각한다.
    아래에는 세 가지 예가 있다.

    ...XXXXXX..XX.XXX ....XXXX.......XX .....XX..........
    ....XXXXXXXXX.XXX .....XXXX..X..... ......X..........
    ...XXXXXXXXXXXX.. ....XXX..XXXX.... .....X.....X.....
    ..XXXXX..XXXXXX.. ...XXX....XXXX... ....X......XX....
    .XXXXXX..XXXXXX.. ..XXXX....XXXX... ...XX......XX....
    XXXXXXX...XXXX... ..XXXX.....XX.... ....X............
    ..XXXXX...XXX.... ....XX.....X..... .................
    ....XXXXX.XXX.... .....XX....X..... .................
          처음               첫째 날             둘째 날
    백조는 오직 물 공간에서 세로나 가로로만(대각선은 제외한다) 움직일 수 있다.
    며칠이 지나야 백조들이 만날 수 있는 지 계산하는 프로그램을 작성하시오.

입력
    입력의 첫째 줄에는 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1500.
    다음 R개의 줄에는 각각 길이 C의 문자열이 하나씩 주어진다. '.'은 물 공간, 'X'는 빙판 공간, 'L'은 백조가 있는 공간으로 나타낸다.

출력
    첫째 줄에 문제에서 주어진 걸리는 날을 출력한다.
"""
"""
접근법
    - 각 공간들을 Node로 해서 Graph로 만들면 되지 않을까?
        - 하루가 지날 때마다, 상하좌우 중 하나가 X이면 .로 바꾸는 거지
        - 바꾸는 거는 한 번에 되어야 할 테니까, to be를 따로 놓고 만들어도 좋을듯
        - 백조 위치도 잡아놔야 할 것 같은데
        - 길 찾기는 DP로 하면 될라나
            - 아닌 것 같아
        - DFS 쓰는 게 맞을듯 
            -> N^2일 경우, 1초 이내는 연산은 10^8 ~ 10^9 연산이 가능함.. 
            - BFS를 써야 할듯
        - 그냥 행렬 쓰면 N^2일텐데...
    ---
    위 접근법은 틀림
정답
    - 두 개의 BFS 큐 사용
        - 하나는 빙판이 녹는 과정을 관리 : water_queue
        - 다른 하나는 백조의 이동 경로를 관리 : swan_queue
    - 동시에 진행
        - 매일 빙판이 녹는 과정을 처리하며 물 공간을 확장함
        - 백조가 물 공간을 따라 이동하며 서로 만나는지 확인
    - 경계 조건 최소화
        - 매일의 반복에서 중복 방문 방지를 위해 방문 상태를 별도의 배열로 관리
"""
import sys
from collections import deque


def input_data():
    r, c = map(int, input().split())
    swans = []
    lake = [["."] * c for _ in range(r)]
    water_queue = deque()

    for i in range(r):
        line = sys.stdin.readline().strip()
        for j, cell in enumerate(line):
            if cell == 'L':
                swans.append((i, j))
                lake[i][j] = "."
            elif cell == '.':
                water_queue.append((i, j))
                lake[i][j] = "."
            else:
                lake[i][j] = "X"

    return r, c, swans, lake, water_queue


def solve():
    r, c, swans, lake, water_queue = input_data()
    visited = [[False] * c for _ in range(r)]
    swan1, swan2 = swans
    swan_queue = deque([swan1])
    visited[swan1[0]][swan1[1]] = True
    day = 0

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # up, down, right, left

    def can_meet(swan_queue):
        next_swan_queue = deque()
        while swan_queue:
            x, y = swan_queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                    if (nx, ny) == swan2:
                        return True, next_swan_queue

                    visited[nx][ny] = True
                    if lake[nx][ny] == ".":
                        swan_queue.append((nx, ny))
                    else:
                        next_swan_queue.append((nx, ny))
        return False, next_swan_queue

    def melt_ice(water_queue):
        next_water_queue = deque()

        while water_queue:
            x, y = water_queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and lake[nx][ny] == "X":
                    lake[nx][ny] = "."
                    next_water_queue.append((nx, ny))
        return next_water_queue

    while True:
        meet, swan_queue = can_meet(swan_queue)
        if meet:
            print(day)
            return

        water_queue = melt_ice(water_queue)
        day += 1


if __name__ == '__main__':
    solve()
