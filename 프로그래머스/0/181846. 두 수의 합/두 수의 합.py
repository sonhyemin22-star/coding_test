def solution(a, b):
    answer = ''
    sum = []
    a1 = list(map(int, list(a[::-1])))
    b1 = list(map(int, list(b[::-1])))
    if len(a1) > len(b1):
        c = [0] * (len(a1) - len(b1))
        c1 = b1 + c
        for i in range(len(c1)):
            if i <= (len(c1) - 2):
                if a1[i] + c1[i] < 10:
                    sum.append(str(a1[i] + c1[i]))
                else:
                    a1[i + 1] += 1
                    sum.append(str((a1[i] + c1[i]) - 10))
            elif i == (len(c1) - 1):
                sum.append(str(a1[i] + c1[i])[::-1])
    elif len(a1) < len(b1):
        c = [0] * (len(b1) - len(a1))
        c1 = a1 + c
        for i in range(len(c1)):
            if i <= (len(c1) - 2):
                if b1[i] + c1[i] < 10:
                    sum.append(str(b1[i] + c1[i]))
                else:
                    b1[i + 1] += 1
                    sum.append(str((b1[i] + c1[i]) - 10))
            elif i == (len(c1) - 1):
                sum.append(str(b1[i] + c1[i])[::-1])
    else:
        if a1[0] == b1[0] == 0:
            sum = ['0']
        else:
            for i in range(len(a1)):
                if i <= (len(a1) - 2):
                    if a1[i] + b1[i] < 10:
                        sum.append(str(a1[i] + b1[i]))
                    else:
                        a1[i + 1] += 1
                        sum.append(str(a1[i] + b1[i] - 10))
                elif i == (len(a1) - 1):
                    sum.append(str(a1[i] + b1[i])[::-1])
    if sum[-1] == '0':
        return '0'
    else:
        for i in range(len(sum)):
            answer += sum[i]
        return answer[::-1]