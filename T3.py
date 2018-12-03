import re

def solution(T, R):
    # write your code in Python 3.6
    count = 0
    
    match = {T[i]: R[i] for i in range(len(T))}
    
    T = sorted(T)
    
    testcase = set()
    for t in T:
        testcase.add(re.findall(r'[a-zA-Z]+[0-9]+', t)[0])
    
    res = {tc: 1 for tc in testcase}
    
    for i, t in enumerate(T):
        for tc in testcase:
            if tc in t and match[t] != 'OK':
                res[tc] = 0
                break
    
    count = list(res.values()).count(1)
    
    return int(count / len(testcase) * 100)

# 驗證 TestSuit 的成功率
# 題目中一個 TestSuit 可能會有 Test1a Test1b 多個 TestCase，要整組對才算對
# 字串處理
