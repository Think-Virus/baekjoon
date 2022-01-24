T = int(input())

def check_count_button(T) :
    if T % 10 :
        return -1

    count_A = T // 300
    count_B = (T-300*count_A) // 60
    count_C = (T-300*count_A-60*count_B) // 10

    return str(count_A) + " " + str(count_B) + " " + str(count_C)

print(check_count_button(T))