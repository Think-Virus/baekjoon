# PPAP 문자열은 문자열 P에서 시작하여, 문자열 내의 P를 PPAP로 바꾸는 과정을 반복하여 만들 수 있는 문자열로 정의된다.
# 정확하게는 다음과 같이 정의된다.
    # P는 PPAP 문자열이다.
    # PPAP 문자열에서 P 하나를 PPAP로 바꾼 문자열은 PPAP 문자열이다.

# 예를 들어 PPAP는 PPAP 문자열이다. 또한, PPAP의 두 번째 P를 PPAP로 바꾼 PPPAPAP 역시 PPAP 문자열이다.

# 문자열이 주어졌을 때, 이 문자열이 PPAP 문자열인지 아닌지를 알려주는 프로그램을 작성하여라.
p = input()

while p.find('A') != -1 and p.find('PPAP') != -1 : # A가 있으면 그를 PPAP -> P 로 수정해보고 마지막에 확인..?
    s_idx = p.find('PPAP')
    p = p[:s_idx] + 'P' + p[s_idx+4:]

if p.find('A') != -1 :
    if p.find('PPAP') != -1 :
        print("PPAP")
    else:
        print("NP")
else:
    print("PPAP")