
def solution(answers):
    a = [1,2,3,4,5] # 5
    b = [2,1,2,3,2,4,2,5] # 8
    c = [3,3,1,1,2,2,4,4,5,5] # 10
    aa = 0
    ba = 0
    ca = 0
    for idx, answer in enumerate(answers):
        a_i = idx % 5
        b_i = idx % 8
        c_i = idx % 10

        if a[a_i] == answer:
            aa += 1
        if b[b_i] == answer:
            ba += 1
        if c[c_i] == answer:
            ca += 1

    tmp = [aa, ba, ca]
    max_tmp = max(tmp)
    answer = [i+1 for i, x in enumerate(tmp) if x == max_tmp]

    
    
    return answer



print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))



