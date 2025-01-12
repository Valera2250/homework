import string
import keyword
def is_valid_variable_name(name):
    if name in keyword.kwlist:
        return False
    allowed_characters = set(string.ascii_lowercase + string.digits + "_")
    if any(char not in allowed_characters for char in name):
        return False
    if name.count("_") > 1:
        return False
    if name[0].isdigit():
        return False
    return True
user_input = input("Введите строку: ")
print(user_input, '==>', is_valid_variable_name(user_input))
