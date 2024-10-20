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

# Метод Ньютона
def nuton(a, b, eps, f):
    df2 = nd.Derivative(f, n=2)(b)  # Друга похідна в точці b
    if f(b) * df2 > 0:
        xi = b
    else:
        xi = a
    df = nd.Derivative(f, n=1)(xi)  # Перша похідна в точці xi
    xi_1 = xi - f(xi) / df
    
    while abs(xi_1 - xi) > eps:  # Перевірте точність
        xi = xi_1
        df = nd.Derivative(f, n=1)(xi)
        xi_1 = xi - f(xi) / df
    
    print('Метод Ньютона, x =', round(xi_1, 4))
    return xi_1

# Комбінований метод (імовірно змішування секансу та методів Ньютона)
def komb(a, b, eps, f):
    if nd.Derivative(f, n=1)(a) * nd.Derivative(f, n=2)(a) > 0:
        a0 = a
        b0 = b
    else:
        a0 = b
        b0 = a
    ai = a0
    bi = b0
    
    while abs(ai - bi) > eps:
        ai_1 = ai - f(ai) * (bi - ai) / (f(bi) - f(ai))
        bi_1 = bi - f(bi) / nd.Derivative(f, n=1)(bi)
        ai = ai_1
        bi = bi_1
        
    x = (ai_1 + bi_1) / 2
    print('Комбінований метод, x =', round(x, 4))
    return x

# Встановити точність
eps = 0.0001

# Знайдіть відрізки, де функція змінює знак
segments = find_segments()
for a, b in segments:
    print(f'Found segment: [{a}, {b}]')

# Застосуйте метод Ньютона та комбінований метод для кожного сегмента
for a, b in segments:
    print(f'\nSolving on segment [{a}, {b}]')
    nuton(a, b, eps, f)  # Метод Ньютона
    komb(a, b, eps, f)  # Комбінований метод
