def generate_cube_numbers(limit):
    """
    Генератор кубов чисел, начиная с 2, пока значения меньше указанной величины.

    :param limit: Верхний предел для кубов чисел.
    """
    number = 2
    while True:
        cube = number ** 3
        if cube >= limit:
            return
        yield cube
        number += 1


print(list(generate_cube_numbers(100)))
