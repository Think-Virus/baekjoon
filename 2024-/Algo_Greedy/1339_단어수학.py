"""
문제
    민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.
    단어 수학 문제는 N개의 단어로 이루어져 있으며,
    각 단어는 알파벳 대문자로만 이루어져 있다.
    이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다.
    같은 알파벳은 같은 숫자로 바꿔야 하며,
    두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.
    예를 들어, GCF + ACDEB를 계산한다고 할 때,
    A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면,
    두 수의 합은 99437이 되어서 최대가 될 것이다.
    N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

입력
    첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다.
    둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다.
    단어는 알파벳 대문자로만 이루어져있다.
    모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8이다.
    서로 다른 문자는 서로 다른 숫자를 나타낸다.

출력
    첫째 줄에 주어진 단어의 합의 최댓값을 출력한다.

3
GCF
ACDEB
CD
---
접근법
    자릿수가 큰 알파벳에 무조건 큰 수를 적용하는 게 답 아닐까?
    ABC
    DD
    986
    77
    이렇게 될 수가 있음
    같은 자리라면, 중복되는 알파벳에 큰 값을 적용하는 게 좋을듯
    길이가 긴 친구들부터 정렬하는 게 좋을 듯 함
    길이가 같아지는 순간 빼놓고 할까? -> 다른 애들을 계속 확인해야 하므로 불가능
    시간도 2초이니 살짝 넉넉함
    find를 매번 돌리면 n^2까지 될 수도 있음
    처음 추가할 때, 중복인 것을 체크할까? -> n^2가 될 듯
"""
import sys


class Alphabet:
    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.count = 0


def input_data() -> list[Alphabet]:
    n = int(sys.stdin.readline())
    alphabets: list[Alphabet] = []
    for _ in range(n):
        word = sys.stdin.readline().strip()
        place = 0
        for i in range(len(word) - 1, -1, -1):
            is_in = False
            for alphabet in alphabets:
                if alphabet.alphabet == word[i]:
                    alphabet.count += 10 ** place
                    is_in = True
                    break
            if not is_in:
                new_alphabet = Alphabet(word[i])
                new_alphabet.count = 10 ** place
                alphabets.append(new_alphabet)
            place += 1

    return alphabets


def solve():
    alphabets = input_data()
    result = 0
    max_num = 9

    alphabets.sort(key=lambda x: -x.count)
    for alphabet in alphabets:
        result += alphabet.count * max_num
        max_num -= 1

    print(result)


if __name__ == '__main__':
    solve()
