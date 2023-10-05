#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

double f(double x) {
    return atan(sin(x));
}

double g1(double x) {
    return cos(x) / (pow(sin(x), 2) + 1.0);
}

double g2(double x) {
    return -sin(x) * (pow(sin(x), 2) + 2*pow(cos(x),2) + 1) / pow(pow(sin(x), 2) + 1, 2);
}

double first_deriv(double X[], int n, int i, double h) {
 
    if (i == 0) {
        return (-3 * f(X[0]) + 4 * f(X[1]) - f(X[2])) / (2 * h);
    }
    if (i == n-1) {
        return (3 * f(X[i]) - 4 * f(X[i-1]) + f(X[i-2])) / (2 * h);
    }

    return (f(X[i+1]) - f(X[i-1]))/(2*h);
}

double second_deriv(double X[], int n, int i, double h) {
    if (i == 0) {
        return (f(X[0]) - 2 * f(X[1]) + f(X[2])) / (h*h);
    }
    if (i == n-1) {
        return (f(X[i-2]) - 2 * f(X[i-1]) + f(X[i])) / (h*h);
    }
    return (f(X[i+1]) - 2*f(X[i]) + f(X[i-1]))/(h*h);
}

int main() {
    double a = -3;
    double b = 3;
    double h = 10e-3;
    int n = int((b - a) / h) + 1;

    double *X {new double[n]};
    double *F_deriv1 {new double[n]};
    double *F_deriv2 {new double[n]};
    double *G1 {new double[n]};
    double *G2 {new double[n]};
    for (int i = 0; i < n; i++){
        X[i] = a + h*i;
    }

    for (int i = 0; i < n; i++){
        F_deriv1[i] = first_deriv(X, n, i, h);
        F_deriv2[i] = second_deriv(X, n, i, h);
        G1[i] = g1(X[i]);
        G2[i] = g2(X[i]);
    }

     ofstream out1("functions.txt");

    if (!out1)
    {
        cout << "Error. Cannot open the file.";
        return false;
    }
    
    for (int i = 0; i < n; i++){
        out1 << double(X[i]) << "\t" << double(G1[i]) << "\t" << double(F_deriv1[i])  << "\t" << double(G2[i]) << "\t" << double(F_deriv2[i])<< "\n";
    }
    
    out1.close();


    return 0;
}