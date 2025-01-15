def first_word(text: str) -> str:
    """
    Находит первое слово в строке.

    :param text: Входная строка.
    :return: Первое слово в строке.
    """
    cleaned_text = text.replace(",", " ").replace(".", " ")
    words = cleaned_text.split()
    return words[0] if words else ""

print(first_word("Hello, world!"))
print(first_word("  ...Let's test."))
print(first_word("single"))
print(first_word(""))                   
