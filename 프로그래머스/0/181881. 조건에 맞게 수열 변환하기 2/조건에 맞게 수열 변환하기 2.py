def solution(arr):
    answer = 0
    while True:
        arr2 = []
        for num in arr:
            if num >= 50 and num % 2 == 0:
                arr2.append(num / 2)
            elif num < 50 and num % 2 == 1:
                arr2.append((num * 2) + 1)
            else:
                arr2.append(num)
        if arr != arr2:
            arr = arr2
        else:
            return answer
        answer += 1