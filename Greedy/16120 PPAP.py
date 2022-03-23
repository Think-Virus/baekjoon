# PPAP 문자열은 문자열 P에서 시작하여, 문자열 내의 P를 PPAP로 바꾸는 과정을 반복하여 만들 수 있는 문자열로 정의된다.
# 정확하게는 다음과 같이 정의된다.
    # P는 PPAP 문자열이다.
    # PPAP 문자열에서 P 하나를 PPAP로 바꾼 문자열은 PPAP 문자열이다.

# 예를 들어 PPAP는 PPAP 문자열이다. 또한, PPAP의 두 번째 P를 PPAP로 바꾼 PPPAPAP 역시 PPAP 문자열이다.

# 문자열이 주어졌을 때, 이 문자열이 PPAP 문자열인지 아닌지를 알려주는 프로그램을 작성하여라.

# tip을 봤을 때, 스택을 이용해서 A와 만날 때 확인하라고 하는데..
# PPPP는 NP임..
from collections import deque
p = input()

if p.find('A') == -1 :
    print('NP')
    exit()

p = deque(p)
tmp_list = []

result = deque([])
while len(p) > 1 :
    pp = p.popleft()
    if pp == 'A' :
        pf = p.popleft()
        if pf == 'P' :
            if len(result) < 2 :
                print('NP')
                exit()
            if result.pop() == 'P' and result.pop() == 'P' :
                result.append('P')
            else:
                print('NP')
                exit()
        else:
            print('NP')
            exit()
    else:
        result.append(pp)
print("PPAP")