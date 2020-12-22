def solution(n, lost, reserve):

    students = [1 for i in range(n)]

    for lost_s in lost:
        students[lost_s - 1] = 0

    for reserve_s in reserve:
        students[reserve_s-1] += 1

    # [2, 0, 2, 0, 2]
    for i, v in enumerate(students):
        left = students[i-1] if i != 0 else 0
        right = students[i+1] if i != len(students)-1 else 0

        if (v == 0):
            if left == 2:
                students[i-1] -= 1
                students[i] += 1
            elif right == 2:
                students[i+1] -= 1
                students[i] += 1
    print(students)
    
    return len(list(filter(lambda x: x >= 1, students)))




n = 5

lost = [2,4]
reserve = [3]
solution(n, lost, reserve)

