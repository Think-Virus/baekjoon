S = input()
last_c = S[0]
s0 = 0
s1 = 0

for c in S[1:] :
    if c != last_c :
        if last_c == '1' :
            s1 += 1
        else :
            s0 += 1
        last_c = c
        continue
if last_c == '1' :
    s1 += 1
else :
    s0 += 1
print(min(s0,s1))
