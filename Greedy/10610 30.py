# 1등 코드
import sys

n = list(sys.stdin.readline().rstrip()) # 바로 리스트로 만들어버림
n.sort(reverse=True) #내가 했던 것처럼 역으로 정렬
if n[-1] != '0' or sum(map(int, n)) % 3 != 0: # 마지막에 0이 없으면 30의 배수가 아니고 값들의 합이 3으로 떨어지지 않으면 30의 배수가 아닌 것을 한 번에 해결함
    print(-1)
else:
    print(''.join(n)) # 값을 내보낼 때에 int든 str이든 상관 없는 듯


# 내 코드
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
