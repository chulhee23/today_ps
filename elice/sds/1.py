# https: // howtoliveworldnice.tistory.com/3

import sys
input = sys.stdin.readline

def dp(arr, m):
    if(m < 3):
        return arr[m-1]
    elif m == 3:
        return arr[0] + arr[1] + arr[2]
    return (dp(arr, m-2) + min(arr[m-1] + arr[m-2] + 2 * arr[0], arr[0] + arr[m-1] + arr[1] * 2))

def main():
    ans = []


    test = int(input())
    for _ in range(test):
        n = int(input())
        arr = list(map(int, input().split()))
        tmp = dp(arr, n)
        ans.append(tmp)

    for i, a in enumerate(ans):
        print(f"#{i+1} {a}")


main()
