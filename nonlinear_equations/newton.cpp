#include <iostream>
#include <math.h>
#include <iomanip>

// модифицированный метод ньютона
long double newton_modif(long double f( long double x),
                long double f0, 
                long double x0, 
                long double eps) 
{
    /*
        f - левая часть решаемого уравнения
        f0 - производная левой части в точке x0
        x0 - начальное приближение
        eps - точность решения
    */

    long double x1 = x0 - f(x0)/f0;
    bool crit1 = fabs(x1 - x0) > eps;        // флаг для отслеживания первого критерия останова
    bool crit2 = fabs(f(x1) - f(x0)) > eps;  // флаг для отслеживания второго критерия останова

    while (crit1) {
        x0 = x1;
        x1 = x1 - f(x1)/f0;    // считаем новые приближенные значения корня
        crit1 = fabs(x1 - x0) > eps;    // проверяем выполнение критериев останова
        crit2 = fabs(f(x1) - f(x0)) > eps;
    }

    std::cout << "Выполнение критериев останова:\n";
    std::cout << "Первый - " << !crit1 << "\n" << "Второй - " << !crit2 << std::endl;

    return x1;
}

// левая часть решаемого уравнения
long double f(long double x) {
    return exp(sin(x/2)) - atan(x) + 1;
}


// производная левой части
long double f_deriv(long double x) {
    return exp(sin(x/2)) * cos(x/2) / 2 - 1/(pow(x,2) + 1);
}


//тестирование метода ньютона
void test_newton_modif(long double x0, long double eps) {

    long double answer = newton_modif(f, f_deriv(x0), x0, eps);
    std::cout << "x = " << std::setprecision(20) << answer << std::endl;
}


int main() {
    long double x0 = 6.0;

    test_newton_modif(x0, 1e-3);
    test_newton_modif(x0, 1e-6);
    test_newton_modif(x0, 1e-9);

    return 0;
}
