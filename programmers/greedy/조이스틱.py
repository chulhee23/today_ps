import pdb

def solution(name):
    answer = 0
    # alphabet = ("a b c d e f g h i j k l m n o p q r s t u v w x y z").split(" ")
    # alphabet = [a.upper() for a in alphabet]
    # 0 .. 25 26개

    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]

    idx = 0
    answer = 0

    while True:
        # 현재 문자열 A 로 전환. A 상태였어도 ok.
        answer += change[idx] # 상하 전환 완료
        change[idx] = 0 # A 로 처리

        # 모든 change 가 0 이면 전부 변환 완료
        if sum(change) == 0:
            print(answer)
            return answer


        # 좌우 이동거리 계산. 배열의 크기를 넘을 일은 없음. 
        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
            # 1
        
        while change[idx + right] == 0:
            right += 1
            # 2

        # 왼쪽으로 이동하는 경우
        if left < right:
            answer += left
            idx += -left
        else:
            answer += right
            idx += right
        




        
        

'''
전략.
1. change 배열에 알파벳 상하 조절 min 값 담기
2. idx 0번 부터 시작해서 좌우 이동 횟수 더하기.
2-1. 좌우 이동 횟수에는 방향이 전환될 수 있는데, A가 아닌 알파벳까지 거리를 구하고 그 중 최솟값을 선택 -> 해당 방향으로 전환됨.
3. 모든 change 가 0 이면 전부 변환 완료.
'''

solution('JEROEN')
print(f'expect {56}')
solution('JAN')
print(f'expect {23}')
