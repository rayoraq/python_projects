from random import *

def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += choice(chars)
    print(password)


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

pwd_quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
pwd_len = int(input('Какой длины должен быть пароль? '))
pwd_digits = input('Включать ли в пароль цифры? ')
pwd_uppercase = input('Включать ли в пароль прописные буквы? ')
pwd_lowercase = input('Включать ли в пароль строчные буквы? ')
pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? ')
pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? ')

if pwd_digits.lower() in ['lf','да']:
    chars+=digits
if pwd_uppercase.lower() in ['lf','да']:
    chars+=pwd_uppercase
if pwd_lowercase.lower() in ['lf','да']:
    chars+=pwd_lowercase
if pwd_punctuation.lower() in ['lf','да']:
    chars+=pwd_punctuation
if pwd_exceptions.lower() in ['lf','да']:
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

for _ in range(pwd_quantity):
    generate_password(pwd_len, chars)
