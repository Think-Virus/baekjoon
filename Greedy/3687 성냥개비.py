# 성냥개비는 숫자를 나타내기에 아주 이상적인 도구이다. 보통 십진수를 성냥개비로 표현하는 방법은 다음과 같다.
# 성냥개비의 개수가 주어졌을 때, 성냥개비를 모두 사용해서 만들 수 있는 가장 작은 수와 큰 수를 찾는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개 이다. 각 테스트 케이스는 한 줄로 이루어져 있고, 성냥개비의 개수 n이 주어진다. (2 ≤ n ≤ 100)
# 출력
# 각 테스트 케이스에 대해서 입력으로 주어진 성냥개비를 모두 사용해서 만들 수 있는 가장 작은 수와 가장 큰 수를 출력한다. 두 숫자는 모두 양수이어야 하고, 숫자는 0으로 시작할 수 없다.

"""
숫자 당 성냥개비 갯수
1 -> 2
2 -> 5
3 -> 5
4 -> 4
5 -> 5
6 -> 6
7 -> 3
8 -> 7
9 -> 6
0 -> 6

In :
4
3
6
7
15

Out :
7 7
6 111
8 711
108 7111111

큰 값을 만들 때는 첫 글자로 7이 가장 효율이 좋고 나머지는 1로 채우는 것이 좋음, 만약 1로 하기 전에 남는다면 그 값이 7보다 클 경우 4보다 앞에, 아니면 7보다 뒤로 설정!
작은 값은 가장 많은 성냥(8)과 0을 이용하는 것이 좋을듯

어차피 모든 숫자는 2와 3으로 만들 수 있음..
가장 작은 숫자를 만들 때는 8 -> 7이 좋고
가장 큰 숫자를 만들 떄는 1 -> 2이 좋음
"""

"""
check_2 = amount // 2 # 2의 개수
8은 성냥 7개 -> 즉 check_2가 3개 +1개가 1개는 있어야 함
만약 개수를 충족하지 않는다면?
다음 우선선위는 첫 자리가 아니라면 0, 첫 자리라면 6 -> check_2가 3개 필요
다음은 2 -> check_2가 2개 +1개 필요    
"""

import sys

n_l = []
for _ in range(int(sys.stdin.readline())) :
    n_l.append(int(sys.stdin.readline()))

for i in n_l :
    min_amount = i
    max_amount = min_amount

    # 최소값 구하기
    min_val = ''
    while min_amount > 0 :
        if min_amount >= 7 and (min_amount % 7 == 0 or min_amount // 7 > 1 or (min_amount // 7 > 0 and min_amount % 7 > 1)) :
             min_val = '8'+min_val
             min_amount -= 7
        elif min_amount >= 6 :
            min_amount -= 6
            if min_amount > 0 :
                min_val = '0'+min_val
            else:
                min_val = '6'+min_val
        elif min_amount >= 5 :
            min_amount -= 5
            min_val = '2'+min_val
        elif min_amount >= 4 :
            min_amount -= 4
            min_val = '4' + min_val
        elif min_amount >= 3:
            min_amount -= 3
            min_val = '7' + min_val
        else :
            min_amount -= 2
            min_val = '1' + min_val

    # 최대값 찾기
    check_2 = max_amount // 2
    if max_amount % 2 == 0 :
        max_val = '1' * check_2
    else:
        max_val = '7'*(max_amount % 2) + '1' * (check_2-1)

    print(min_val,max_val)