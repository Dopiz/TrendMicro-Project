import re

def solution(A, B):
    
    def transform(S):
        first = 1 if S[0].isalpha() else 0
        alpha  = re.findall(r'[a-zA-Z]+', S)
        number = list(map(int, re.findall(r'[0-9]+', S)))
        s = ""

        if first:
            for i in range(len(alpha)):
                if i < len(number):
                    s += alpha[i] + '?' * number[i]
                else: s += alpha[i]
        else:
            for i in range(len(number)):
                if i < len(alpha):
                    s += '?' * number[i] + alpha[i]
                else: s += '?' * number[i]
    
        return s

    
    A = transform(A)
    B = transform(B)

    if len(A) != len(B):
        return False

    for i in range(len(A)):
        if A[i] == '?' or B[i] == '?':
            continue
        if A[i] != B[i]:
            return False
    
    return True



A = "3x2x"
B = "8"
print(solution(A, B))

