def solution(arr):
    if 2 in arr:
        x = []
        for i in range(len(arr)):
            if arr[i] == 2:
                x.append(i)
        return arr[x[0]:(x[-1] + 1)]
    else:
        return [-1]