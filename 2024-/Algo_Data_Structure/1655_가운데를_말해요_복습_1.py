"""
문제
백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다.
백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다.
만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다.
백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 백준이가 외치는 정수의 개수 N이 주어진다.
N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다.
그 다음 N줄에 걸쳐서 백준이가 외치는 정수가 차례대로 주어진다.
정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

출력
한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력한다.

input
7
1
5
2
10
-99
7
5

출력
1
1
2
2
2
2
5
---
해결 전략
- 매 입력마다 정렬해서 중간값을 찾을까?
    -> N이 100,000이니까 당연히 불가능함
- 본 문제 해결을 위해 '정렬'이 반드시 필요함
    - 그렇다면 가장 빠르고 효율적으로 정렬하는 방법은?
        - Heap!!
- 여기까지는 PS를 연습해본 이라면 어렵지 않게 도출할 수 있다. 그러나, 문제는 그 다음이다.
    - "Heap을 사용해볼까"라는 생각이 들었을 때, 많은 이들이 다음과 같은 간단한 Idea를 떠올려볼 것이다.
    - 무언가 중간 지점을 의미하는 Value를 두고, 그 값을 기준으로 Heap을 구축해볼까?
        - Value가 매 입력마다 바뀌기 때문에 결국 Linearity가 추가되고, 시간 초과가 날 것이다.
    - STL Heap을 사용하지 말고, 직접 Heap을 구축한 다음, Tree에서의 높이를 따져서 중간값을 찾아볼까?
        - 높이와 원소 개수만으로는 선형 코딩 없이 중간값을 특정하기 어렵다.
    - 위 과정을 통해 Heap 아이디어를 폐기함
-But, Max Heap과 Min Heap을 동시에 두고, 마치 모래시계처럼 구조를 설계한다면?
    - 그 다음, 매 입력마다 항상 Max Heap과 Min Heap의 원소 개수 차이가 1이하가 되도록(Max가 더 많게) 만들어주고,
      동시에 항상 Min Heap의 Top 원소가 Max Heap의 Top 원소보다 크도록 만들어준다.

"""
import sys
import heapq


def print_mid(numbers: list[int]) -> None:
    max_heap = []
    min_heap = []

    for number in numbers:
        if not max_heap or number <= -max_heap[0]:
            heapq.heappush(max_heap, -number)
        else:
            heapq.heappush(min_heap, number)

        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        print(-max_heap[0])
    return


def main():
    n = int(sys.stdin.readline())
    numbers = [int(sys.stdin.readline()) for _ in range(n)]

    print_mid(numbers)


if __name__ == "__main__":
    main()
