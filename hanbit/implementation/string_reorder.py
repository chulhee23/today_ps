a = str(input())

val = 0
result = []
for x in a:
    if x.isalpha():
        result.append(x)
    else:
        val += int(x)
result.sort()
if value !=0 :
    result.append(str(val))

print(''.join(result))