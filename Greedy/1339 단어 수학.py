# 답 코드 확인
# 생각한 로직 자체는 맞았는데, 코드가 잘못되었음
import sys

n = int(sys.stdin.readline())

alpha = [] # 단어를 저장할 리스트
alpha_dict = {} # 단어 내의 알파벳별로 수를 저장할 딕셔너리
numList = [] # 수를 저장할 리스트

for i in range(n): # 단어를 입력받음
    alpha.append(sys.stdin.readline().rstrip())

for i in range(n): # 모든 단어에 대해서
    for j in range(len(alpha[i])): # 단어의 길이만큼 실행
        if alpha[i][j] in alpha_dict: # 단어의 알파벳이 이미 dict에 있으면
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i])-j-1) # 자리에 맞게 추가 ( 1의 자리면 1 )
        else:   # 자리에 없으면 새로 추가 ( 10의 자리면 10 )
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)

for val in alpha_dict.values(): # dict에 저장된 수들을 모두 리스트에 추가
    numList.append(val)

numList.sort(reverse=True) # 수들을 내림차순 정렬

sum = 0
pows = 9
for i in numList: # 첫 번째 부터 가장 큰 부분을 차지하므로 9를 곱해준다
    sum += pows * i
    pows -= 1
# 내려갈수록 그 알파벳이 차지하는 비중이 적으므로 -1
print(sum)

# 틀림
# import operator
# import sys
# from collections import defaultdict
#
# N = int(sys.stdin.readline().rstrip())
# val_list =[]
# val_index_list = []
#
# for _ in range(N) :
#     tmp = sys.stdin.readline().rstrip()
#     val_list.append(tmp)
# val_list.sort(key=lambda x:len(x), reverse=True) # 길이가 긴 것부터 정렬
#
# max_len = len(val_list[0])
# alphabet_idx_dict = defaultdict(list)
# for char_val in val_list :
#     tmp_idx = max_len - len(char_val)
#     for c in char_val :
#         alphabet_idx_dict[c].append(tmp_idx)
#         tmp_idx += 1
# alphabet_idx_dict = dict(sorted(alphabet_idx_dict.items(), key=operator.itemgetter(1)))
# val_int = 10
# S = 0
#
# for a in alphabet_idx_dict.keys() :
#     val_int -=1
#     for i in alphabet_idx_dict[a] :
#         S += val_int*10**(max_len-1-i)
# print(S)


# 접근법에 오류 존재
# from collections import defaultdict
# alphabet_dict = defaultdict(int)
# int_val = 10
# val_sum = 0
# for char_val in val_list :
#     tmp_mul = 10**(len(char_val)-1)
#     for c in char_val :
#         if alphabet_dict.get(c) is None : #딕셔너리에 값이 없을 경우
#             int_val -= 1
#             alphabet_dict[c] = int_val
#             val_sum += alphabet_dict[c] * tmp_mul
#         else:
#             val_sum +=  alphabet_dict[c] * tmp_mul
#         tmp_mul = tmp_mul//10
# print(alphabet_dict)
# print(val_sum)
