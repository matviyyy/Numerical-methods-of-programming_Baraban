import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# Дана точка даних
x = np.array([1.415], dtype=float)
y = np.array([0.8885], dtype=float)

# Бали для оцінки
points_to_evaluate = [1.416, 1.456]

# Функція прямої інтерполяції Ньютона
def newton_forward_interpolation(x, y, x0):
    n = len(x)
    h = x[1] - x[0] if n > 1 else 1  # Розмір кроку між точками, за умовчанням 1, якщо одна точка
    # Обчислити кінцеві різниці
    delta_y = np.zeros((n, n))
    delta_y[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            delta_y[i, j] = delta_y[i + 1, j - 1] - delta_y[i, j - 1]
    # Обчисліть q
    q = (x0 - x[0]) / h
    # Обчислити інтерпольоване значення
    ans = delta_y[0, 0]
    q_prod = 1
    for i in range(1, n):
        q_prod *= (q - i + 1)
        ans += (q_prod * delta_y[0, i]) / factorial(i)
    return ans

# Обчислити інтерпольовані значення
for idx, point in enumerate(points_to_evaluate):
    f_point = newton_forward_interpolation(x, y, point)
    print(f"Значення функції у точці x_{idx+1} = {f_point:.4f}")

# Згенеруйте дані для побудови графіка функції інтерполяції
x_new = np.linspace(min(x[0], points_to_evaluate[0]), max(x[0], points_to_evaluate[1]), 100)
y_new = [newton_forward_interpolation(x, y, i) for i in x_new]

# Побудуйте графік інтерполяційної функції та заданої точки
plt.plot(x, y, 'o', label="Дані точки")
plt.plot(x_new, y_new, label="Інтерполяційна функція Ньютона", color='blue')
for point in points_to_evaluate:
    plt.plot(point, newton_forward_interpolation(x, y, point), 'ro')  # Поставте оцінені бали

plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік інтерполяційної функції Ньютона')
plt.grid(True)
plt.legend()
plt.show()
