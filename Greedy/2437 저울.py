import sys

N = int(sys.stdin.readline())
Weight = list(map(int,sys.stdin.readline().split()))
Weight.sort()
Anser = 0
Find_check = False

while not Find_check :
    Anser += 1
    tmp = Anser
    Find_check = True
    for i in range(N) :
        if tmp in Weight[i:] :
            Find_check = False
            break
        elif tmp < 0 :
            Find_check = False
            break
        elif tmp == 0 :
            Find_check = True
            break            
        tmp -= Weight[i]
print(Anser)