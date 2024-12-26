# 팰린드롬 -> 회문
# 첫째 줄에 문제의 정답을 출력한다. 만약 불가능할 때는 "I'm Sorry Hansoo"를 출력한다. 정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력한다.
Alphabet_list = list(input())
Alphabet_list.sort(reverse=True)
Alphabet_set = sorted(set(Alphabet_list),reverse=True)

result = ""
remain_val = []
for alphabet in Alphabet_set :
    if Alphabet_list.count(alphabet) % 2 == 0 :# 짝수개 있을 때
        tmp = alphabet*(Alphabet_list.count(alphabet)//2)
        result = tmp + result + tmp
    else: # tmp
        tmp = alphabet*(Alphabet_list.count(alphabet)//2)
        result = tmp + result + tmp
        if not remain_val :
            remain_val.append(alphabet)
        else:
            print("I'm Sorry Hansoo")
            exit()
    Alphabet_list = [i for i in Alphabet_list if i != alphabet]

if remain_val :
    mid_idx = len(result)//2
    result = result[:mid_idx]+remain_val[0]+result[mid_idx:]
print(result)