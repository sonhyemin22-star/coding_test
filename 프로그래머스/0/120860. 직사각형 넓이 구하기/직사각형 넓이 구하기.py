def solution(dots):
    for i in range(1, len(dots)):
        if dots[0][0] == dots[i][0]:
            y = abs(dots[0][1] - dots[i][1])
        if dots[0][1] == dots[i][1]:
            x = abs(dots[0][0] - dots[i][0])
    return x * y