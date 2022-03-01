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
S = list(enumerate(input()))
T = input()
T_len = len(T)

anser = 0
while True and S :
    tmp = 0
    pre_idx = 0
    for t in T :
        for i,s in enumerate(S) :
            if s[1] == t :
                if pre_idx > s[0] :
                    tmp = -1
                    break
                del S[i]
                pre_idx = s[0]
                tmp += 1
                if T_len == tmp:
                    anser += 1
                break
    if T_len != tmp :
        break

print(anser)
