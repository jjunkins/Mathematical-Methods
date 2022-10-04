ode - Jerod Junkins

def eulers_method(f, y0, b, N):
   
    ans = [(0., y0)] #period after 0 needed
    
    delta = b/N
    
    y_xplush = y0
    
    for i in range(1, N+1):
        
        y_xplush += f(ans[-1][0], ans[-1][1])*delta
        
        # append the current x and y_plush as tuple into ans, current x = i * delta
        x = i * delta
        
        tup = [x, y_xplush]
        
        ans.append(tup)
        
    return ans

