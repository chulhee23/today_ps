def distance(current, number):
    number_lv = (number - 1) // 3
    current_lv = (current - 1) // 3
    y_distance = abs(number_lv - current_lv)
    x_distance = abs(((number - 1) % 3) - ((current - 1) % 3))
    
    return x_distance + y_distance


def solution(numbers, hand):
    answer = ''
    left_arr = [1, 4, 7]
    right_arr = [3, 6, 9]
    left = 10
    right = 12

    numbers = list(map(lambda x: 11 if x == 0 else x, numbers ))
    
    for number in numbers:

        if number in left_arr:
            answer += 'L'
            left = number
        
        elif number in right_arr:
            answer += 'R'
            right = number
        
        else:
            left_d = distance(left, number)
            right_d = distance(right, number)
            
            if left_d < right_d:
                answer += 'L'
                left = number
            elif left_d > right_d:
                answer += 'R'
                right = number
            else:
                if hand == "right":
                    answer += 'R'
                    right = number
                else:
                    answer += 'L'
                    left = number    
    
    return answer



print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))