# 하루에 한 과제를 끝냄
# 과제마다 마감일이 있으므로 모든 과제를 끝내지 못할 수도 있음
# 과제마다 끝냈을 때 얻을 수 있는 점수가 있는데, 마감일이 지난 과제는 점수를 받을 수 없다.
"""
In :
7
4 60
4 40
1 20
2 50
3 30
4 10
6 5
Out :
185
"""

"""
해결 방법 :
그래서 최대한 마감일에 가깝게! 처리하는 것이 중요합니다.

이를 나타내보면,

점수가 가장 큰 (4, 60)은 넷째 날

그 다음 큰 (2, 50)은 둘째 날

그 다음 큰 값인 (4, 40)은 넷째 날에 할 수 없으므로 셋째 날

그 다음 (3, 30)은 셋째 날에 할 수 없으므로 첫째 날

(1, 20)은 첫째 날에 할수 없으므로 포기합니다.
[출처] [파이썬 알고리즘] Greedy 예제 / BOJ 13904 / 백준 130904|작성자 namucoding_pohang
"""
import sys

N = int(sys.stdin.readline())
arr = []
answer = [0 for _ in range(1000)]

for _ in range(N) :
    arr.append(list(map(int,sys.stdin.readline().split())))

arr.sort(key=lambda x:x[1],reverse=True)

for i in range(N) :
    for j in range(arr[i][0]-1,-1,-1) :
        if answer[j] == 0 :
            answer[j] = arr[i][1]
            break
print(sum(answer))





