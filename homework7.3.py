def second_index(text: str, search: str) -> int | None:
    try:
        first_index = text.index(search)
        second_index = text.index(search, first_index + 1)
        return second_index
    except ValueError:
        return None
text = "sims"
search = "s"
result = second_index(text, search)
print(result)

text = "hello world"
search = "o"
result = second_index(text, search)
print(result)

text = "hello"
search = "x"
result = second_index(text, search)
print(result)
