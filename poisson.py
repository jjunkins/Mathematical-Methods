# Jerod Junkins - Poisson
# Collaborators: Brendan Schwartz & Alec Wells

import numpy as np
import numpy.linalg


def solve_poisson(f, a, b, alpha, beta, n):

    
    x_grid = np.linspace(a, b, n+1)
    

    h = (b - a)/n
   

    rhs = np.array([alpha] + [f(x)*(h**2) for x in x_grid[1:-1]] + [beta])
    
    
    d_a = np.diag(-2*np.ones(n+1))
   
    up_a = np.diag(np.ones(n),1)
   

    lo_a = np.diag(np.ones(n),-1)
   

    lhs = d_a + up_a + lo_a
    lhs[0,0] = 1
    lhs[0,1] = 0
    lhs[-1,-1] = 1
    lhs[-1,-2] = 0

    ans = np.linalg.solve(lhs, rhs)
   

    return ans