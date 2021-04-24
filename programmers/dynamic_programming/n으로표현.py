def solution(n, number):
    # n 5
    # number 12

    num_set = [set() for _ in range(9)]
    
    for i in range(1, 9):
        num_set[i].add(int(str(n) * i))
        
        for j in range(1, i//2 + 1):
            for x in num_set[j]:
                for y in num_set[i-j]:
                    num_set[i].add( x + y)
                    num_set[i].add( x * y)
                    num_set[i].add( x - y)
                    num_set[i].add( y - x)
                    if x != 0:
                        num_set[i].add( y // x)
                    if y != 0:
                        num_set[i].add( x // y)
                    

    
    for i in range(1, 9):
        if number in num_set[i]:
            return i
    return -1
    


print(solution(5, 12))
print(solution(2, 11))
