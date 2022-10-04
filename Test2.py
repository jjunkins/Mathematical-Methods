import math
import bisection_method

def f(x):
    return x**2 - 2

def g(x):
    return math.exp(x) - 10


def h(x):
    return x**2 + 1


f_interval = [0.0, 4.0]
g_interval = [0.0, 6.0]
cos_interval = [0.0, 2.0]
h_interval = [0.0, 3.0]

functions = [f, g, h, math.cos]
intervals = [f_interval, g_interval, cos_interval, h_interval]
tolerances = [1e-12, None, 1e-12, 1e-14]




with open("hw62_output.txt", "w") as outfile:
    for fun, interval, tol in zip(functions, intervals, tolerances):
        try:
            if tol:
                root = bisection_method.bisection_method(fun, interval, tol)
            else:
                root = bisection_method.bisection_method(fun, interval)
            print(root)
            outfile.write(f"{root}\n")
        except ValueError as ve:
            print(ve)
            outfile.write("No root found\n")