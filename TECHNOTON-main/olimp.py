# a, b = float(input().split()[0]), int(input().split()[1])



# x = input()
# s = 0
# a = False
# for digit in x:
#     s += int(digit)
#     if int(digit)%2==0:
#         a=True

# if s%9==0 and a:
#     print("YES")
# else:
#     print("NO")




# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def find_a_b(s, d):
#     min_a = float('inf')  
#     res_a, res_b = -1, -1  
#     for a in range(1, int(s ** 0.5) + 1):
#         if s % a == 0:
#             b = s // a
#             if gcd(a, b) == d:
#                 if a < min_a: 
#                     min_a = a
#                     res_a, res_b = a, b
#                 elif a == min_a and b < res_b: 
#                     res_b = b
#     return res_a, res_b


# s, d = input().split()
# s=int(s)
# d=int(d)

# a, b = find_a_b(s, d)
# if a == -1 or b == -1:
#     print(-1)
# else:
#     print(a, b)




# N, X, Y = input().split()
# N = int(N)
# X = int(X)
# Y = int(Y)
# res = 0
# if X>N and Y<=N:
#     X = 2*N - X + 1
#     res=abs(X - Y) + 1
# elif Y>N and X<=N:
#     Y = 2*N - Y + 1
#     res=abs(X - Y) + 1
# elif (X>N and Y>N) or (X<=N and Y<=N):
#     res=abs(X - Y)

# print(res)




from itertools import combinations

def can_form_strong_team(students, N, K):
    student_knowledge = [{idx for idx, topic in enumerate(student) if topic == 'Y'} for student in students]
    
    for team in combinations(student_knowledge, 3):
        combined_knowledge = set().union(*team)
        if len(combined_knowledge) == K:
            return True
    return False

N, K = map(int, input().split())
students = [input() for _ in range(N)]

if can_form_strong_team(students, N, K):
    print("Ia")
else:
    print("Joq")






# def minimize_max(x):
#     digits = [int(digit) for digit in x]
#     if len(x) == 2:
#         return max(int(x), int(x[::-1]))
    
#     digits = sorted(digits)

#     min_digit = min(digits)
#     max_digit = max(digits)

#     min_digits = []
#     max_digits = []

#     for digit in digits:
#         if digit == min_digit:
#             min_digits.append(digit)
#         else:
#             max_digits.append(digit)

#     new_number = ''.join(map(str, min_digits))

#     mid_index = len(new_number) // 2
#     new_number = new_number[:mid_index] + ''.join(map(str, max_digits)) + new_number[mid_index:]

#     if len(max_digits) == 1:
#         new_number += str(max_digits[0])

#     return new_number

# x = input().strip()
# print(minimize_max(x))

