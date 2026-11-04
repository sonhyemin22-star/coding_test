def solution(citations):
    h_list = []
    for num1 in citations:
        h = 0
        for num2 in citations:
            if num1 <= num2:
                h += 1
        if num1 <= h:
            h_list.append(num1)
        else:
            h_list.append(h)
    return max(h_list)