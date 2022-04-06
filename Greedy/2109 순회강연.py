# 한 저명한 학자에게 n(0 ≤ n ≤ 10,000)개의 대학에서 강연 요청을 해 왔다.
# 각 대학에서는 d(1 ≤ d ≤ 10,000)일 안에 와서 강연을 해 주면 p(1 ≤ p ≤ 10,000)만큼의 강연료를 지불하겠다고 알려왔다.
# 각 대학에서 제시하는 d와 p값은 서로 다를 수도 있다. 이 학자는 이를 바탕으로, 가장 많은 돈을 벌 수 있도록 순회강연을 하려 한다.
# 강연의 특성상, 이 학자는 하루에 최대 한 곳에서만 강연을 할 수 있다.
# 예를 들어 네 대학에서 제시한 p값이 각각 50, 10, 20, 30이고, d값이 차례로 2, 1, 2, 1 이라고 하자.
# 이럴 때에는 첫째 날에 4번 대학에서 강연을 하고, 둘째 날에 1번 대학에서 강연을 하면 80만큼의 돈을 벌 수 있다.
"""
이전에 풀었던 것처럼 하면 될 듯
1. 날짜 순 오름차순, 페이 내림차순으로 정렬
2. pay를 pay_heap에 넣기
3. 리스트에 추가한 후 데드라인과 리스트의 길이를 비교한다.
"""
import heapq
import sys

speech_list = []
pay_heap = []
for _ in range(int(sys.stdin.readline())) :
    speech_list.append(list(map(int,sys.stdin.readline().split())))

# 정렬
speech_list.sort(key = lambda x:(x[1],-x[0]))

for speech in speech_list :
    heapq.heappush(pay_heap,speech[0])
    if speech[1] < len(pay_heap) : # 추가하고나서 날짜랑 비교하는 게 중요!!!!!!
        heapq.heappop(pay_heap)

print(sum(pay_heap))