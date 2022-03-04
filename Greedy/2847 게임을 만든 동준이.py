# 게임에는 총 N개의 레벨이 있고, 각 레벨을 클리어할 때 마다 점수가 주어진다.
# 플레이어의 점수는 레벨을 클리어하면서 얻은 점수의 합으로, 이 점수를 바탕으로 온라인 순위를 매긴다.
# 동준이는 레벨을 난이도 순으로 배치했다. 하지만, 실수로 쉬운 레벨이 어려운 레벨보다 점수를 많이 받는 경우를 만들었다.
# 이 문제를 해결하기 위해 동준이는 특정 레벨의 점수를 감소시키려고 한다.
# 이렇게해서 각 레벨을 클리어할 때 주는 점수가 증가하게 만들려고 한다.
# 각 레벨을 클리어할 때 얻는 점수가 주어졌을 때, 몇 번 감소시키면 되는지 구하는 프로그램을 작성하시오.
# 점수는 항상 양수이어야 하고, 1만큼 감소시키는 것이 1번이다. 항상 답이 존재하는 경우만 주어진다.
# 정답이 여러 가지인 경우에는 점수를 내리는 것을 최소한으로 하는 방법을 찾아야 한다.

# 다음 값에서 -1하구 원래 값이랑 비교해서 얼만큼 내렸는지 확인하면 해결 가능할 듯
import sys
N = int(sys.stdin.readline())
Score_list = []
for _ in range(N) :
    Score_list.append(int(sys.stdin.readline()))

anser = 0
for i in range(N-1,-1,-1) :
    if i == 0 :
        break
    else:
        if Score_list[i] > Score_list[i-1] :
            continue
        else:
            tmp = Score_list[i] - 1
            anser += Score_list[i-1] - tmp
            Score_list[i - 1] = tmp
print(anser)