def solution(order):
    A = []
    C = []
    for menu in order:
        if menu.find('americano') != -1:
            A.append(menu)
        elif menu == 'anything':
            A.append(menu)
        else:
            C.append(menu)
    return (len(A) * 4500) + (len(C) * 5000)