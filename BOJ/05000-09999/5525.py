n = int(input())
m = int(input())
s = input()

p = "IO" * n + "I"
pl = len(p)
count = 0


if s[0] != "O":
    i = s.index("O") - 1
else:
    i = s[1:].index("O") - 1


while(i < len(s) - pl + 1):
    if p == s[i:i+pl]:
        count += 1
        # 일치했는데, 그 다음이 I 인 경우 i 를 바로 그 다음으로 넘기면 됨
        if s[i + pl] == "I":
            i += pl
        else:
            i += 2
            # s[i] == 1

    else:
        i += 1
print(count)
