def grade(s):
    if s >= 90:
        return "A"
    elif s >= 80:
        return "B"
    elif s >= 70:
        return "C"
    elif s >= 50:
        return "D"
    else:
        return "F"

def solution(scores):
    answer = ''
    n = len(scores)
    for j in range(n):  
        arr = []
        me = -1
        for i in range(n):
            arr.append(scores[i][j])
            if i == j:
                me = scores[i][j]
        s = sum(arr)
        a = s / len(arr)
        
        if (max(arr) == me or min(arr) == me):
            if len(list(filter(lambda x: x == me, arr))) == 1:
                s -= me
                a = s / (len(arr) - 1)
        answer += grade(a)
        
    return answer