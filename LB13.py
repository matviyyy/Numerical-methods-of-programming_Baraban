import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

# Параметри для рівняння (а)
a, b, h, y0 = 1.8, 2.8, 0.1, 2.6
n = int((b - a) / h)
x_vals = np.arange(a, b + h, h)  # Включаємо b у x_vals

# Функція для диф. рівняння (а): y' = x + cos(y / sqrt(5))
def f_a(x, y):
    return x + np.cos(y / np.sqrt(5))

# Метод Ейлера для рівняння (а)
y_vals = np.empty(len(x_vals))  # Створюємо масив y_vals з такою ж кількістю елементів, як і x_vals
y_vals[0] = y0

for i in range(len(x_vals) - 1):  # Виконуємо цикл до len(x_vals) - 1
    y_vals[i + 1] = y_vals[i] + h * f_a(x_vals[i], y_vals[i])

# Вивід результатів
print("Метод Ейлера (рівняння а):")
print("x =", x_vals)
print("y =", y_vals)

# Графік
plt.plot(x_vals, y_vals, marker='o', label="Euler's Method (a)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Метод Ейлера для рівняння (а)")
plt.legend()
plt.grid()
plt.show()


# Метод Ейлера-Коші
y_vals = np.empty(len(x_vals))
y_vals[0] = y0
for i in range(len(x_vals) - 1):
    y_temp = y_vals[i] + h * f_a(x_vals[i], y_vals[i])
    y_vals[i + 1] = y_vals[i] + h * 0.5 * (f_a(x_vals[i], y_vals[i]) + f_a(x_vals[i + 1], y_temp))

# Вивід результатів
print("Метод Ейлера-Коші (рівняння а):")
print("x =", x_vals)
print("y =", y_vals)

# Графік
plt.plot(x_vals, y_vals, marker='o', label="Euler-Cauchy Method (a)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Метод Ейлера-Коші для рівняння (а)")
plt.legend()
plt.grid()
plt.show()


# Розв'язання диф. рівняння (а) за допомогою odeint
y_odeint = odeint(lambda y, x: f_a(x, y), y0, x_vals)

# Вивід результатів
print("odeint результат (рівняння а):")
print("x =", x_vals)
print("y =", y_odeint.flatten())

# Графік
plt.plot(x_vals, y_odeint, marker='o', label="odeint (a)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Розв’язання за допомогою odeint для рівняння (а)")
plt.legend()
plt.grid()
plt.show()


# Розв'язання диф. рівняння (а) за допомогою solve_ivp
# Задаємо інтервал та початкові умови для рівняння (а)
a, b = 1.8, 2.8
y0 = 2.6
h = 0.1
x_vals = np.linspace(a, b, int((b - a) / h) + 1)

# Функція для рівняння (а): y' = x + cos(y / sqrt(5))
def f_a(x, y):
    return x + np.cos(y / np.sqrt(5))

# Розв'язання рівняння (а) за допомогою solve_ivp
sol = solve_ivp(f_a, [a, b], [y0], t_eval=x_vals)

# Виведення результатів
print("solve_ivp результат (рівняння а):")
print("x =", sol.t)
print("y =", sol.y[0])

# Графік
plt.plot(sol.t, sol.y[0], marker='o', label="solve_ivp (a)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Розв’язання за допомогою solve_ivp для рівняння (а)")
plt.legend()
plt.grid()
plt.show()