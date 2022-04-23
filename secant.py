

def f(x):            # our function
    
    e = 2.71

    #return x * e**((x**2)/4) -3 * x + 2
    return -x**6 +3*x -7


""" def f(x):           # our function
    e = 2.71
    return x * e**((x**2)/4) -3 * x + 2 """

def iterate(first, next):     # newton's formula
    return first - f(first)/( ( f(next) - f(first) ) / (next-first) )
 

def main():
    previous_point = 0
    next_point = 1      #starting point of iteration
    n = 1
    print("step         x_(n-1)         x_n         x_(n+1")
    while True:             #if difference of iteration points is between -10^(-7) and 10^(-7) brake the loop
         
        if (next_point - previous_point) > 10 ** (-7) or (next_point - previous_point) < (-10 ** (-7)) :  
            
            next_point_holder = next_point
            next_point = iterate(previous_point, next_point)
            previous_point = next_point_holder
            
            
            print("{}       {}      {}      {}".format(n, round(previous_point, 2), round(next_point_holder, 2), round(next_point, 4)) )
            #round() function limits the floating point to 2 decimal number. For example 2.456879 -> 2.45

            n += 1      #iteration number increases in each step of iteration 

        elif (next_point-previous_point) < 10**(-7):
            #print("{}       {}      {}".format(n, round(y, 2), round(y_deriv, 2)))
            break
    
main()      # calling the main function