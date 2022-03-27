# 한국도로공사는 고속도로의 유비쿼터스화를 위해 고속도로 위에 N개의 센서를 설치하였다.
# 문제는 이 센서들이 수집한 자료들을 모으고 분석할 몇 개의 집중국을 세우는 일인데, 예산상의 문제로, 고속도로 위에 최대 K개의 집중국을 세울 수 있다고 한다.
# 각 집중국은 센서의 수신 가능 영역을 조절할 수 있다. 집중국의 수신 가능 영역은 고속도로 상에서 연결된 구간으로 나타나게 된다.
# N개의 센서가 적어도 하나의 집중국과는 통신이 가능해야 하며, 집중국의 유지비 문제로 인해 각 집중국의 수신 가능 영역의 길이의 합을 최소화해야 한다.
# 편의를 위해 고속도로는 평면상의 직선이라고 가정하고, 센서들은 이 직선 위의 한 기점인 원점으로부터의 정수 거리의 위치에 놓여 있다고 하자.
# 따라서, 각 센서의 좌표는 정수 하나로 표현된다. 이 상황에서 각 집중국의 수신 가능영역의 거리의 합의 최솟값을 구하는 프로그램을 작성하시오.
# 단, 집중국의 수신 가능영역의 길이는 0 이상이며 모든 센서의 좌표가 다를 필요는 없다.
"""
1등 코드가 훨씬 간단하고 빨라서 공부
"""

n = int(input())
m = int(input())
l1 = list(map(int, input().split()))
l1.sort()
#l1 = [1, 3, 6, 6, 7, 9, 12 ,14]
# if n==1 and m==1: # 왜 n이 1이고 m이 1이면 길이의 합 최솟값이 1이지..?  -> 문제 푼 사람이 잘못 생각한듯!
#     print(1)
#
# elif (n ==1):
#     print(0)
#
# elif m ==1 :
#     print(l1[-1]-l1[0])

if (n ==1):
    print(0)

elif m ==1 :
    print(l1[-1]-l1[0])


else :
    diff_list = [l1[i+1] - l1[i] for i in range(len(l1)-1)] # 각 거리차를 리스트로 만들고

    diff_list.sort() # 정렬하고

    for _ in range(m-1): # 왜 m-1일까...?
        diff_list.pop()
    print(sum(diff_list))

"""
위 풀이의 접근 방식을 생각해보자.
[1, 3, 6, 6, 7, 9]
   2  3  0  1  2
범위라고 했으니까.. 결국 관리국의 범위들의 합을 생각해보면 각 지점간의 거리를 서로 더한 값이겠구나
그럼 각 범위마다 있다고 관리국이 있다고 하면
2 3 0 1 2 -> 정렬 : 0 1 2 2 3 
pop을 하는 게, 그 범위를 기준으로 잘라버린 거구나!
위에서는 3이 pop되니까
1 3 // 6 6 7 9 일케 돼서 나머지 합들을 더한 거지!

그러면.. 왜 m-1일까는..
ㅁㅁㅁㅁ
일케 4개로 나눠진 박스를 2 그룹으로 나눌 때 필요한 칸막이의 개수는 1개니까.. m-1한거네! 대박쓰...

핵심은 가장 긴 범위를 버림으로써 구간을 나누는 것이네.
"""

# ___________________________________________________________________________________________________

"""
In :
6
2
1 6 9 3 6 7

Out :
5

위에걸 정렬하면 [1, 3, 6, 6, 7, 9] 일케 되니까
1~3 / 6~9 일케 해서 5인 거 같은데..
이걸 로직을 작성하려면 음..
하나만 더 보자

In :
10
5
20 3 14 6 7 8 18 10 12 15

Out :
7

정렬하면 [3, 6, 7, 8, 10, 12, 14, 15, 18, 20] 이거
5개나 놓을 수 있긴 해
거리가 많이 멀어지는 곳을 기점으로 설치하나..?
그럼 얘는
[3, 6, 7, 8, 10, 12, 14, 15, 18, 20]
   3  1  1  2   2   2   1   3   2
5개 놓을 수 있고..
3 / 6~8 / 10~12 / 14~15 /18~20
0 2 2 1 2 = 7

원래 가장 큰 값을 기준으로 자른다고 하면
3 // 6 7 8 10 12 14 15 // 18 20
2개만 썼으니까 더 쓸 수 있지? 그러니까 그 다음으로 작은 애로 자르면
3 // 6 7 8 // 10 // 12 // 14 15 // 18 // 20

아냐 반대로 접근하자 다 잘려있는데, 거리가 작은 애들끼리 합치는 걸로 관리국 개수랑 맞을 때까지를 생각해보자
그러면 원래
[3 // 6 // 7 // 8 // 10 // 12 // 14 // 15 // 18 // 20]
쓰는 관리국 개수 : 10
이 상태에서 거리가 가장 짧은 애들 합쳐
[3 // 6 7 8 // 10 // 12 // 14 15 // 18 // 20]
쓰는 관리국 개수 : 7
다음으로 짧은 애들 합치자 (이미 합친 애들 제외)
[3 // 6 7 8 // 10  12 // 14 15 // 18  20]
쓰는 관리국 개수 : 5 종료.
만약에 더 작아질 경우에는?
총 거리에서 가장 작은 값을 빼주면 됨

첫번째 걸로 다시 확인
[1 // 3 // 6 // 6 // 7 // 9]
쓰는 관리국 개수 : 6
[1 // 3 // 6  6 // 7 // 9]
쓰는 관리국 개수 : 5
[1 // 3 // 6  6  7 // 9]
쓰는 관리국 개수 : 4
[1  3 // 6  6  7  9]
쓰는 관리국 개수 : 2

이 로직이 맞는 듯 이제 구현 ㄱㄱ
"""

# N = int(input())
# K = int(input())
# Position_list = list(map(int,input().split()))
# Position_list.sort()
#
# distance_list = sorted(list(set([i-j for i,j in zip(Position_list[1:],Position_list[:-1])])))
#
# for d in distance_list :
#     k = 0
#     while True :
#         if k >= len(Position_list)-1 : # Position_list가 계속 바뀔 것이므로 IdexError 발생하지 않게 처리
#             break
#         if len(Position_list) == K : # 원하는 개수의 관리국을 사용
#             break
#
#         if type(Position_list[k+1]) != int :
#             val1 = Position_list[k+1][0]
#             check1 = "l"
#         else:
#             val1 = Position_list[k+1]
#             check1 = "i"
#         if type(Position_list[k]) != int :
#             val0 = Position_list[k][-1]
#             check0 = "l"
#         else:
#             val0 = Position_list[k]
#             check0 = "i"
#
#         if  val1-val0 == d :
#             if check1 == 'l' and check0 == 'i' :
#                 Position_list = [*Position_list[:k], [val0] + Position_list[k + 1], *Position_list[k + 2:]]
#             elif check1 == 'l' and check0 == 'l':
#                 Position_list = [*Position_list[:k], Position_list[k] + Position_list[k + 1], *Position_list[k + 2:]]
#             elif check1 == 'i' and check0 == 'l' :
#                 Position_list = [*Position_list[:k], Position_list[k]+[val1], *Position_list[k+2:]]
#             else:
#                 Position_list = [*Position_list[:k] ,[val0,val1], *Position_list[k + 2:]]
#             k -= 1
#         k += 1
#
# def find_range(v) :
#     if type(v) == int :
#         return 0
#     else:
#         return v[-1]-v[0]
#
# print(sum(map(find_range,Position_list)))