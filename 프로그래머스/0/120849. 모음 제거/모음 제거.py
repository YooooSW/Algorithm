def solution(my_string):
    aeiou = "aeiou"
    result = ""
    
    for char in my_string:
        if char not in aeiou:
            result += char
    
    return result
