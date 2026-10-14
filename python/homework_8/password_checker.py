"""Prompt for a password until the correct one is entered."""

CORRECT_PASSWORD = 'secret'

password = input('Enter the password: ')
while password != CORRECT_PASSWORD:
    password = input('Wrong password. Try again: ')
print('Access granted!')
