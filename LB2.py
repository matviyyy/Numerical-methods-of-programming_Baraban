import numpy as np
import numdifftools as nd

# Дати визначення функції
def f(x):
    return 9*pow(x, 4) + 8*pow(x, 3) + 1.5*pow(x, 2) + 2*x - 10

# Функція ізоляції кореня (пошук сегментів, де f(x) змінює знак)
def find_segments(): 
    search_range = np.arange(-10, 10, 0.5) # Визначте діапазон пошуку та розмір кроку
    a = None
    previous_x = None
    current_x = None
    segments = []
    
    for x in search_range:
        x = round(x, 4)
        current_x = f(x)
        if previous_x is not None and previous_x * current_x < 0:
            segments.append((a, x))  # Між a і x існує корінь
        a = x
        previous_x = current_x
    return segments

# Метод розрізу навпіл
def rec(a, b, eps): 
    while abs(a - b) > eps:
        mid = (a + b) / 2
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    x = (a + b) / 2
    print('x =', round(x, 5), ' - Half division method')
    return x

# Метод січної (хорди).
def hord(a, b, eps):
    derivative_f = nd.Derivative(f, n=1)
    if f(a) * derivative_f(a) > 0:
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a
    
    xi_1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0))
    
    while abs(xi_1 - xi) > eps:
        xi = xi_1
        xi_1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0))
    
    print('x =', round(xi_1, 5), ' - Chord method')
    return xi_1

# Встановити точність
eps = 0.0001

# Знайдіть відрізки, де функція змінює знак
segments = find_segments()
for a, b in segments:
    print(f'Found segment: [{a}, {b}]')

# Застосуйте методи для кожного сегмента
for a, b in segments:
    print(f'\nSolving on segment [{a}, {b}]')
    rec(a, b, eps)  # Метод розрізу навпіл
    hord(a, b, eps)  # Метод січної
