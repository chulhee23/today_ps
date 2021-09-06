# win_rate, heavy fight, weight, idx, head2head
def solution(weights, head2head):
    win_rate = [] 
    arr = []    

    for idx in range(len(weights)):
        w = weights[idx]
        h = head2head[idx]
        win = len(list(filter(lambda x: x == 'W', h)))
        lose = len(list(filter(lambda x: x == 'L', h)))
        win_rate = 0

        if lose + win != 0:
            win_rate = win / (lose + win)

        arr.append({'win_rate': (win_rate * 100), 'weight': w, 'idx': idx})


    n = len(head2head)
    for i in range(n):
        heavyfight = 0
        arr[i]['heavy'] = 0
        for j in range(n):
            cur = head2head[i][j]
            if cur == 'W' and weights[i] < weights[j]:
                heavyfight += 1
        arr[i]['heavy'] = heavyfight

    arr.sort(key = lambda x: (x['win_rate'], x['heavy'], x['weight'],n - x['idx']), reverse=True)
    ans = []
    print(arr)
    for i in arr:
        ans.append(i['idx'] + 1)
    return ans


print(solution([50, 82, 75, 120],["NLWL", "WNLL", "LWNW", "WWLN"]))
print(solution([145, 92, 86],["NLW", "WNL", "LWN"]))
print(solution([60, 70, 60],["NNN", "NNN", "NNN"]))
