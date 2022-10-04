bisection method - Jerod Junkins

def bisection_method(f, interval, tol = 10e-10):
    
    a = interval[0]
    b = interval[1]
    
    if f(a) == 0:
        
        return a
        
    elif f(b) == 0:
        
        return b
        
    elif f(a)*f(b)>0:
        
        #if f(a)*f(b)>0 need to raise error
        raise ValueError("No syspected root: f(a) and f(b) have the same sign.")
        
    else:
        
        while b - a >= tol:
            
            mid = (b+a)/2 #compute the midpoint (x1+x2/2)
            
            f_mid = f(mid) #comopute the value of f at mid point
            
            if f_mid == 0:  #check whether f_mid equal to 0, 
                
                return mid

            elif f(a)*f(mid)<0:

               b = mid

            elif f(a)*f(mid)>0:
                
                a = mid
                
                
        if abs(f(a)) <= abs(f(b)):
            return a
        else:
            return b


            
            #check which product, f_mid * f(a), f_mid * f(b) smaller than zero
            
            # update the a and b accordingly
            
        #check which one is smaller f(a), f(b) (by absolute value)
        #return the endpoint of the smaller value