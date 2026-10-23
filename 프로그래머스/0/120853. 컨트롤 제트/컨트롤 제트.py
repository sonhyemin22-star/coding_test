def solution(s):
    s1 = s.split()
    for i in range(1, len(s1)):
        if s1[i] == 'Z':
            s1[i] = -int(s1[i - 1])
    return sum(map(int, s1))