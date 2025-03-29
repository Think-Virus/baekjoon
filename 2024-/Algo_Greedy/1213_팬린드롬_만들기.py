import heapq


def solve():
    name = input()
    alphabets = []
    for alphabet in name:
        heapq.heappush(alphabets, alphabet)

    result = []
    middle_alphabet = ""
    while alphabets:
        start = heapq.heappop(alphabets)
        end = heapq.heappop(alphabets)

        if not end:  # final
            middle_alphabet = end
        else:
            if start != end:
                print("I'm Sorry Hansoo")
                return
            else:
                result.append(start)

    palindrome = ''
    for alphabet in result:
        palindrome += alphabet
    palindrome += middle_alphabet
    for alphabet in result[::-1]:
        palindrome += alphabet

    print(palindrome)


if __name__ == '__main__':
    solve()
