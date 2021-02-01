import pdb
# 체스판
# 나이트의 가능한 경우의 수
x = 'a b c d e f g h'.split()
y = '1 2 3 4 5 6 7 8'.split()

loc = str(input())
loc = [i for i in loc]
# a 1

loc[0] = x.index(loc[0]) + 1

loc = [int(i) for i in loc]

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

result = []
for i in range(len(dx)):
    result.append([loc[0] + dx[i], loc[1] + dy[i]])

def inChessBoard(l):
    '''
    '''
    if 0 < l[0] and l[0] < 9 and 0 < l[1] and l[1] < 9:
        return l

result = list(filter(inChessBoard, result))

print(len(result))


