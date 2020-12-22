


def solution(number, k):

    nums = [int(num) for num in str(number)]
    
    # nums.sort(reverse=True)

    # nums = nums[:len(nums)-k]

    # 1 2 3 1 2 3 4
    # _ _ _ _
    # 1
    # 2
    # 3
    # 3 1
    # 3 2
    # 3 2 3
    # 더 큰 값으로 교체
    arr = [0 for _ in range(len(nums)-k)]
    current_index = 0

    for i, num in enumerate(nums):
        # 현재 arr 남은 수와 남은 갯수 동일할 경우
        left_arr_num = len(arr) - current_index
        left_nums = len(nums) - i

        print(f"left_nums: {left_nums}")
        print(f"left_arr_num: {left_arr_num}")
        print(f"current_index: {current_index}")
        print("==")
        if left_nums == left_arr_num:
            arr[current_index+1:] = nums[i+1:]
            break
        else:
            if arr[current_index] < num:
                arr[current_index] = num
                
                # arr[current_index] = num
            
    print("---------")
    print(arr)


number = "4177252841"
"4177252841"
"    775841"
k=4
solution(number, k)

