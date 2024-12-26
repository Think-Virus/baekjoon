# 전구 N개를 가지고 있다. 전구는 1번부터 N번까지 번호가 매겨져 있으며, 일렬로 놓여져 있다. 전구는 켜져있거나 꺼져있다.
# 모든 전구를 끄려고 한다.
# 강호는 전구를 켜고 끌 수 있는 스위치 N개를 가지고 있고, 스위치도 1번부터 N번까지 번호가 매겨져 있다.
# i번 스위치는 i의 배수 번호를 가지는 전구의 상태를 모두 반전시킨다.
# 모든 전구를 끄기 위해서 스위치를 몇 번 눌러야 하는지 출력한다. 만약, 모든 전구를 끌 수 없다면 -1을 출력한다.
Light_bulbs = input()
def change_int(val) :
    if val == "Y" :
        return 1
    else:
        return 0
Light_bulbs = list(map(change_int,Light_bulbs))

def change_status(iter) :
    idx, val = iter[0]+1,iter[1]
    if idx % i == 0 :
        return (val + 1)% 2
    else:
        return val

Cnt = 0
global i
for i in range(1,len(Light_bulbs)+1) :
    if Light_bulbs.count(1) == 0 :
        break
    else:
        if Light_bulbs[i-1] == 1 :
            Cnt += 1
            Light_bulbs = list(map(change_status,enumerate(Light_bulbs)))

if Light_bulbs.count(1) == 0 :
    print(Cnt)
else:
    print(-1)

