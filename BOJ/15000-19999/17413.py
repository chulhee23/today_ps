from collections import deque
import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":       # 열린 괄호를 만나면
        i += 1
        while word[i] != ">":      # 닫힌 괄호를 만날 때 까지
            i += 1
        i += 1               # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[i].isalnum():  # 숫자나 알파벳을 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i += 1
        tmp = word[start:i]  # 숫자,알파벳 범위에 있는 것들을
        tmp.reverse()       # 뒤집는다
        word[start:i] = tmp
    else:                   # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i += 1                # 그냥 증가시킨다

print("".join(word))

# nums = list(str(i) for i in range(10))
# stacking = False
# queueing = False
# for c in s:
    
#     if c.isalpha() or c in nums:
#         if queueing:
#             queue.append(c)
#         else:
#             stacking = True
#             stack.append(c)

#     elif c == '<':
#         stacking = False
#         queueing = True
#         while stack:
#             tmp = stack.pop()
#             ans += tmp
#         queue.append(c)

#     elif c == '>':
#         queueing = False
#         queue.append(c)
#         while queue:
#             ans += queue.popleft()
        
#     else:
#         # 공백
#         if stacking:
#             stacking = False
#             while stack:
#                 ans += stack.pop()
#             ans += c
#         elif queueing:
#             queue.append(c)
#         else:
#             ans += c
# if stacking:
#     while stack:
#         tmp = stack.pop()
#         ans += tmp
# print(ans)
