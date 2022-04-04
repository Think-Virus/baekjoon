# 아래 그림과 같이 직선 도로상에 왼쪽부터 오른쪽으로 1번부터 차례대로 번호가 붙여진 마을들이 있다.
# 마을에 있는 물건을 배송하기 위한 트럭 한 대가 있고, 트럭이 있는 본부는 1번 마을 왼쪽에 있다.
# 이 트럭은 본부에서 출발하여 1번 마을부터 마지막 마을까지 오른쪽으로 가면서 마을에 있는 물건을 배송한다.
# 각 마을은 배송할 물건들을 박스에 넣어 보내며, 본부에서는 박스를 보내는 마을번호, 박스를 받는 마을번호와 보낼 박스의 개수를 알고 있다.
# 박스들은 모두 크기가 같다. 트럭에 최대로 실을 수 있는 박스의 개수, 즉 트럭의 용량이 있다.
# 이 트럭 한대를 이용하여 다음의 조건을 모두 만족하면서 최대한 많은 박스들을 배송하려고 한다.
# 조건 1: 박스를 트럭에 실으면, 이 박스는 받는 마을에서만 내린다.
# 조건 2: 트럭은 지나온 마을로 되돌아가지 않는다.
# 조건 3: 박스들 중 일부만 배송할 수도 있다.
# 마을의 개수, 트럭의 용량, 박스 정보(보내는 마을번호, 받는 마을번호, 박스 개수)가 주어질 때,
# 트럭 한 대로 배송할 수 있는 최대 박스 수를 구하는 프로그램을 작성하시오. 단, 받는 마을번호는 보내는 마을번호보다 항상 크다.

"""
내려놓는 위치가 가까운 순으로 sort하고
저장공간에 자리 있느지 여부로 값 집어넣고
단계 확인하기

In :
4 40
6
3 4 20
1 2 10
1 3 20
1 4 30
2 3 10
2 4 20

Out :
70
"""

"""
1. 도착 순서가 빠른 순서로 박스를 정렬합니다.
2. 마을의 수와 길이가 동일한 배열을 선언합니다. (초기값은 트럭의 최대 용량입니다)
3. 현재 박스의 출발 위치에서 도착 위치로 배송할 수 있는 만큼 최대한 박스를 배송합니다.
- 2번에서 선언한 배열에는 각 위치에 배송할 수 있는 최대 박스 크기가 저장되어 있습니다. 
따라서 출발 위치에서 도착 위치 사이에 있는 배열의 값 중 가장 작은 값과 현재 배송할 박스의 수 중 작은 값을 최종적으로 배송할 수 있습니다.

# 핵심은 도착지 순으로 정렬 하는것과
# 마을별 가능 적재량을 저장하여 목적지까지 거쳐가는 마을 중 가장 적은 적재량만큼만 배달 하는것이다.

# 도착지가 가장 가까운 순으로 정렬
# 1. 가장 가까운 곳의 도착지까지 거치는 마을 중 적재량이 가장 조금 남은곳을 찾아서 그만큼만 싣는다.
# 2. 제일 궁금했던 부분: 적재량이 가장 조금 남은곳을 찾아서 실는 이유 
# -> 거쳐가는 마을에서 적재량이 가장 조금 남은만큼만 실어야 도착지가 먼 곳의 박스를 많이 실어서 거쳐가는 마을의 박스를 못실는 일을 방지할 수 있다.
# 예를들어    
    1 -> 4 50박스 배달. 
    2 -> 3 10박스배달. 
    3 -> 4 10박스배달 
이고 최대 적재량이 50일때 1번 마을에서 50을 다 실어버리면 2번 3번 마을에선 여유 적재공간이 없기때문에 그냥 지나쳐야한다.
# 하지만 적재량이 가장 조금 남은 곳인 2번 마을의 40 을 찾아서 1번 마을에서 40박스만 싣는다면 2번마을에서 10박스를 싣고 3번마을에서 10박스를 내려주고 10박스를 싣고 4번마을에서 40+10박스를 내려줘서 총 60박스를 나를수있다.
"""
import sys

n, c = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

box.sort(key=lambda x: x[1])  # 도착 시간이 빠른 순서로 정렬

answer = 0  # 최대 박스 수
remain = [c] * (n + 1)  # 각 위치에 남은 공간

for i in range(m):
    temp = c  # c개를 옮길 수 있다고 가정
    for j in range(box[i][0], box[i][1]):
        temp = min(temp, remain[j])
    temp = min(temp, box[i][2])
    for j in range(box[i][0], box[i][1]): # 앞에서 최소 갯수를 들기로 했으니, 그 전까지에서 들 수 있는 개수를 든만큼 빼주는 것
        remain[j] -= temp
    answer += temp

print(answer)