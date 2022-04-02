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
"""
N,M = map(int,input().split())
position_list = list(map(int,input().split()))
position_list.sort()
plus_position_list = []
minus_position_list = []
for i in range(N) :
    if position_list[i] > 0 :
        plus_position_list = position_list[i:]
        minus_position_list.sort()
        break
    else:
        minus_position_list.append(-1 * position_list[i])

ans = 0
while plus_position_list and minus_position_list : # 둘 다 가득 차 있을 때만 사용
    if len(plus_position_list) < M and len(minus_position_list) < M : # 두 방향 모두 M보다 양이 적을 때
        if plus_position_list[-1] < minus_position_list[-1] : # 음수 위치에 있는 책이 더 먼 경우
            ans += plus_position_list[-1]*2
            plus_position_list = []
        else:
            ans += minus_position_list[-1]*2
            minus_position_list = []
    elif len(plus_position_list) < M : # 양수 진영만 M보다 작을 때
        if plus_position_list[-1] < minus_position_list[M-1] : # 음수 위치에 있는 책이 더 먼 경우
            ans += plus_position_list[-1]*2
            plus_position_list = []
        else:
            ans += minus_position_list[M-1]*2
            minus_position_list = minus_position_list[M-1:]
            if minus_position_list :
                minus_position_list = minus_position_list[1:] # IndexError 방지
    elif len(minus_position_list) < M : # 음수 진영만 M보다 작을 때
        if plus_position_list[M-1] < minus_position_list[-1] : # 음수 위치에 있는 책이 더 먼 경우
            ans += plus_position_list[M-1]*2
            plus_position_list = plus_position_list[M-1:]
            if plus_position_list :
                plus_position_list = plus_position_list[1:] # IndexError 방지
        else:
            ans += minus_position_list[-1]*2
            minus_position_list = []
    else:
        if plus_position_list[M-1] < minus_position_list[M-1] : # 음수 위치에 있는 책이 더 먼 경우
            ans += plus_position_list[M-1]*2
            plus_position_list = plus_position_list[M-1:]
            if plus_position_list :
                plus_position_list = plus_position_list[1:] # IndexError 방지
        else:
            ans += minus_position_list[M-1]*2
            minus_position_list = minus_position_list[M-1:]
            if minus_position_list :
                minus_position_list = minus_position_list[1:] # IndexError 방지

while plus_position_list :
    if len(plus_position_list) < M :# M 개보다 적게 남았을 때
        ans += plus_position_list[-1]
        break
    else:
        ans += plus_position_list[M - 1] * 2
        plus_position_list = plus_position_list[M - 1:]
        if plus_position_list:
            plus_position_list = plus_position_list[1:]  # IndexError 방지

while minus_position_list :
    if len(minus_position_list) < M :# M 개보다 적게 남았을 때
        ans += minus_position_list[-1]
        break
    else:
        ans += minus_position_list[M - 1] * 2
        minus_position_list = minus_position_list[M - 1:]
        if minus_position_list:
            minus_position_list = minus_position_list[1:]  # IndexError 방지
print(ans)