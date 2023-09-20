#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

double f(double x) {
    return sin(exp(x / 3.0) / 10.0);
}

double coef_lagr(double x, double grid[], int i, int n){
    double xi = grid[i];
    double prod = 1.0;

    for (int j = 0; j < n; j++) {
        if (j != i) {
            prod *= (x - grid[j]) / (xi - grid[j]);
        }
    }
    
    return prod;
}

double lagr_polynom(double x, double grid[], int n){
    double sum = 0;
    for (int i = 0; i < n; i++){
        sum += f(grid[i]) * coef_lagr(x, grid, i, n);
    }
    
    return sum;
}

double divided_diff(double grid[], int n){
    double sum = 0.;
    if (n == 1){
        return f(grid[0]);
    }
    
    for (int i = 0; i < n; i++){
        double prod = 1.;
        for (int j = 0; j < n; j++){
            if (i != j){
                prod *= (grid[i] - grid[j]);
            }
        }
        sum += f(grid[i]) / prod;
    }

    return sum;
}

double coef_newton(int i, double grid[]){
    double new_grid[i+1];
    for (int j = 0; j < i+1; j++){
        new_grid[j] = grid[j];
    }
    return divided_diff(new_grid, i+1);
}

double newton_polynom(double x, int i, double grid[], int n){
    if (i == n - 1){
        return coef_newton(i-1, grid) + (x - grid[i-1]) * coef_newton(i, grid);
    }
    return newton_polynom(x, i + 1, grid, n) * (x - grid[i-1]) +  coef_newton(i-1, grid);
}

double cheb_points(int j, double a, double b, int n){
    return (a + b) / 2 + (b - a) * cos((2*j+1) * acos(-1) / (2*n)) / 2;
}

int main() {
    int n = 7;
    double a = 0.;
    double b = 10.;

    double *grid {new double[n]};
    double *cheb_grid {new double[n]};
    double h = (b - a) / (n-1);
    for (int i = 0; i < n; i++){
        grid[i] = a + h*i;
        cheb_grid[i] = cheb_points(i, a, b, n);
    }

    int n1 = 100;
    double *X {new double[n1]};
    double *Y {new double[n1]};
    double *Y_lagrange {new double[n1]};
    double *Y_newton {new double[n1]};
    double *Y_lagrange_cheb {new double[n1]};
    double *Y_newton_cheb {new double[n1]};
    double h1 = (b - a) / (n1-1);
    for (int i = 0; i <= n1; i++){
        X[i] = a + h1*i;
        Y[i] = f(X[i]);
        Y_lagrange[i] = lagr_polynom(X[i], grid, n);
        Y_newton[i] = newton_polynom(X[i], 1, grid, n);
        Y_lagrange_cheb[i] = lagr_polynom(X[i], cheb_grid, n);
        Y_newton_cheb[i] = newton_polynom(X[i], 1, cheb_grid, n);
    }

    ofstream out1("functions.txt");

    if (!out1)
    {
        cout << "Error. Cannot open the file.";
        return false;
    }
    
    // out1 << "x\t f(x)\t lagrange\t newton\t lagrange_cheb\t newton_cheb\n";

    for (int i = 0; i < n1; i++){
        out1 << double(X[i]) << "\t" << double(Y[i]) << "\t" << double(Y_lagrange[i]) << "\t" << double(Y_newton[i]) << "\t" << double(Y_lagrange_cheb[i]) << "\t" << double(Y_newton_cheb[i]) << "\n";
    }
    
    out1.close();

    ofstream out2("points.txt");

    // Записываем точки интерполяции в файл
    if (!out2)
    {
        cout << "Error. Cannot open the file.";
        return false;
    }
    
    // out2 << "x_uniform\t x_chebyshev\t f(x_uniform)\t f(x_chebyshev)\n";

    for (int i = 0; i < n; i++){
        out2 << double(grid[i]) << "\t" << double(cheb_grid[i]) << "\t" << double(f(grid[i])) << "\t" << double(f(cheb_grid[i])) << "\n";
    }

    out2.close();
    return 0;
}

