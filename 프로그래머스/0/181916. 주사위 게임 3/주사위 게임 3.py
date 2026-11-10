def solution(a, b, c, d):
    if a == b == c == d:
        return 1111 * a
    elif a == b == c and d != a:
        return (10 * a + d) ** 2
    elif a == b == d and c != a:
        return (10 * a + c) ** 2
    elif a == c == d and b != a:
        return (10 * a + b) ** 2
    elif b == c == d and a != b:
        return (10 * b + a) ** 2
    elif a == b and c == d:
        return (a + c) * abs(a - c)
    elif a == c and b == d:
        return (a + b) * abs(a - b)
    elif a == d and b == c:
        return (a + b) * abs(a - b)
    elif a == b and c != a and c != d and d != a:
        return c * d
    elif a == c and b != a and b != d and d != a:
        return b * d
    elif a == d and b != a and b != c and c != a:
        return b * c
    elif b == c and a != b and a != d and d != b:
        return a * d
    elif b == d and a != b and a != c and c != b:
        return a * c
    elif c == d and a != c and a != b and b != c:
        return a * b
    elif a != b and b != c and c != d and a != c and a != d and b != d:
        return min(a, b, c, d)