def solution(arr):
    n = 0
    while True:
        if len(arr) < 2 ** n:
            arr.extend([0] * (2 ** n - len(arr)))
            return arr
            break
        elif len(arr) == 2 ** n:
            return arr
            break
        else:
            n += 1