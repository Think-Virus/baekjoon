#     +---+
#     | D |
# +---+---+---+---+
# | E | A | B | F |
# +---+---+---+---+
#     | C |
#     +---+
# 주사위는 위와 같이 생겼다. 주사위의 여섯 면에는 수가 쓰여 있다. 위의 전개도를 수가 밖으로 나오게 접는다.
# A, B, C, D, E, F에 쓰여 있는 수가 주어진다.
# 지민이는 현재 동일한 주사위를 N^3개 가지고 있다.
# 이 주사위를 적절히 회전시키고 쌓아서, N×N×N크기의 정육면체를 만들려고 한다. 이 정육면체는 탁자위에 있으므로, 5개의 면만 보인다.
# N과 주사위에 쓰여 있는 수가 주어질 때, 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램을 작성하시오.

"""
완벽한 하나의 공식이 있다고 생각했는데 아닌듯..
풀이법 :
3면이 보이는 주사위 : 4개
2면이 보이는 주사위 : (N-2)*4 + (N-1)*4
1면이 보이는 주사위 : (N-2)*(N-2) + (N-1)*(N-2)*4

-> 3면 최소 조합, 2면 최소조합, 1면 최소 값을 구해야 함
"""
N = int(input())
dice_val = list(map(int,input().split()))
idx = 0
dice_val = [[v,i] for i,v in enumerate(dice_val)]

# 맞은 편에 있는 것만 나올 수 없음 -> 즉, A & F // B & E // D & C -> idx로 치면 0 5 // 1 4 // 2 3 -> idx를 합쳤을 때, 5가 되면 안되네..
# 1면이 보이는 주사위의 합
first_min_val = min(dice_val, key=lambda x:x[0])
one_face_sum = first_min_val[0]*((N-2)*(N-2) + (N-1)*(N-2)*4)

# 2면이 보이는 주사위의 합
second_min_val = [51,7]
for dice in dice_val :
    if first_min_val == dice :
        continue
    else :
        if dice[0] < second_min_val[0] and dice[1]+first_min_val[1] != 5 :
            second_min_val = dice
two_face_sum = (first_min_val[0]+second_min_val[0])*((N-2)*4 + (N-1)*4)

# 3면이 보이는 주사위의 합
third_min_val = [51,7]
for dice in dice_val :
    if first_min_val == dice or second_min_val == dice :
        continue
    else :
        if dice[0] < third_min_val[0] and dice[1]+first_min_val[1] != 5 and dice[1]+second_min_val[1] != 5 :
            third_min_val = dice
three_face_sum = (first_min_val[0]+second_min_val[0]+third_min_val[0])*4

print(one_face_sum+two_face_sum+three_face_sum)