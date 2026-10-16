def solution(myStr):
    x = myStr.replace('a', ' ')
    y = x.replace('b', ' ')
    z = y.replace('c', ' ')
    answer = z.strip().split()
    if not answer:
        return ['EMPTY']
    else:
        return answer