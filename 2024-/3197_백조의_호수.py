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
"""
import sys


class Node:
    def __init__(self, state):
        self.state = state  # Ice : 1, Water : 0, Swan : -1
        self.right = None
        self.left = None
        self.up = None
        self.down = None
        self.row = None
        self.col = None


class Lake:
    def __init__(self, root=None):
        self.root = root
        self.goal = None
        self.day = 0
        self.nodes = []

    def insert_node(self, node, total_c):
        self.nodes.append(node)
        node.row = (len(self.nodes) - 1) // total_c
        node.col = (len(self.nodes) - 1) % total_c

        if not self.root and node.state == -1:
            self.root = node
        elif node.state == -1:
            self.goal = node

    def melt(self):
        freezing_nodes = list(filter(self._is_freezing, self.nodes))
        self.day += 1
        for node in freezing_nodes:
            node.state = 0

    def _is_freezing(self, node):
        if node.state != 1:  # Water or Swan -> pass
            return False
        else:
            left_node_state = node.left.state if node.left else 2
            right_node_state = node.right.state if node.right else 2
            up_node_state = node.up.state if node.up else 2
            down_node_state = node.down.state if node.down else 2

            return any(state == 0 for state in [left_node_state, right_node_state, up_node_state, down_node_state])

    def find_path(self):
        visited_nodes = [self.root]
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            for n in self._directions_not_ice(node):
                if n not in visited_nodes:
                    visited_nodes.append(n)
                    queue.append(n)
        #
        # tmp = [[0 for _ in range(2)] for _ in range(10)]
        # for visited_node in visited_nodes:
        #     tmp[visited_node.row][visited_node.col] = 1
        # print(f"---\n{self.day}")
        # for r in range(10):
        #     origin = ""
        #     non_origin = ""
        #     for c in range(2):
        #         origin += str(self.nodes[2*r+c].state) + " "
        #         non_origin += str(tmp[r][c]) + " "
        #     print(f"{origin}->{non_origin}")

            # print()

        return self.goal in visited_nodes

    def _directions_not_ice(self, node):
        directions = []
        if node.right:
            if node.right.state != 1:
                directions.append(node.right)
        if node.left:
            if node.left.state != 1:
                directions.append(node.left)
        if node.up:
            if node.up.state != 1:
                directions.append(node.up)
        if node.down:
            if node.down.state != 1:
                directions.append(node.down)
        return directions


def make_lake(r, c, data, lake):
    for ir, row in enumerate(data):
        for ic, node in enumerate(row):
            if ic != c - 1:
                right_node = data[ir][ic + 1]
                node.right = right_node
                right_node.left = node
            if ic != 0:
                left_node = data[ir][ic - 1]
                node.left = left_node
                left_node.right = node
            if ir != 0:
                up_node = data[ir - 1][ic]
                node.up = up_node
                up_node.down = node
            if ir != r - 1:
                down_node = data[ir + 1][ic]
                node.down = down_node
                down_node.up = node

            lake.insert_node(node, c)


def main():
    r, c = map(int, sys.stdin.readline().split())
    data = [[Node(1 if s == "X" else (0 if s == "." else -1)) for s in sys.stdin.readline()[:-1]] for _ in range(r)]
    lake = Lake()

    make_lake(r, c, data, lake)

    is_find = lake.find_path()
    while not is_find:
        lake.melt()
        is_find = lake.find_path()

    print(lake.day)


if __name__ == '__main__':
    main()
