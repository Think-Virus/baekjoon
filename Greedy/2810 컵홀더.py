# 극장의 한 줄에는 자리가 N개
# 서로 인접한 좌석 사이에는 컵홀더가 하나씩 있고, 양 끝 좌석에는 컵홀더가 하나씩 더 있다.
# 이 극장에는 커플석이 있다. 커플석 사이에는 컵홀더가 없다.
# 극장의 한 줄의 정보가 주어진다. 이때, 이 줄에 사람들이 모두 앉았을 때, 컵홀더에 컵을 꽂을 수 있는 최대 사람의 수를 구하는 프로그램을 작성
# S는 일반 좌석, L은 커플석을 의미하며, L은 항상 두개씩 쌍으로 주어진다.

# 너무 복잡하게 생각했었다. 그냥 *이 들어가는 위치부터 만들고 인원하고 비교하는 분기처리만 하면 해결

N = int(input())
Row = input()
Row_plus = "*"
L_check_var = False

for Seat in Row :
    if Seat == "S" :
        Row_plus = Row_plus + "S" + "*"
    elif Seat == "L" and not L_check_var :
        L_check_var = True
        Row_plus = Row_plus + "L"
    else:
        L_check_var = False
        Row_plus = Row_plus + "L" + "*"

Holder_Cnt = Row_plus.count("*")
if N > Holder_Cnt :
    print(Holder_Cnt)
else:
    print(N)
