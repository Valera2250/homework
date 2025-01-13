def correct_sentence(sentence1: str, sentence2: str) -> tuple:
    def correct_single_sentence(sentence: str) -> str:
        sentence = sentence.strip()
        if sentence:
            sentence = sentence[0].upper() + sentence[1:]
        if not sentence.endswith('.'):
            sentence += '.'
        return sentence
    corrected_sentence1 = correct_single_sentence(sentence1)
    corrected_sentence2 = correct_single_sentence(sentence2)

    return corrected_sentence1, corrected_sentence2

sentence1 = "привет, как дела"
sentence2 = "это тестовое предложение."
result = correct_sentence(sentence1, sentence2)
print(result)  # Вывод: ('Привет, как дела.', 'Это тестовое предложение.')
