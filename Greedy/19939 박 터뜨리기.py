# K개의 팀이 박 터트리기 게임을 한다. 각 팀은 하나의 바구니를 가지고 있고, 바구니에 들어있는 공을 던져서 자기 팀의 박을 터트려야 한다.
# 우리는 게임을 준비하기 위해서, N개의 공을 K개의 바구니에 나눠 담아야 한다. 이때, 게임의 재미를 위해서 바구니에 담기는 공의 개수를 모두 다르게 하고 싶다.
# 즉, N개의 공을 K개의 바구니에 빠짐없이 나누어 담는데, 각 바구니에는 1개 이상의 공이 있어야 하고, 바구니에 담긴 공의 개수가 모두 달라야 한다.
# 게임의 불공정함을 줄이기 위해서, 가장 많이 담긴 바구니와 가장 적게 담긴 바구니의 공의 개수 차이가 최소가 되도록 담을 것이다.

# 공을 바구니에 나눠 담기 위한 규칙을 정리하면 다음과 같다.
# N개의 공을 K개의 바구니에 빠짐없이 나누어 담는다.
# 각 바구니에는 1개 이상의 공이 들어 있어야 한다.
# 각 바구니에 담긴 공의 개수는 모두 달라야 한다.
# 가장 많이 담긴 바구니와 가장 적게 담긴 바구니의 공의 개수 차이가 최소가 되어야 한다.

# 위의 규칙을 모두 만족하며 N개의 공을 K개의 바구니에 나눠 담을 때, 나눠 담을 수 있는지 여부를 결정하고,
# 담을 수 있는 경우에는 가장 많이 담긴 바구니와 가장 적게 담긴 바구니의 공의 개수 차이를 계산해서 출력하는 프로그램을 작성하시오.
# 등차수열..
N, K = map(int, input().split())

if N < K*(K+1)/2 :
    print(-1)
    exit()



if K % 2 == 0:  # K가 짝수일 때
    mid_val = N // K + 1
else:
    mid_val = N // K

calc_val = -(round((K-1)/2))


def calc_map(v):
    global calc_val
    rv = v + calc_val
    calc_val += 1
    return rv


K_list = list(map(calc_map, [mid_val]*K))

remain = N-sum(K_list)
add_point = remain%K
if not add_point :
    print(K_list[-1]-K_list[0])
else:
    print(K_list[-1] - K_list[0] + 1)