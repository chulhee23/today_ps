import sys
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())
for tt in range(t):
    s = input().rstrip()

    ans = []

    while True:
        sentence = input().rstrip()
        if sentence == "END":
            break

        a, b, c = sentence.split()

        if a == "I":
            idx = int(c)
            ch = b
            front = s[:idx]
            rear = s[idx:]
            s = front + ch + rear

        else:
            start = int(b)
            end = int(c)
            print(f"{''.join(s[start:end + 1])}\n")

