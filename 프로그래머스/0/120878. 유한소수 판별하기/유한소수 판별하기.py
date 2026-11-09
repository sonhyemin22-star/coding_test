def solution(a, b):
    d = []
    for i in range(2, (b + 1)):
        if b % i == 0:
            d.append(i)
    d.sort(reverse=True)
    for j in d:
        if a % j == 0:
            a //= j
            b //= j
            break
    dd = []
    for k in range(2, (b + 1)):
        while b % k == 0:
            b //= k
            if not k in dd:
                dd.append(k)
    for l in dd:
        if l == 2:
            continue
        elif l == 5:
            continue
        else:
            return 2
    return 1