import string

letters = string.ascii_letters
user_input = input("Enter two letters: ")

start = letters.index(user_input[0])
end = letters.index(user_input[2])

if start <= end:
    print(letters[start:end + 1])
else:
    print(letters[start:] + letters[:end + 1])