import numpy as np

# моифицированный метолд ньютона
def newton_modif(f, f0, x0, eps):
    '''
        f - левая часть решаемого уравнения
        f0 - производная левой части в точке x0
        x0 - начальное приближение
        eps - точность решения
    '''
    x1 = np.float128(x0) - np.float128(f(x0))/np.float128(f0)  # считаем первое приближение

    crit1 = abs(x1 - x0) > np.float128(eps)         # флаг для отслеживания первого критерия останова
    crit2 = abs(f(x1) - f(x0)) > np.float128(eps)   # флаг для отслеживания второго критерия останова

    while(crit1):
        x0, x1 = x1, x1 - np.float128(f(x1))/np.float128(f0)   # считаем новые приближенные значения корня 
        crit1 = abs(x1 - x0) > np.float128(eps)     # проверяем выполнение критериев останова
        crit2 = abs(f(x1) - f(x0)) > np.float128(eps)
    
    return x1, crit1, crit2


# левая часть решаемого уравнения
def f(x):
    return np.float128(np.exp(np.sin(x/2)) - np.arctan(x) + 1)


# первая производная левой части
def f_deriv(x):
    return np.float128(0.5 * np.exp(np.sin(x/2))*np.cos(x/2) - 1/(x**2 + 1))


# тестирование метода ньютона
def test_newton_modif(x0, eps):
    answer, crit1, crit2 = newton_modif(f, f_deriv(x0), x0, eps)
    print("x =", answer)
    print("Выполнение критериев останова: ")
    print("Первый -", not crit1)
    print("Второй -", not crit2)


def main():
    x0 = np.float128(6.0)

    test_newton_modif(x0, 1e-3)
    test_newton_modif(x0, 1e-6)
    test_newton_modif(x0, 1e-9)


main()
