def is_palindrome(str) -> bool:
    for i in range(int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

print(is_palindrome("malayalam"))