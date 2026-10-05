def solution(arr, intervals):
    num_list1 = arr[intervals[0][0]:(intervals[0][1] + 1)]
    num_list2 = arr[intervals[1][0]:(intervals[1][1] + 1)]
    return num_list1 + num_list2