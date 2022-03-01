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
    tmp_list = []
    for t in T :
        try :
            tmp_list.append(S.index(t))
        except ValueError :
            var_check = False
            break
    if tmp_list != sorted(tmp_list) :
        var_check = False
        break

    if var_check :
        anser += 1
        for i in tmp_list[::-1] :
            del S[i]
print(anser)
