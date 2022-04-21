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
import heapq

S = list(enumerate(input()))
T = input()
T_len = len(T)

anser = 0
while True and S :
    tmp = 0
    pre_idx = 0
    candidate_S = []
    for t in T :
        while S :
            s = heapq.heappop(S)
            if s[1] == t :
                if pre_idx > s[0] :
                    continue
                pre_idx = s[0]
                tmp += 1
                if T_len == tmp:
                    anser += 1
                break
            else:
                candidate_S.append(s)

    if T_len != tmp :
        break

    while candidate_S:
        heapq.heappush(S, heapq.heappop(candidate_S))
print(anser)