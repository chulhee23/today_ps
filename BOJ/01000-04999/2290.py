s, n = map(int, input().split())

m = '-'
l = '|'

def init():
    num = [ [' '] * (s + 2) for _ in range(2 * s + 3)]
    return num


def top(num):
   for i in range(1, s+1):
       num[0][i] = m

def lt(num):
    for i in range(1, s+1):
        num[i][0] = l

def rt(num):
    for i in range(1, s+1):
        num[i][-1] = l

def md(num):
    for i in range(1, s+1):
        num[s+1][i] = m

def bl(num):
    for i in range(s+2, 2*s + 2):
        num[i][0] = l

def br(num):
    for i in range(s+2, 2*s + 2):
        num[i][-1] = l

def bt(num):
    for i in range(1, s+1):
        num[2*s + 2][i] = m


def draw(c, num):
    if c in [0, 2, 3, 5, 6, 7, 8, 9]:
        top(num)
    if c in [0,4, 5, 6, 8, 9]:
        lt(num)
    if c in [0,1,2,3,4,7,8,9]:
        rt(num)
    if c in [2,3,4,5,6,8,9]:
        md(num)
    if c in [0,2,6,8]:
        bl(num)
    if c in [0,1, 3,4,5,6,7,8,9]:
        br(num)
    if c in [0,2,3,5,6,8,9]:
        bt(num)

n = str(n)
arr = []

for c in n:
    num = init()
    draw(int(c), num)
    arr.append(num)

ans = [[] for _ in range(2*s + 3)]

for i in range(0, 2*s + 3):
    for idx in range(len(arr)):
        ans[i] += arr[idx][i]
        ans[i].append(' ')

    
for c_arr in ans:
    print(''.join(c_arr))
