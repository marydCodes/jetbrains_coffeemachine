# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# print(alphabet[14])

def capwords():
    user_input = str(input())
    print(user_input.title().replace("_", ""))


capwords()