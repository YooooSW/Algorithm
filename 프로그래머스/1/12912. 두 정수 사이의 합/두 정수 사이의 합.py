def solution(a, b):
    if a > b:
        a, b = b, a
        
    n = b - a + 1
    return n * (a + b) // 2
# 등차수열공식사용