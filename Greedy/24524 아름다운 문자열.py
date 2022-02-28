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
from collections import defaultdict

S_dict = defaultdict(list)
for i,s in enumerate(input()) :
    S_dict[s].append(i)
T = input()

var_check = True
anser = 0

while var_check and S_dict :
    pre_idx = -1
    for t in T :
        if not S_dict.get(t) :
            var_check = False
            break
        now_idx = S_dict.get(t).pop(0)
        if now_idx < pre_idx :
            var_check = False
            break
        else:
            pre_idx = now_idx
    if var_check :
        anser += 1
print(anser)
