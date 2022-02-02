N = input()

def make_30(N) :
    if int(N) < 30 : # 30보다 작으면 30의 배수로 재배열 불가능함
        return -1

    if N.find("0") == -1 : # 30의 배수이기 때문에 0을 갖고있지 않으면 30의 배수로 재배열 불가능
        return -1

    # 0 제거
    Nr0 = N.replace("0","")
    Nr0_sum = 0 # 3의 배수 확인
    for i in Nr0 : # 반복문은 속도를 저하시키므로 최종적으로 확인
        Nr0_sum += int(i)
    if Nr0_sum // 3 != Nr0_sum / 3 :
        return -1

    # 0 개수 확인
    Cnt_0 = str(N).count("0")
    Nr0_list = list(Nr0)
    Nr0_max = "".join(sorted(Nr0_list,reverse=True))
    return int(Nr0_max) * 10**Cnt_0

print(make_30(N))
