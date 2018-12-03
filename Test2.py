# def solution(A, B, M, X, Y):
#     count = 0
#     stack = []
#     weight = 0
    
#     while A:
#         while A and weight + A[0] <= Y and len(stack) <= X:
#             weight += A[0]
#             stack.append(B[0])
#             A.pop(0)
#             B.pop(0)

#         count += len(set(stack)) + 1
#         stack [:] = []
#         weight = 0

#     return count

def solution(A, B, M, X, Y):
    count = 0
    
    weight = 0

    while A and B:
        stack = [B[0]]
        while A and weight + A[0] <= Y and len(stack) <= X:
            weight += A[0]
            if stack and B[0] != stack[-1]:
                stack.append(B[0])
            print(stack)
            A.pop(0)
            B.pop(0)

        count += len(stack) + 1
        weight = 0

    return count




A = [60, 40, 80, 60]    # Weight
B = [4, 3, 4, 2]          # Target floor
M = 5                        # Top floor
X = 3                        # Max people
Y = 200                      # Max Weight

# A = [40, 40, 100, 80, 20]    # Weight
# B = [3, 3, 2, 2, 3]          # Target floor
# M = 5                        # Top floor
# X = 3                        # Max people
# Y = 200                      # Max Weight

print(solution(A,B, M, X, Y))