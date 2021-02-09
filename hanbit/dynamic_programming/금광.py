# 그리디 아님
# 탐색? 아님
# dp!
# 정확한 점화식을 구해내면 단순 구현 문제로 바뀐다.
# 점화식 dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

# 1 3 3 2 
# 2 1 4 1 
# 0 6 4 7



# 테스트 케이스별 
for tc in range(int(input())):
    n,m = map(int, input().split())
    array = list(map(int, input().split()))
    
    # dp 위한 2차원 배열 초기화
    dp = []
    index = 0

    for i in range(n):
        dp.append(array[index: index+m])
        index += m

    # skill : 0,0 1,0 2,0 순서로 읽기 -> 2중 for문 i, j 순서 거꾸로!
    for j in range(1, m):
        for i in range(n):
            if i == 0: 
                # 예외 처리
                left_up = 0
            else: 
                left_up = dp[i-1][j-1]
            
            if i == n - 1: 
                # 예외 처리
                left_down = 0
            else: 
                left_down = dp[i+1][j-1]
            
            left = dp[i][j-1]
            dp[i][j] = array[i][j] + max(left_up, left_down, left)
    
    result = 0
    # 마지막 열에 대한 결과값
    for i in range(n):
        result = max(result, dp[i][m-1])
    
    print(result)