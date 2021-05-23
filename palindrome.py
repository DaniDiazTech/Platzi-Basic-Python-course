def palindrome(string):
    string = string.lower().replace(' ', '')
    return string == string[::-1]

def main():
    is_palindrome = palindrome(input('Your string: '))

    print("Yep it's palindrome" if is_palindrome else "No it's not palindrome")

if __name__ == '__main__':
    main()