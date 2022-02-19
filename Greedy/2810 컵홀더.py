# 극장의 한 줄에는 자리가 N개
# 서로 인접한 좌석 사이에는 컵홀더가 하나씩 있고, 양 끝 좌석에는 컵홀더가 하나씩 더 있다.
# 이 극장에는 커플석이 있다. 커플석 사이에는 컵홀더가 없다.
# 극장의 한 줄의 정보가 주어진다. 이때, 이 줄에 사람들이 모두 앉았을 때, 컵홀더에 컵을 꽂을 수 있는 최대 사람의 수를 구하는 프로그램을 작성
# S는 일반 좌석, L은 커플석을 의미하며, L은 항상 두개씩 쌍으로 주어진다.
N = int(input())
Row = input()

L_check_var = False

if N == 1 :
    print(1)
elif N == 2 :
    print(2)
else : # N이 3 이상일 때
    Result_mid = ""
    Result_start = "*" + Row[0]
    Result_end =  Row[-1] + "*"
    Row = Row[1:len(Row)-1]
    Cnt = 0
    for Seat in Row :
        Cnt += 1
        if Seat == "S" :
            Result_mid = Result_mid+"*"+Seat
        elif Seat == "L" and not L_check_var :
            Result_mid = Result_mid+"*"+Seat
            L_check_var = True
        else :
            if Cnt == len(Row) :
                Result_mid = Result_mid + Seat + "*"
            else:
                Result_mid = Result_mid + Seat
            L_check_var = False
    Result = Result_start + Result_mid + Result_end
    print(Result.count("*"))