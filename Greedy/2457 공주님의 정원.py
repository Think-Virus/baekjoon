# 총 N개의 꽃이 있는 데, 꽃은 모두 같은 해에 피어서 같은 해에 진다. 하나의 꽃은 피는 날과 지는 날이 정해져 있다.
# 예를 들어, 5월 8일 피어서 6월 13일 지는 꽃은 5월 8일부터 6월 12일까지는 꽃이 피어 있고, 6월 13일을 포함하여 이후로는 꽃을 볼 수 없다는 의미이다.
# (올해는 4, 6, 9, 11월은 30일까지 있고, 1, 3, 5, 7, 8, 10, 12월은 31일까지 있으며, 2월은 28일까지만 있다.)

# 이러한 N개의 꽃들 중에서 다음의 두 조건을 만족하는 꽃들을 선택하고 싶다.
#   공주가 가장 좋아하는 계절인 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 한다.
#   정원이 넓지 않으므로 정원에 심는 꽃들의 수를 가능한 적게 한다.
# N개의 꽃들 중에서 위의 두 조건을 만족하는, 즉 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 꽃들을 선택할 때,
# 선택한 꽃들의 최소 개수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에는 꽃들의 총 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 각 꽃이 피는 날짜와 지는 날짜가 주어진다.
# 하나의 날짜는 월과 일을 나타내는 두 숫자로 표현된다. 예를 들어서, 3 8 7 31은 꽃이 3월 8일에 피어서 7월 31일에 진다는 것을 나타낸다.
"""
정렬 문제일 듯 한데.. 일단 만약에 꽃들 중에서 11월 30일 이후까지 살아있는 것이 없거나 3월 1일에 필 수 있는 꽃이 없을 경우에는 0 출력

지금 예제를 보면
4
1 1 5 31
1 1 6 30
5 15 8 31
6 10 12 10
이렇게 인데..
같은 날짜면 최대한 늦게 지는 꽃이 좋을 것 같아
그러면 일단 정렬하고, 3월 1일 이전에 피는 꽃 중에서 가장 큰 값을 먼저 뽑자
그리고 날짜 값들은 3 1 -> 301 / 3 24 -> 324 이런 식으로 설정하면 계산하기 편할 거 같아

정리해보면
1. 3월 1일 이전에 피는 꽃 중 가장 늦게 지는 꽃 선택
2. 3월 1일 ~ 11월 30일 사이에 있는 꽃들 중에 기간이 긴 애들로 선정하고 선정 결과 중 마지막 결과가 11월 30일 이후인 애들만 고르면 될 듯?

1초 이내이고 N이 100,000이니까 2중 for문 쓰면 안될듯!
"""
import sys
N = int(sys.stdin.readline())
flower_list = []

def plus_0(val) :
    if int(val) < 10 :
        return "0"+val
    else :
        return val

for _ in range(N) : # 날짜 값을 정렬하기 위해 원하는 형식으로 변경해서 저장받는 부분
    input_val = list(map(plus_0,sys.stdin.readline().split()))
    flower_list.append((int(input_val[0] + input_val[1]),int(input_val[2] + input_val[3])))

flower_list.sort(key=lambda x:(x[0],-x[1])) # x[0]은 앞의 숫자를 기준으로 오름차순이며, -x[1]은 뒤의 숫자를 기준으로 내림차순으로 하는 것

if max(map(max, flower_list)) <= 1130 : # 꽃들 중에서 11월 30일 이후까지 살아있는 것이 없는 경우
    print(0)
    exit()

# 시작월의 첫 숫자가 3이 아닌 것중에 가장 길게 가는 걸 첫번째 것으로 뽑아야지
check_list = [x for x in flower_list if x[0] <= 310]
if not check_list :
    print(0)
    exit()

flower_list = flower_list[len(check_list):]

end_date = max(map(max,check_list))
Cnt = 1

while True :
    Cnt += 1
    check_list = [x for x in flower_list if x[0] <= end_date] # 이전 끝나는 것보다 크거나 같아야 함
    end_date = max(map(max,check_list))
    if end_date >= 1130 :
        break

    flower_list = flower_list[len(check_list):]

print(Cnt)