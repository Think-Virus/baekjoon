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

anser = 0
var_while_check = True
while S and var_while_check :
    tmp = ""
    find_idx = 0
    for t in T :
        if S.count(t) == 0 :
            var_while_check = False
            break

        tmp_idx = -1
        for s in S[find_idx:] :
            tmp_idx += 1
            if t == s and tmp.find(t) == -1 :
                find_idx = tmp_idx
                del S[S.index(t)]
                tmp += t
    if T == tmp :
        anser += 1
    else:
        var_while_check = False
        break
print(anser)