import heapq


def get_index(alphabet):
    return ord(alphabet) - 65


def get_alphabet(idx):
    return chr(idx + 65)


def solve():
    name = input()
    amounts = [0] * 26
    palindrome = ""
    middle_alphabet = ""

    for alphabet in name:
        amounts[get_index(alphabet)] += 1

    for _i, amount in enumerate(amounts[::-1]):
        i = 25 - _i
        if not amount:
            continue
        if amount % 2 == 1:
            if middle_alphabet:
                print("I'm Sorry Hansoo")
                return

            middle_alphabet = get_alphabet(i)

        curr_alphabet = get_alphabet(i)
        palindrome = curr_alphabet * (amount // 2) + palindrome + curr_alphabet * (amount // 2)

    if middle_alphabet:
        palindrome = palindrome[:len(palindrome) // 2] + middle_alphabet + palindrome[len(palindrome) // 2:]

    print(palindrome)


if __name__ == '__main__':
    solve()
