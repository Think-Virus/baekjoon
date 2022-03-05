# N개의 물병
# 각 물병에는 물을 무한대로 부을 수 있다.
# 처음에 모든 물병에는 물이 1리터씩 들어있다.
# 지민이는 이 물병을 또 다른 장소로 옮기려고 한다. 지민이는 한 번에 K개의 물병을 옮길 수 있다.
# 지민이는 물을 낭비하기는 싫고, 이동을 한 번보다 많이 하기는 싫다.
# 지민이는 물병의 물을 적절히 재분배해서, K개를 넘지 않는 비어있지 않은 물병을 만들려고 한다.
# -> 먼저 같은 양의 물이 들어있는 물병 두 개를 고른다. 그 다음에 한 개의 물병에 다른 한 쪽에 있는 물을 모두 붓는다. 이 방법을 필요한 만큼 계속 한다.
# 이런 제약 때문에, N개로 K개를 넘지않는 비어있지 않은 물병을 만드는 것이 불가능할 수도 있다.
# 다행히도, 새로운 물병을 살 수 있다. 상점에서 사는 물병은 물이 1리터 들어있다.

# 첫째 줄에 상점에서 사야하는 물병의 최솟값을 출력한다. 만약 정답이 없을 경우에는 -1을 출력한다.

# 그냥 반복문으로 하니까 속도가 곱창나네... 함수 만들어서 map으로 처리하는 게 맞을 듯..?

N,K = map(int,input().split())
Bottle_list = [1]*N

# K를 *2^n 해서 원하는 수를 만들어야 할듯
# 합쳐야만 가능할 수도 있고 안합치고도 될 수 있음

anser = 0
while True :
    Bottle_list.sort(reverse=True)
    candidate_list = []
    if len(Bottle_list) <= K:  # 결과
        break

    while True :
        Bottle = Bottle_list.pop()
        if Bottle_list.count(Bottle) >= 1 :
            end_idx = Bottle_list.index(Bottle)
            Bottle_Cnt = Bottle_list.count(Bottle) + 1
            share_Cnt = Bottle_Cnt // 2
            remain_Cnt = Bottle_Cnt % 2
            Bottle_list = Bottle_list[:end_idx]
            Bottle_list += [2*Bottle]*share_Cnt + [Bottle] * remain_Cnt
        else:
            candidate_list.append(Bottle)
        if not Bottle_list :
            break

    Bottle_list += candidate_list
    if len(Bottle_list) <= K : #결과
        break

    Bottle_list.append(1)
    anser +=1

print(anser)