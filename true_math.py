from math import inf

def divide(first, second):
    if second == 0:  # Проверка делителя
        return inf  # Если деление на 0
    return first / second  # Обычное деление