# 5
# 1 1 1 6 0
# 2 7 8 3 1

n = int(input())
A_list = input("")
B_list = input("")

A_list = list(map(int, A_list.split(" ")))
B_list = list(map(int, B_list.split(" ")))

A_dict = {i:val for i,val in enumerate(A_list)}
A_list= sorted(A_dict.items(), key=lambda x : x[1])

B_dict = {i:val for i,val in enumerate(B_list)}
B_list = sorted(B_dict.items(), key=lambda x : x[1], reverse=True)

anser = 0
for i in range(n) :
    anser = anser + A_list[i][1] * B_list[i][1]

print(anser)

# 내가 짠 코드는 72ms / 30864kb 였는데 아래 코드는 52ms에 29284kb임
# B를 sorting하지 않고 최대값 뽑아서 계산한 거여서 빠른 듯
# N = int(input())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# def min(A,B):
#     sum = 0
#     A.sort()
#     for i in A:
#         t = max(B)
#         sum += i*t
#         B.pop(B.index(t))
#     return print(sum)
# min(A,B)