# 모든 학생들은 자신이 N명 중에서 몇 등을 할 것인지 예상 등수를 적어서 제출
# KOI 담당조교로 참가한 김진영 조교는 실수로 모든 학생의 프로그램을 날려 버렸다.
# 1등부터 N등까지 동석차 없이 등수를 매겨야 하는 김 조교는, 어쩔 수 없이 각 사람이 제출한 예상 등수를 바탕으로 임의로 등수를 매기기로 했다.
# 자신의 등수를 A등으로 예상하였는데 실제 등수가 B등이 될 경우,
# 이 사람의 불만도는 A와 B의 차이 (|A - B|)로 수치화할 수 있다. 당신은 N명의 사람들의 불만도의 총 합을 최소로 하면서, 학생들의 등수를 매기려고 한다.
import sys

rank_list = []
N = int(sys.stdin.readline())
for _ in range(N) :
    rank_list.append(int(sys.stdin.readline()))

rank_list.sort()
real_rank_list = [i for i in range(1,N+1)]
rank_list = [abs(x-y) for x,y in zip(real_rank_list,rank_list)]
print(sum(rank_list))