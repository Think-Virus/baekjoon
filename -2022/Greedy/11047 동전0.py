kind_N_goal = input("")

var_kind = list(map(int, kind_N_goal.split(" ")))[0]
var_goal = list(map(int, kind_N_goal.split(" ")))[1]
list_kind = []

for _ in range(var_kind) :
    list_kind.append(int(input()))

def min_number_of_coin(pay,coin_list) :
    coin_dic = {kind : 0 for kind in reversed(coin_list)}
    total = 0
    for amount in coin_dic.keys() :
        if pay >= amount :
            coin_dic[amount] = pay // amount
            pay = pay - amount * coin_dic[amount]
    for count in coin_dic.values() :
        total = total+count
    return total

print(min_number_of_coin(var_goal,list_kind))