# PPAP 문자열은 문자열 P에서 시작하여, 문자열 내의 P를 PPAP로 바꾸는 과정을 반복하여 만들 수 있는 문자열로 정의된다.
# 정확하게는 다음과 같이 정의된다.
    # P는 PPAP 문자열이다.
    # PPAP 문자열에서 P 하나를 PPAP로 바꾼 문자열은 PPAP 문자열이다.

# 예를 들어 PPAP는 PPAP 문자열이다. 또한, PPAP의 두 번째 P를 PPAP로 바꾼 PPPAPAP 역시 PPAP 문자열이다.

# 문자열이 주어졌을 때, 이 문자열이 PPAP 문자열인지 아닌지를 알려주는 프로그램을 작성하여라.

# tip을 봤을 때, 스택을 이용해서 A와 만날 때 확인하라고 하는데..
# PPPP는 NP임..
# P도 PPAP임...

# 1등 코드는 아예 방식이 다르고 속도도 4배 빠르므로 알아둬야 할 필요 있을듯
import sys

s = input()

cnt = 0 # cnt는 P의 개수
i = 0
while i < len(s):
    if s[i] == 'P': # P인 경우
        cnt += 1
        i += 1
        continue

    # A 인 경우
    if i + 1 < len(s): # 가장 끝에 A가 있지 않는 경우
        if cnt >= 2 and s[i + 1] == 'P': # A 다음에 P가 있는 경우
            cnt -= 1 # 2개 쌓였던 PP가 PPAP로 판정되어 P가 되었으므로 -1한 거
            i += 1 # A 다음까지 확인했으므로 i는 다음으로 넘어가기 위해 +1
        else: # A 다음에 A가 있는 경우
            print("NP")
            sys.exit()
            break

    else: # 가장 끝에 A가 있는 경우
        print("NP")
        sys.exit()
        break

    i += 1

if cnt == 1:
    print("PPAP")
else: # P만 있는 경우
    print("NP")


"""
from collections import deque
p = input()

p = deque(p)
tmp_list = []

result = deque([])
while len(p) > 2 :
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

if "".join(result)+"".join(p) == "PPAP" or "".join(result)+"".join(p) == "P" :
    print("PPAP")
else:
    print("NP")
"""