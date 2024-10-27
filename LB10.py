import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import approximate_taylor_polynomial

# Визначимо символічну змінну x і функцію f(x)
x = sp.symbols('x')
f = sp.cos(4 * x) - x + 1

# Обчисліть перші три похідні
f1 = sp.diff(f, x)
f2 = sp.diff(f1, x)
f3 = sp.diff(f2, x)

# Відобразити похідні
print("f'(x) =", f1)
print("f''(x) =", f2)
print("f'''(x) =", f3)

# Обчислити значення функції та її похідних при x = 0
x0 = 0
f_x0 = f.subs(x, x0).evalf()
f1_x0 = f1.subs(x, x0).evalf()
f2_x0 = f2.subs(x, x0).evalf()
f3_x0 = f3.subs(x, x0).evalf()

# Побудуйте поліном Тейлора третього ступеня при x = 0
T = f_x0 + f1_x0 * (x - x0) + (f2_x0 / 2) * (x - x0)**2 + (f3_x0 / 6) * (x - x0)**3
print("f(0) =", f_x0.round(3))
print("T(x) =", T.evalf())

# Перетворення символьного виразу на числову функцію для побудови
f_lambdified = sp.lambdify(x, f, 'numpy')
T_lambdified = sp.lambdify(x, T, 'numpy')

# Визначте значення x для побудови
x_vals = np.linspace(-2, 2, 1000)
f_vals = f_lambdified(x_vals)
T_vals = T_lambdified(x_vals)

# Побудуйте вихідну функцію та наближення полінома Тейлора
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_vals, label='f(x) = cos(4x) - x + 1', color='blue')
plt.plot(x_vals, T_vals, label='Тейлор (3rd order)', color='red', linestyle='--')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Графік функції та її апроксимація поліномом Тейлора")
plt.legend()
plt.grid(True)
plt.show()

# Побудуйте поліном Тейлора за допомогою scipy для порівняння
def f_np(x):
    return np.cos(4 * x) - x + 1

# Використовуйте scipy, щоб побудувати поліном Тейлора третього ступеня
degree = 3
taylor_approx = approximate_taylor_polynomial(f_np, 0, degree, 1)

# Побудуйте графік, використовуючи наближення полінома Тейлора Scipy
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_vals, label="if(x) curve", color='blue')
plt.plot(x_vals, taylor_approx(x_vals), label=f"degree={degree}", color='green', linestyle='--')
plt.legend(loc='upper left')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Графік функції та апроксимація полінома Тейлора (scipy)")
plt.grid(True)
plt.show()
