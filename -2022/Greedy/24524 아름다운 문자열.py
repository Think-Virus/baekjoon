# S를 갖고 T 만들기
"""
In :
aabb
ab
Out :
2

In :
aabb
ba
Out :
0

In :
abba
ab
Out :
1
"""


"""
정답 코드 확인...

|T| 크기의 배열 A를 만들어서, 그 배열에 무언가를 기록을 하는 거다.
그리고 문자열 S를 앞부터 순차적으로 확인하면서 다음과 같은 규칙에 의거해 숫자를 기록하면 된다.
A[i] : 현재 까지 T[i] 문자가 문자열 S에서 몇 번 선택이 됐습니다. (i == 0 일 때만, 이 한가지 조건만으로 A[i]++ 된다.)
그런데 i !=0 이면 선택되는 기준이 한 개가 더 생긴다. 바로 A[i] < A[i – 1]이어야 A[i]++된다는 것이다.
"""
import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()
A = [0] * len(T)

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            if j == 0:
                A[j] += 1
                continue
            if A[j] < A[j - 1]:
                A[j] += 1
                continue
print(A[len(T)-1])