usr = int(input(""))
time_str = input("")

time_list = list(map(int, time_str.split(" ")))
time_list.sort()
sum_time = 0

for i in range(usr) :
    sum_time = sum_time + sum(time_list[:i+1])

print(sum_time)