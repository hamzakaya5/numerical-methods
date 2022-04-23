"""
def f(x):               #function to find its roots
    return x**4 + 7 * x**3 -11 * x**2 +5
"""

def f(x):            # our function
    e = 2.71
    #return x * e**((x**2)/4) -3 * x + 2
    return -x**6 +3*x -7


def iteration(a, b):                    #function of regula falsi method
    return (a*f(b)-b*f(a))/(f(b)-f(a))

def main():
    a = -2      #starting point
    b = 0       #finishing point
    n= 1        #number of iterations
    print(" n\tXl\tXu\tXr")
    x = iteration(a,b)    
    while True:
        if  n > 1:
            if (x-iter_holder) < 10**(-7) and (x-iter_holder) > -10**(-7):
                break
        if n ==1 or (f(a)*f(x)) < 0:
            b = x
        elif n ==1 or (f(x)) < 0:
            a = x
        elif f(x) == 0:
            break
        if n == 1:
            print("{}\t{%.6f}\t{%.6f}\t{%.6f}\t-".format(n, a, b, x))
        else:
            print("{%.6f}\t{%.6f}\t{%.6f}\t{%.6f}\t{%.6f}-".format(n, a, b, x,x-iter_holder))
        iter_holder = x
        x = iteration(a,b)
        n +=1

main()
