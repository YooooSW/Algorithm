def solution(l, r):
    answer = []
    
    for num in range(l, r + 1):
        str_num = str(num)
        if all(c in '05' for c in str_num):
            answer.append(num)
    if not answer:
        return [-1]
    
    return answer