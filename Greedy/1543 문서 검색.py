# 1등 코드 대박..
print(input().count(input()))

# 영어로만 이루어진 어떤 문서를 검색하는 함수
# 이 함수는 어떤 단어가 총 몇 번 등장하는지 세려고 함
# but 함수는 중복되어 세는 것은 빼고 세야 한다
# ex) 문서가 abababa이고, 그리고 찾으려는 단어가 ababa라면 이 단어를 0과 2에서 찾을 수 있음 -> 이를 1개로 해야 함

doc = input()
word = input()
word_len = len(word)
answer = 0

while True :
    tmp = doc.find(word)
    if tmp == -1 :
        break
    answer += 1
    doc = doc[tmp+word_len:]

print(answer)
