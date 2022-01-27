var_input = input("")
var_input = list(map(int, var_input.split(" ")))
A = int(var_input[0])
B = int(var_input[1])
var_count = 0
while B :
    var_count += 1

    if B == A :
        print(var_count)
        break
    elif B < A :
        print(-1)
        break
    C = B
    C = str(B)

    if B % 2 == 0 : # 2로 나눠지는 경우
        B = B//2
    elif C[-1] == '1' and B > 10: # 2로 나눠지지 않고, 끝이 1인 경우
        B = int(C[:-1])
    else:
        print(-1)
        break