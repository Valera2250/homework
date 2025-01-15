def popular_words(text: str, words: list) -> dict:

    text_words = text.lower().split()

    result = {word: text_words.count(word) for word in words}
    return result

text = """
When I was One,
I had just begun.
When I was Two,
I was nearly new.
"""
words = ['one', 'two', 'three']
print(popular_words(text, words))
