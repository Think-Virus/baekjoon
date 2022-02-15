# 정답 코드 확인
# 추가 담겨있는 리스트를 오름차순으로 정렬
# 여태까지 추의 합 + 1 >= 추의 무게 형식으로 비교
# 만약 여태까지 추의 합 + 1 가 추의 무게보다 크다면 여태까지 추의 합 + 1 무게는 추를 이용하여 구현하지 못하게 됨
"""
여기서 핵심은 target전에는 모두 만들 수 있다는 것이다.

리스트에 원소가 1,2,3 이라고 가정할 때
1
2
3
4=1+3
5=2+3
6=1+2+3
7은 만들 수 없으므로 정답은 7이 된다.
즉, target보다 더하는원소가 낮아야 한다는 것이다.
"""
# -> 수학적인 증명이 필요해
"""
7
3 1 6 2 7 30 1
"""
import sys

N = int(input())

weightList = list(map(int,sys.stdin.readline().split()))
weightList.sort()

result = 0
for i in range(N):
    if result + 1 >= weightList[i]:
        result += weightList[i]
    else:
        break

print(result + 1)