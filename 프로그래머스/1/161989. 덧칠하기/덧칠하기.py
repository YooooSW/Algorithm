def solution(n, m, section):
    answer = 0
    paint = 0
    
    for i in section:
        if(i > paint):
            paint = i + m - 1
            answer += 1
            
    return answer