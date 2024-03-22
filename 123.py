
#№1
def calculate(number):
    sum_of_парні = 0

    for num in range(1, number + 1):
        if num % 2 == 0:
            sum_of_парні += num

    return sum_of_парні


# Приклад виклику функції
number = 10
result = calculate(number)
print(f"Сума парних чисел від 1 до {number} дорівнює {result}")






#№2
def calculate(number):
    sum_of_odds = 0

    for num in range(1, number + 1):
        if num % 2 != 0:
            sum_of_odds += num

    return sum_of_odds


# Приклад виклику функції
number = 10
result = calculate(number)
print(f"Сума непарних чисел від 1 до {number} дорівнює {result}")






#№3
def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        # Перевірка дільників від 3 до квадратного кореня числа
        for num in range(3, int(number**0.5) + 1, 2):
            if number % num == 0:
                return False
        return True

# Приклад використання
num = 17
if is_prime(num):
    print(f"{num} є простим числом.")
else:
    print(f"{num} не є простим числом.")






#№4
# Функція для обчислення значень функції y = 2*x - 1
def calculate_function(x):
    return 2*x - 1

# Задання проміжку та кроку
start = -3
end = 3
step = 0.5

# Створення списку для збереження результатів
results = []

# Обчислення та збереження значень функції
current_x = start
while current_x <= end:
    y = calculate_function(current_x)
    results.append((current_x, y))
    current_x += step

# Виведення результатів на екран
for x, y in results:
    print(f"x = {x}, y = {y}")





#№5
# Заданий список (припустимо, що це ваш список)
numbers = [1, -2, 3, -4, 5, -6, 7, 8, -9]

# Ініціалізація лічильника
negative_count = 0

# Перегляд кожного елемента у списку
for num in numbers:
    # Перевірка, чи є елемент від'ємним
    if num < 0:
        negative_count += 1

# Виведення результату на екран
print(f"Кількість від'ємних елементів у списку: {negative_count}")






#№6
# Заданий список (припустимо, що це ваш список)
numbers = [1, -2, 3, -4, 5, -6, 7, 8, -9]

# Ініціалізація лічильника
positive_count = 0

# Перегляд кожного елемента у списку
for num in numbers:
    # Перевірка, чи є елемент додатнім
    if num > 0:
        positive_count += 1

# Виведення результату на екран
print(f"Кількість додатніх елементів у списку: {positive_count}")





#№7
# Ініціалізація змінної для збереження суми
sum_of_numbers = 0

# Цикл for для перегляду чисел від 21 до 99 (більше 20, менше 100)
for number in range(21, 100):
    # Перевірка, чи число кратне 3
    if number % 3 == 0:
        sum_of_numbers += number

# Виведення результату на екран
print(f"Сума натуральних чисел, більших 20, менших 100 і кратних 3: {sum_of_numbers}")






#№8
# Початкова сума вкладу
initial_amount = 5000

# Річна відсоткова ставка
annual_interest_rate = 20

# Кількість років
years = 5

# Цикл для обчислення суми вкладу за кожен рік
for year in range(1, years + 1):
    # Формула для обчислення суми вкладу після певного часового періоду
    deposit_amount = initial_amount * (1 + annual_interest_rate / 100) ** year
    print(f"Після {year} років сума вкладу буде {(deposit_amount, 2)} грн")




#№9




stack = []  # створення порожнього стеку

stack.append(1)  # додаємо елементи до стеку
stack.append(2)
stack.append(3)

# видаляємо елементи зі стеку
print(stack.pop())  # виводить 3
print(stack.pop())  # виводить 2
print(stack.pop())  # виводить 1
