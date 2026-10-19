def solution(s):
    count = 0
    for x in s:
        if x == '(':
            count += 1
        else:
            count -= 1
    if count == 0:
        return True
    else:
        return False