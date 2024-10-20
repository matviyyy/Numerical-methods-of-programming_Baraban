import numpy as np
import matplotlib.pyplot as plt
import math

# Графічне відокремлення коренів

# Область значень для x та y
x_min, x_max = -2, 2
y_min, y_max = -4, 4
step = 0.01

# Створюємо масиви значень x та y
x, y = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))

# Рівняння системи
eq1 = np.sin(x + 1) - y - 1.2
eq2 = 2 * x + np.cos(y) - 2

# Створюємо графік
fig, ax = plt.subplots(figsize=(10, 10))

# Додаємо графік першого рівняння
ax.contour(x, y, eq1, levels=[0], colors='red', label='sin(x + 1) - y = 1.2')

# Додаємо графік другого рівняння
ax.contour(x, y, eq2, levels=[0], colors='blue', label='2x + cos(y) = 2')

# Налаштування графіка
ax.set_xlim([x_min, x_max])
ax.set_ylim([y_min, y_max])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Графік системи рівнянь')
plt.grid(True)

# Показуємо графік
plt.show()

# Метод простої ітерації

# Початкові наближення
x0 = 0.5
y0 = -1.5
epsilon = 0.001

# Визначення функцій для ітерацій
def f1(y):
    return 1/2 * (2 - math.cos(y))  # з рівняння 2x + cos(y) = 2 -> x = (2 - cos(y)) / 2

def f2(x):
    return math.sin(x + 1) - 1.2  # з рівняння sin(x+1) - y = 1.2 -> y = sin(x+1) - 1.2

# Метод простої ітерації
def simple_iteration(x, y, epsilon):
    xn, yn = x, y
    xn1 = f1(yn)
    yn1 = f2(xn)
    iterations = 1

    while abs(xn1 - xn) > epsilon or abs(yn1 - yn) > epsilon:
        xn, yn = xn1, yn1
        xn1 = f1(yn)
        yn1 = f2(xn)
        iterations += 1

    return xn, yn, iterations

# Виконання методу
x_sol, y_sol, iter_count = simple_iteration(x0, y0, epsilon)

# Виведення результату
print(f'Розв\'язок: x = {x_sol:.3f}, y = {y_sol:.3f}')
print(f'Кількість ітерацій: {iter_count}')
