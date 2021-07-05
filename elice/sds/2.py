
import sys
input = sys.stdin.readline


def main():
    ans = []

    test = int(input())
    for _ in range(test):

        tmp = 0
        ans.append(tmp)

    for i, a in enumerate(ans):
        print(f"#{i+1} {a}")


main()
