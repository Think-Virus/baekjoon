# N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)
# 둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.
"""
tmp = input().split()
N,K = tmp[0],int(tmp[1])
Val = list(input())
Sorted_val = sorted(Val)

for i in Sorted_val[:K] :
    Val.remove(i)
print("".join(Val))

위와 같이 할 경우, 아래 경우를 처리 못함
In :
10 4
4177252841
Out :
775841
"""

tmp = input().split()
N,K = int(tmp[0]),int(tmp[1])+1
Val = list(input())

# 입력 값이 500000까지 가능하므로 이중 for문이면 O(n)이므로 안됨
result_val = ""
while len(result_val) <= N-K-1 :
    if K == 1 :
        result_val += "".join(Val)
        break
    tmp = Val[:K]
    result_idx = tmp.index(max(tmp))
    result_val += max(tmp)
    K -= result_idx
    Val = Val[result_idx+1:]
print(result_val)