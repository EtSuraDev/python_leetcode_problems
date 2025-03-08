def isPalindrome(x):
    reversed_num = str(x)[::-1]

    if(str(x) == reversed_num):
        print(True)
        return True
    print(False)
    return False


isPalindrome(121)
isPalindrome(-120)
isPalindrome(10)