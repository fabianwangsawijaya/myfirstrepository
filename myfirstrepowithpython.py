def is_palindrome(string):
    new_string = ""
    for i in string:
        if i.isalnum():
            new_string += i
    print(new_string)
    # new_integer = 0
    # for x in string:
    #     if x.isalpha():
    #         new_integer += x
    return new_string[::-1].casefold() == new_string.casefold()




word = input("Please enter a word to check if its a palindrome: ")
if is_palindrome(word):
    print("'{}' is a Palindrome.".format(word))
else:
    print("'{}' is not a Palindrome.".format(word))
