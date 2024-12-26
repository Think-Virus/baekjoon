# 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 최소 개수

payment = int(input())

def min_charge(pay) :
    bill_dic =  {500 : 0, 100 : 0, 50 : 0, 10 : 0, 5 : 0, 1 : 0}
    total = 0
    charge = 1000 - pay
    for amount in bill_dic.keys() :
        if charge >= amount :
            bill_dic[amount] = charge // amount
            charge = charge - amount * bill_dic[amount]
    for count in bill_dic.values() :
        total = total+count
    return total

print(min_charge(payment))

# 아래 거처럼 간단한 게 더 빠른 것도 있구나..
# a=int(input())
# b=1000-a
# c=b//500
# d=b%500//100
# e=b%100//50
# f=b%50//10
# g=b%10//5
# h=b%5
# print(c+d+e+f+g+h)