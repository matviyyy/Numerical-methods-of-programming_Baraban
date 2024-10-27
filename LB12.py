import numpy as np
from scipy import integrate

# Інтеграл 1: ∫(dx / √(2x^2 + 1)) від 0.8 до 1.6 методом прямокутників
a1, b1, n1 = 0.8, 1.6, 10
h1 = (b1 - a1) / n1
def f1(x):
    return 1 / np.sqrt(2 * x**2 + 1)

# Метод лівих прямокутників
def left_rectangle(f, a, b, n, h):
    result = sum(f(a + i * h) for i in range(n))
    return result * h

# Метод правих прямокутників
def right_rectangle(f, a, b, n, h):
    result = sum(f(a + (i + 1) * h) for i in range(n))
    return result * h

# Метод середніх прямокутників
def middle_rectangle(f, a, b, n, h):
    result = sum(f(a + (i + 0.5) * h) for i in range(n))
    return result * h

# Обчислення інтегралів методом прямокутників
left_result = left_rectangle(f1, a1, b1, n1, h1)
right_result = right_rectangle(f1, a1, b1, n1, h1)
middle_result = middle_rectangle(f1, a1, b1, n1, h1)

print(f"Метод лівого прямокутника (1st integral): {left_result:.4f}")
print(f"Метод правого прямокутника (1st integral): {right_result:.4f}")
print(f"Метод центрального прямокутника (1st integral): {middle_result:.4f}")

# Інтеграл 2: ∫(lg(x+2) / x) від 1.2 до 2 методом Сімпсона
a2, b2, n2 = 1.2, 2.0, 8
h2 = (b2 - a2) / n2
def f2(x):
    return np.log10(x + 2) / x

# Метод Сімпсона
def simpson_rule(f, a, b, n, h):
    result = f(a) + f(b)
    for i in range(1, n):
        coef = 4 if i % 2 != 0 else 2
        result += coef * f(a + i * h)
    result *= h / 3
    return result

simpson_result = simpson_rule(f2, a2, b2, n2, h2)
print(f"Метод Сімпсона (2-й інтеграл): {simpson_result:.4f}")

# Інтеграл 3: ∫(dx / √(x^2 + 2.3)) від 0.32 до 0.66 методом трапецій
a3, b3, n3 = 0.32, 0.66, 20
h3 = (b3 - a3) / n3
def f3(x):
    return 1 / np.sqrt(x**2 + 2.3)

# Метод трапецій
def trapezoidal_rule(f, a, b, n, h):
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result

trapezoidal_result = trapezoidal_rule(f3, a3, b3, n3, h3)
print(f"Трапецієподібний метод (3-й інтеграл): {trapezoidal_result:.4f}")

# Перевірка результатів за допомогою scipy.integrate.quad
v1, err1 = integrate.quad(f1, a1, b1)
v2, err2 = integrate.quad(f2, a2, b2)
v3, err3 = integrate.quad(f3, a3, b3)
print(f"Перевірте за допомогою SciPy (1-й інтеграл): {v1:.4f}")
print(f"Перевірте за допомогою SciPy (2-й інтеграл): {v2:.4f}")
print(f"Перевірте за допомогою SciPy (3-й інтеграл): {v3:.4f}")
