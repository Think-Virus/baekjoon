N = int(input())
Distance_list = input("")
Price_list = input("")
Distance_list = list(map(int, Distance_list.split(" ")))
Price_list = list(map(int, Price_list.split(" ")))[:-1] # 마지막 도시에서 기름을 넣을 필요가 없음

total_price = 0
min_price = Price_list[0]
for k in range(N-1) :
    distance = Distance_list[k]
    price = Price_list[k]
    if price < min_price :
        min_price = price
    total_price = total_price + distance * min_price

print(total_price)