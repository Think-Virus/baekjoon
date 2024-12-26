# 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있음 AAAA와 BB
# 이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다.
# '.'는 폴리오미노로 덮으면 안된다.
# 만약 덮을 수 없으면 -1을 출력한다.

"""
In :
XXXXXX
Out :
AAAABB
"""
import sys
board = sys.stdin.readline().rstrip()

while True :
    if board.count("X") % 2 == 1 :
        print(-1)
        break

    anser = ""
    c_length = 0
    for c in board :
        if c == "." :
            if c_length % 2 == 1 :
                anser = -1
                break
            len_4 = c_length // 4
            len_2 = (c_length - len_4*4)//2
            anser += "AAAA" * len_4 + "BB" * len_2
            c_length = 0
            anser += "."
        else :
            c_length += 1
    if anser != -1 and c_length != 0 :
        if c_length % 2 == 1 :
                anser = -1
        len_4 = c_length // 4
        len_2 = (c_length - len_4*4)//2
        anser += "AAAA" * len_4 + "BB" * len_2

    print(anser)
    break
