"""
문제
    세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
    그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
    괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

입력
    첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다.
    그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다.
    수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

출력
    첫째 줄에 정답을 출력한다.

55-50+40

-35

10+20+30+40
100

00009-00009
0
---
접근법
    -가 나온 적 없으면 (를 열어줌
    이후에 -가 나오면 )를 닫고 sum에 빼줌
"""


def solve():
    input_line = input()
    minus_input_list = input_line.split('-')
    result = 0

    for i, sub in enumerate(minus_input_list):
        plus_input_list = list(map(int, sub.split('+')))
        sub_sum = 0
        for n in plus_input_list:
            sub_sum += n

        if i == 0:
            result = sub_sum
        else:
            result -= sub_sum

    print(result)


if __name__ == '__main__':
    solve()
