from fake_math import divide as fake_div
from true_math import divide as true_div

# Тестовые вызовы функций
result1 = fake_div(69, 3)       # Обычное деление
result2 = fake_div(3, 0)        # Деление на 0, ошибка
result3 = true_div(49, 7)       # Обычное деление
result4 = true_div(15, 0)       # Деление на 0, возвращает бесконечность

# Вывод результатов
print(result1)  # 23.0
print(result2)  # "Ошибка"
print(result3)  # 7.0
print(result4)  # inf