target, s = input().split()

l, r = 0, len(target) - 1

while r < len(s):
    cf = []
    for i in range(l, r+1):
        if s[i] not in target:
            l, r = i + 1, i + len(target)
            break

        else:
            if s[i] not in cf:
                cf.append(s[i])

    if len(cf) == len(target):
        print(l)
        exit(0)
print(-1)