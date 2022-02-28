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
S = list(input())
T = input()

var_check = True
anser = 0
while var_check and S :
    pre_idx = -1
    for t in T :
        try :
            now_idx = S.index(t)
        except ValueError :
            var_check = False
            break
        if pre_idx > now_idx :
            var_check = False
            break
        pre_idx = now_idx
        del S[now_idx]
    if var_check :
        anser += 1
print(anser)
