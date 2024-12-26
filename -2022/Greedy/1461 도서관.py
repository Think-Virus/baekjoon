# 도서관의 개방시간이 끝나서 세준이는 사람들이 마구 놓은 책을 다시 가져다 놓아야 한다.
# 세준이는 현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 있다.
# 각 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하는 프로그램을 작성하시오.
# 세준이는 한 걸음에 좌표 1칸씩 가며, 책의 원래 위치는 정수 좌표이다.
# 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다.
# 그리고 세준이는 한 번에 최대 M권의 책을 들 수 있다.
"""
In :
7 2
-37 2 -6 -39 -29 11 -28

Out :
131

정렬문제인거같고.. 일단 한 방향으로 쭉 가는 게 맞지
가까운 곳부터 가는 게 맞음 -> 왜냐면 결국 책 다시 가지러 0으로 가야하기 때문
- 값과 + 값 중 가까운 곳을 계속 확인해야 할듯

아 풀이방식 자체가 틀린 건 아니었네...
1. 음수와 양수를 나눈다.
2. 절대값이 큰 수부터 M개씩 분류
3. 각 묶음에서 절대값이 큰 수만큼 움직이면 됨
4. 움직여야 하는 값이 가장 큰 묶음은 돌아오지 않음
"""
n, m = map(int, input().split())
book = list(map(int, input().split()))

# 음수, 양수 나누기
left = []
right = []
for item in book:
    if item < 0:
        left.append(item)
    elif item > 0:
        right.append(item)

distance = []
left.sort()
for i in range(len(left) // m):
    distance.append(abs(left[m * i]))
if len(left) % m > 0:
    distance.append(abs(left[(len(left) // m) * m]))

right.sort(reverse=True)
for i in range(len(right) // m):
    distance.append(right[m * i])
if len(right) % m > 0:
    distance.append(right[(len(right) // m) * m])

distance.sort()
result = distance.pop()
result += 2 * sum(distance)
print(result)