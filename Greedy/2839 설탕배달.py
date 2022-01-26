# N = int(input())
# case_5 = N // 5
#
# if N < 5:
#     if N % 3 != 0:
#         print(-1)
#     else:
#         print(N % 3)
#
# elif (N - 5 * case_5) % 3 == 0:
#     case_3 = (N - 5 * case_5) // 3
#     print(case_5 + case_3)
#
# else:
#     M = N
#     for i in range(0, case_5):
#         M = N - 5 * i
#         if M < 0:
#             print(-1)
#             break
#         elif M % 3 == 0:
#             case_3 = (N - 5 * i) // 3
#             print(i + case_3)
#             break


#N = int(input())
# def sugar_delivery(N) :
#     tmp_list = []
#     case_5 = N // 5
#     tmp_var = 0
#
#     if N == 0 :
#         return tmp_list, -1
#     if N < 5:
#         if N % 3 != 0:
#             return tmp_list, -1
#         elif N % 3 == 0:
#             tmp_list.append(3)
#             return tmp_list, 1
#     elif (N - 5 * case_5) % 3 == 0:
#         case_3 = (N - 5 * case_5) // 3
#         for _ in range(case_5) :
#             tmp_list.append(5)
#         for _ in range(case_3) :
#             tmp_list.append(3)
#         return tmp_list, case_5 + case_3
#     else:
#         M = N
#         for i in range(case_5-1, -1 , -1):
#             M = N - 5 * i
#             if M < 0:
#                 return tmp_list, -1
#                 break
#             elif M % 3 == 0:
#                 tmp_var = 0
#                 case_3 = (N - 5 * i) // 3
#                 for _ in range(i):
#                     tmp_list.append(5)
#                 for _ in range(case_3):
#                     tmp_list.append(3)
#                 return tmp_list, i + case_3
#                 break
#             else :
#                 tmp_var = -1
#     if tmp_var :
#         return tmp_list, tmp_var

def sugar_delivery(N) :
    case_5 = N // 5
    tmp_var = 0

    if N == 0 :
        return -1
    if N < 5:
        if N % 3 != 0:
            return -1
        elif N % 3 == 0:
            return 1
    elif (N - 5 * case_5) % 3 == 0:
        case_3 = (N - 5 * case_5) // 3
        return case_5 + case_3
    else:
        M = N
        for i in range(case_5-1,-1,-1):
            M = N - 5 * i
            if M < 0:
                return -1
                break
            elif M % 3 == 0:
                tmp_var = 0
                case_3 = (N - 5 * i) // 3
                return i + case_3
                break
            else :
                tmp_var = -1
    if tmp_var :
        return tmp_var

for N in range(50) :
    print(N,":", end='')
    print(sugar_delivery(N))
