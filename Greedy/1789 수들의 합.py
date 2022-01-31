# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값
# 200 -> 19
S = int(input())
minus_val = 0
while S :
    minus_val +=1
    S = S - minus_val
    if S <= minus_val :
        break
print(minus_val)