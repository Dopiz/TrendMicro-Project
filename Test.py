import re

# def solution(S, C):
#     name_list = re.split(';', S)
#     res_list = []

#     for name in name_list:
#         n = re.split(' ', name)
#         n = [i.lower() for i in n if i != '']

#         for i in range(len(n)):
#             if not n[i].isalpha():
#                 S = ""
#                 for c in n[i]:
#                     if c.isalpha():
#                         S += c
#                 n[i] = S

#         if len(n) == 2:
#             mail = "{}_{}@{}.com".format(n[1], n[0], C)
#             num = 1
#             while mail in res_list:
#                 num = num + 1
#                 mail = "{}_{}{}@{}.com".format(n[1], n[0], num, C)

#             res_list.append(mail)
        
#         elif len(n) == 3:
#             mail = "{}_{}_{}@{}.com".format(n[2], n[0], n[1][0], C)
#             num = 1
#             while mail in res_list:
#                 num = num + 1
#                 mail = "{}_{}_{}{}@{}.com".format(n[2], n[0], n[1][0], num, C)

#             res_list.append(mail)

#     return res_list


# S = 'aa bb cc; xx yy Z-z; aa bb; aa bx cc'
# C = 'test'

# print(solution(S, C))


def solution(S, C):
    
    res_list = []

    for full_name in S:
        name = re.split(' ', full_name.lower())    

        for i, n in enumerate(name):
            if not n.isalpha():
                S = ""
                for c in n:
                    if c.isalpha():
                        S += c
                name[i] = S

        if len(name) == 2:
            mail = "{}_{}@{}.com".format(name[1], name[0], C)
            num = 1
            while mail in res_list:
                num = num + 1
                mail = "{}_{}{}@{}.com".format(name[1], name[0], num, C)

            res_list.append(mail)
        
        elif len(name) == 3:
            mail = "{}_{}_{}@{}.com".format(name[2], name[0], name[1][0], C)
            num = 1
            while mail in res_list:
                num = num + 1
                mail = "{}_{}_{}{}@{}.com".format(name[2], name[0], name[1][0], num, C)

            res_list.append(mail)
        
    return res_list

       

S = ['aa bb cc', 'xx yy Z-z', 'aa bb', 'aa bx cc']
C = 'test'

print(solution(S, C))


# 如果名字出現數字，先檢查並處理非英文字母的跟 '-' 的問題。
