def solution(my_string, s, e):
    front = my_string[:s]
    middle = my_string[s:e+1][::-1]
    end = my_string[e+1:]
    
    result = front + middle + end
    return result