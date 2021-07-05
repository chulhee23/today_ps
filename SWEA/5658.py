# 보물상자 비밀번호
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo&categoryId=AWXRUN9KfZ8DFAUo&categoryType=CODE&problemTitle=%EB%B3%B4%EB%AC%BC&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

t = int(input())
answers = []
for _ in range(t):
    n, k = map(int, input().split())
    d = n // 4 # 묶이는 개수

    nums = input()
    arr = []
    
    for num in nums:
        arr.append(num)
        # num = int(num, 16)
    
    result = []

    tmp = ""
    i = 0

    for tt in range(d+1):
        for i in range(4):
            start = d * i
            end = d * (i + 1)
            # result.append(int(''.join(arr[start:end]), 16))
            result.append(''.join(arr[start:end]))
        temp = arr.pop()
        arr.insert(0, temp)

    result = list(set(result))
    result.sort(reverse=True)
    answers.append(result[k-1])

for i in range(len(answers)):
    print(f"#{i+1} {int(answers[i], 16)}")
