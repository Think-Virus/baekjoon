# 길이가 N인 수열이 주어졌을 때, 그 수열의 합
# 하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라, 수열의 두 수를 묶으려고 함
# 위치에 상관없이 묶을 수 있음
# 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능
# 어떤 수를 묶게 되면, 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더함
# ex) 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다. 하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(2*3)+(4*5) = 27이 되어 최대가 된다.
# 수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.
# 합이 최대가 되게 하는 프로그램 작성

# 생각한 로직
# 양수 값들은 큰 값들끼리 곱해서 진행하면 되고 O(1/2N)
# 음수는 절대값이 큰 값들끼리 곱해서 마지막에 둘을 합침
import sys
N = int(sys.stdin.readline())
Minus_Seq = []
Plus_Seq = []
Seq_Sum = 0

for _ in range(N) :
    Input_val = int(sys.stdin.readline())
    if Input_val > 0 :
        Plus_Seq.append(Input_val)
    else:
        Minus_Seq.append(Input_val)

Plus_Seq.sort()
for _ in range(len(Plus_Seq)//2) :
    first_val = Plus_Seq.pop()
    second_val = Plus_Seq.pop()
    if first_val + second_val > first_val*second_val :
        Seq_Sum = Seq_Sum + first_val + second_val
    else:
        Seq_Sum = Seq_Sum + first_val*second_val
if Plus_Seq :
    Seq_Sum = Seq_Sum + Plus_Seq.pop()

Minus_Seq.sort(reverse=True)
for _ in range(len(Minus_Seq)//2) :
    Seq_Sum = Seq_Sum + Minus_Seq.pop() * Minus_Seq.pop()
if Minus_Seq :
    Seq_Sum = Seq_Sum + Minus_Seq.pop()

print(Seq_Sum)