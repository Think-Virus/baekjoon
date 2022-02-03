#55-50+40-35+30
val_list = [*map(int,input().replace("+", " +").replace("-"," -").split())]
result = 0
change_point = 0
for i in val_list :
    if i < 0 :
        result += i
        change_point = 1
    else:
        if change_point == 0 :
            result += i
        else:
            result -= i
print(result)

# 1등 정답 코드 -> -를 기준으로 값을 나눠서 진행했네.. 대박
e = [sum(map(int, x.split('+'))) for x in input().split('-')]
print(e)
print(e[0]-sum(e[1:]))

# new_formula = []
# start_point = 0
# var_count = 0
# for i in range(len(formula)) :
#     if formula[i] == "-" :
#         if var_count%2 == 0 :
#             new_formula.append(str(int(formula[start_point:i])))
#             new_formula.append("-(")
#         else:
#             new_formula.append(str(int(formula[start_point:i])))
#             new_formula.append(")-(")
#         start_point = i + 1
#         var_count += 1
#     elif formula[i] == "+" :
#         new_formula.append(str(int(formula[start_point:i])))
#         new_formula.append("+")
#         start_point = i + 1
# new_formula.append(str(int(formula[start_point:len(formula)])))
# new_formula = "".join(new_formula)
# if var_count :
#     new_formula = new_formula + ")"
# print(eval(new_formula))

# 런타임 에러
# formula = input()
# var_idx = 0
# symbol_dic = {}
# new_formula = []
# var_count = 0
# for i in range(len(formula)) :
#     if formula[i] == "+" or formula[i] == "-" :
#         symbol_dic[var_idx] = formula[i]
#         var_idx += 1
# value_list = list(map(int,formula.replace("-","/").replace("+","/").split("/")))
# length = len(value_list)
# for k in range(length) :
#     new_formula.append(str(value_list[k]))
#     if length-1-k :
#         var_symbol = symbol_dic.get(k)
#         if var_symbol == '-' :
#             if var_count % 2 == 0:
#                 new_formula.append(var_symbol)
#                 new_formula.append("(")
#             else:
#                 new_formula.append(")-(")
#             var_count += 1
#         else:
#             new_formula.append(var_symbol)
# new_formula = "".join(new_formula)
# if var_count :
#     new_formula = new_formula + ")"
# print(eval(new_formula))


# new_formula = [*sum(zip(value_list,symbol_dic.values()),())]
# print(new_formula)

# for i in formula :
#     if i == '-' :
#         idx += 1
#         if var_count%2 == 0 :
#             formula = formula[:idx] + "(" + formula[idx:]
#         else:
#             formula = formula[:idx-1] + ")-(" + formula[idx:]
#         var_count += 1
#     idx += 1
# if var_count :
#     formula = formula + ")"
# print(eval(formula))

# formula = "55-50+40" #input()
# # formula = formula.replace("-","-1*(")
# # print(formula)
# minus_idx = []
# new_formula = ""
# var_count = 0
# idx = 0
# for i in formula :
#     print(i)
#     print()
#     if i == '-' :
#         idx += 1
#         if var_count%2 == 0 :
#             formula = formula[:idx] + "(" + formula[idx:]
#         else:
#             formula = formula[:idx-1] + ")-(" + formula[idx:]
#         var_count += 1
#     idx += 1
# if var_count :
#     formula = formula + ")"
#
# print(eval(formula))

# formula = formula.replace("+", " + ").replace("-"," - ")
# formula_list = formula.split()
#
# for i in formula_list :
#     if
