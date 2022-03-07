# 문자열이 주어지면 이 문자열을 적절히 축약해서 "UCPC"로 만들 수 있는지 확인하는 프로그램을 만들어보자.
# 첫 번째 줄에 알파벳 대소문자, 공백으로 구성된 문자열이 주어진다. 문자열의 길이는 최대 1,000자이다. 문자열의 맨 앞과 맨 끝에 공백이 있는 경우는 없고, 공백이 연속해서 2번 이상 주어지는 경우도 없다.
S = input()
Goal = "UCPC"
result = "I love UCPC"
for c in Goal :
    idx = S.find(c)
    if idx == -1 :
        result = "I hate UCPC"
        break
    else:
        S = S[idx+1:]
print(result)