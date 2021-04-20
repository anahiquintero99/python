def palindrome(word):
    word = word.replace(' ', '')
    word = word.lower()
    word_backwards = word[::-1]
    if word == word_backwards:
        return True
    else:
        return False


def run():
    word = input('\nEnter Word: ')
    is_palindrome = palindrome(word)

    if is_palindrome == True:
        print('\nThe word is palindrome.')
    else:
        print('\nThe word is not palindrome')


if __name__ == '__main__':
    run()
