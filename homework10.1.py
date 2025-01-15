def custom_sequence(first, n, rule):
    """
    Генераторная функция для числовой последовательности.

    :param first: Первый член последовательности.
    :param n: Количество членов последовательности.
    :param rule: Функция, задающая закон последовательности (f(prev) -> next).
    """
    current = first
    for _ in range(n):
        yield current
        current = rule(current)

rule = lambda x: x * 2

sequence = custom_sequence(1, 5, rule)

print(list(sequence))  # [1, 2, 4, 8, 16]
