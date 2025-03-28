import numpy as np
import sympy as sp

def solve_cubic(a, b, c, d):
    coeffs = [a, b, c, d]
    roots = np.roots(coeffs)
    return roots

def solve_quartic(a, b, c, d, e):
    x = sp.symbols('x')
    equation = a*x**4 + b*x**3 + c*x**2 + d*x + e
    roots = sp.solve(equation, x)
    return roots

def main():
    print("Select the type of equation to solve:")
    print("1. Cubic Equation (Ax^3 + Bx^2 + Cx + D = 0)")
    print("2. Quartic Equation (Ax^4 + Bx^3 + Cx^2 + Dx + E = 0)")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        print("Solving a cubic equation")
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))
        d = float(input("Enter coefficient D: "))
        roots = solve_cubic(a, b, c, d)
        print("Roots of the cubic equation:", roots)
    
    elif choice == '2':
        print("Solving a quartic equation")
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))
        d = float(input("Enter coefficient D: "))
        e = float(input("Enter coefficient E: "))
        roots = solve_quartic(a, b, c, d, e)
        print("Roots of the quartic equation:", roots)
    
    else:
        print("Invalid choice. Please select 1 or 2.")
        
input()