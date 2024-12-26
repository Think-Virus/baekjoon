# 백준이는 방 청소를 하면서 필요 없는 전공 서적을 사람들에게 나눠주려고 한다.
# 나눠줄 책을 모아보니 총 N권이었다. 책이 너무 많기 때문에 백준이는 책을 구분하기 위해 각각 1부터 N까지의 정수 번호를 중복되지 않게 매겨 두었다.
# 조사를 해 보니 책을 원하는 서강대학교 학부생이 총 M명이었다. 백준이는 이 M명에게 신청서에 두 정수 a, b (1 ≤ a ≤ b ≤ N)를 적어 내라고 했다.
# 그러면 백준이는 책 번호가 a 이상 b 이하인 책 중 남아있는 책 한 권을 골라 그 학생에게 준다.
# 만약 a번부터 b번까지의 모든 책을 이미 다른 학생에게 주고 없다면 그 학생에게는 책을 주지 않는다.
# 백준이가 책을 줄 수 있는 최대 학생 수를 구하시오

"""
첫째 줄에 테스트 케이스의 수가 주어진다.
각 케이스의 첫 줄에 정수 N(1 ≤ N ≤ 1,000)과 M(1 ≤ M ≤ 1,000)이 주어진다.
다음 줄부터 M개의 줄에는 각각 정수 ai, bi가 주어진다. (1 ≤ ai ≤ bi ≤ N)

In :
1
2 3
1 2
1 2
1 2

Out :
2
"""
import sys
for _ in range(int(sys.stdin.readline())) :
    N,M = map(int,sys.stdin.readline().split())
    book_list = [0 for i in range(N)]
    people_list = []

    for _ in range(M):
        people_list.append(list(map(int,sys.stdin.readline().split())))

    people_list.sort(key=lambda x:(x[1],x[0]))
    ans = 0
    for person in people_list :
        if book_list[person[0]-1:person[1]].count(0) != 0 :
            idx = person[0] - 1 + book_list[person[0] - 1:person[1]].index(0)
            book_list[idx] = 1
            ans += 1

    print(ans)


