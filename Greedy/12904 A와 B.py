# 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 것
# 문자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능
# 1. 문자열의 뒤에 A를 추가한다.
# 2. 문자열을 뒤집고 뒤에 B를 추가한다.
# 주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성
# S를 T로 바꿀 수 있으면 1을 없으면 0을 출력
"""
첫째 줄에 S가 둘째 줄에 T가 주어진다. (1 ≤ S의 길이 ≤ 999, 2 ≤ T의 길이 ≤ 1000, S의 길이 < T의 길이)
In :
B
ABBA
Out :
1
"""
import sys
S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

tmp = 0
for _ in range(len(T)) :
    if T == S : # 같은지 확인
        tmp = 1
        break
    else:
        if T[-1] == "A" : # 끝이 A일 경우는 1번 경우만 있음
            T = T[:-1] # 마지막 A 없애기
        else : # 끝이 B인 경우는 2번 경우만 있음
            T = T[-2::-1]
print(tmp)