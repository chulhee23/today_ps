n = int(input())

arr = list(map(int, input().split()))

sum_arr = [0] * n
sum_arr[0] = arr[0]
sum_arr[1] = arr[1]


if (arr[1] > arr[0] + arr[2]): 
    flag = False
    sum_arr[2] = arr[1]
else: 
    flag = True
    sum_arr[2] = arr[0] + arr[2]
print(sum_arr)
print(flag)
for i in range(3, len(arr)):
    v = arr[i]
    print("====")
    print(i)
    # 직전에 더한 경우
    if flag:
    # 넘어가거나, 2칸 전 값과 더한 값이 더 크면 이 값으로!
        # 지금꺼 , 2번째꺼 더한게 더 작음 
        if sum_arr[i-1] > sum_arr[i-2] + v:
            sum_arr[i] = sum_arr[i-1]
            flag = False
        else:
            sum_arr[i] = sum_arr[i-2] + v
            flag = True
    else:
        sum_arr[i] = sum_arr[i-1] + v
        flag = True
    
    # 그 이전에 더한 경우
    # 바로 더함

    
print(sum_arr)