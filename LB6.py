import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# Дані точки даних
x = np.array([-2, -1, 0, 1], dtype=float)
y = np.array([-7, 4, 1, 2], dtype=float)

# Бали для оцінки
points_to_evaluate = [-3, -1.5, 0.5, 1.5]

# Функція для інтерполяції Лагранжа
def lagrange_interpolation(x, y, x_test):
    n = len(x)
    p = np.zeros(n)  # Масив для зберігання значень поліномів L_i
    for i in range(n):
        # Обчисліть поліном L_i
        p_i = 1
        for j in range(n):
            if i != j:
                p_i *= (x_test - x[j]) / (x[i] - x[j])
        p[i] = p_i
    return np.dot(y, p)  # Повертає значення полінома

# Обчислити значення функції у вказаних точках
for idx, point in enumerate(points_to_evaluate):
    f_point = lagrange_interpolation(x, y, point)
    print(f"Значення функції у точці x_{idx+1} = {f_point:.4f}")

# Згенеруйте дані для побудови полінома Лагранжа
x_new = np.linspace(np.min(x), np.max(x), 100)  # Точки для нанесення графіка
y_new = [lagrange_interpolation(x, y, i) for i in x_new]

# Побудуйте поліном Лагранжа та точки даних
plt.plot(x, y, 'o', label="Дані точки")
plt.plot(x_new, y_new, label="Lagrange Polynomial", color='blue')
for point in points_to_evaluate:
    plt.plot(point, lagrange_interpolation(x, y, point), 'ro')  # Поставте оцінені бали

plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Polynomial_1')
plt.grid(True)
plt.legend()
plt.show()

# Перевірка за допомогою функції Лагранжа scipy
f_lagrange = lagrange(x, y)
plt.figure(figsize=(10, 6))
plt.plot(x_new, f_lagrange(x_new), 'b', label="Scipy Lagrange Polynomial")
plt.plot(x, y, 'ro', label="Дані точки")
for idx, point in enumerate(points_to_evaluate):
    plt.plot(point, lagrange_interpolation(x, y, point), 'ro')
    plt.annotate(f"{lagrange_interpolation(x, y, point):.4f}", (point, lagrange_interpolation(x, y, point)), textcoords="offset points", xytext=(5,5), ha='center')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Polynomial_2')
plt.grid(True)
plt.legend()
plt.show()
