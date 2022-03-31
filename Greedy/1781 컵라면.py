# 상욱 조교는 동호에게 N개의 문제를 주고서, 각각의 문제를 풀었을 때 컵라면을 몇 개 줄 것인지 제시 하였다.
# 하지만 동호의 찌를듯한 자신감에 소심한 상욱 조교는 각각의 문제에 대해 데드라인을 정하였다.

"""
문제 번호   1   2   3   4   5   6   7
데드라인       1   1   3   3   2   2   6
컵라면 수   6   7   2   1   4   5   1
"""

# 위와 같은 상황에서 동호가 2, 6, 3, 1, 7, 5, 4 순으로 숙제를 한다면 2, 6, 3, 7번 문제를 시간 내에 풀어 총 15개의 컵라면을 받을 수 있다.
# 문제는 동호가 받을 수 있는 최대 컵라면 수를 구하는 것이다. 위의 예에서는 15가 최대이다.
# 문제를 푸는데는 단위 시간 1이 걸리며, 각 문제의 데드라인은 N이하의 자연수이다.
# 또, 각 문제를 풀 때 받을 수 있는 컵라면 수와 최대로 받을 수 있는 컵라면 수는 모두 2^31보다 작거나 같은 자연수이다.
# 첫 줄에 숙제의 개수 N (1 ≤ N ≤ 200,000)이 들어온다.
# 다음 줄부터 N+1번째 줄까지 i+1번째 줄에 i번째 문제에 대한 데드라인과 풀면 받을 수 있는 컵라면 수가 공백으로 구분되어 입력된다.

"""
그냥 딕셔너리 써서 데드라인 순으로 자르고 하면 쉽게 풀 수 있지 않을까..?
정렬 문제일 거 같긴 한데
정렬한다면 컵라면 수가 1순위고, 그 다음에 데드라인일라나? -> 물론 데드라인 지난 것들은 페기해야 겠지만.. 이게 맞을듯??
그럴 경우 문제가
문제 번호   1   2   3   4   5   6   7
데드라인       1   1   1   3   2   2   6
컵라면 수   1   2   1   4   4   5   1
이럴 경우에 아 컵라면 수가 우선이면 괜찮을라나??

마지막 날에 할 수 있는 건 마지막 날에 처리하자
그러면 날짜별로 큰 데드라인부터 확인..? N부터 거꾸로 내려가면 될듯
"""
import sys
stdin = sys.stdin
N = int(stdin.readline())
day_list = [0 for i in range(N)]
assignment_list = []

for _ in range(N) :
    assignment_list.append(list(map(int,stdin.readline().split())))

assignment_list.sort(key =lambda x:(-x[1],-x[0]))

for assignment in assignment_list :
    idx_deadline = assignment[0]-1
    if day_list[idx_deadline] == 0 :
        day_list[idx_deadline] = assignment[1]
    elif day_list[:idx_deadline+1].count(0) != 0 :
        tmp = day_list[:idx_deadline+1][::-1]
        day_list[idx_deadline - tmp.index(0)] = assignment[1]

print(sum(day_list))