def solution(arr, queries):
    for list1 in queries:
        for i in range(list1[0], list1[1] + 1):
            arr[i] += 1
    return arr