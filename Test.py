import ode


def f1(x, y):
    return -2 * x * y


soln1 = ode.eulers_method(f1, 1.0, 2.0, 2000)

with open("hw_61_results1.txt", "w") as outfile:
    for x, y in soln1:
        outfile.write(f"{x:.16f}, {y:.16f}\n")
        
        
def f2(x, y):
    return 3 * x**2

soln2 = ode.eulers_method(f2, 0.0, 3.0, 100)

with open("hw_61_results2.txt", "w") as outfile:
    for x, y in soln2:
        outfile.write(f"{x:.3f}, {y:.16f}\n")
        
        
def f3(x, y):
    return -y
        
soln3 = ode.eulers_method(f3, 1.0, 4.0, 1000)

with open("hw_61_results3.txt", "w") as outfile:
    for x, y in soln3:
        outfile.write(f"{x:.4f}, {y:.16f}\n")