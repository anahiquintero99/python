
word = input('\nEnter Word: ')
word_backwards = word[::-1]
print(f'\nWord: {word_backwards}')

if word == word_backwards:
    print('\nThe word is palindrome.')
else:
    print('\nThe word is not palindrome')
