usr = int(input(""))
time_str = input("")

time_list = list(map(int, time_str.split(" ")))
time_list.sort()
sum_time = 0

for i in range(usr):
    sum_time = sum_time + sum(time_list[:i + 1])

print(sum_time)

# 코드 감 살리기
N = int(input(""))
Pi = input("")
S = 0

# Pi = list(map(int, sorted(Pi.split(" "))))
# 이유는 모르겠지만, 백준에서 sorted는 틀림으로 책점됨
Pi = list(map(int, Pi.split(" ")))
Pi.sort()

for i in range(N):
    S = S + sum(Pi[:i + 1])

print(S)
