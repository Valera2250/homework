import string

def get_letters_between(input_range):
    all_letters = string.ascii_letters
    start, end = input_range.split('-')
    start_index = all_letters.index(start)
    end_index = all_letters.index(end)
    return all_letters[start_index:end_index + 1]
user_input = input("Введите две буквы через дефис: ")
result = get_letters_between(user_input)
print(user_input,'==>' ,result)