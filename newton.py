import math

def f(x):           # our function
    e = 2.71
    return x * e**((x**2)/4) -3 * x + 2
def f_derive(x):        #derivative of our function
    e = 2.71
    return e ** ((x**2)/4) + x * 2 * x / 4 * e**((x**2)/4) - 3

""" def f(x):       # function given in the question
    return x**(1/3) + math.log(x) """

def f_derive(x):
    return 1/3 * x**(-2/3) +1/x

    
def iterate(start):     # newton's formula
    return start - f(start)/f_derive(start), f(start), f_derive(start) #returns the next point of iteration and values of the functions


def main():
    next_point = 1      #starting point of iteration
    n = 1
    while True:             #if difference of iteration points is between -10^(-7) and 10^(-7) brake the loop
         
        if n ==1 or (next_point - previous_point) > 10 ** (-7) or (next_point - previous_point) < (-10 ** (-7)) :  
            
            previous_point = next_point    # previous_poin holds the previous position of next_point
            next_point, y, y_deriv = iterate(next_point)
            
            print("step= {}       f(x)= {}      f'(x)= {}      root= {}".format(n, round(y, 2), round(y_deriv, 2), next_point))
            #round() function limits the floating point to 2 decimal number. For example 2.456879 -> 2.45

            n += 1      #iteration number increases in each step of iteration 

        else:
            #print("{}       {}      {}".format(n, round(y, 2), round(y_deriv, 2)))
            break
    
main()      # calling the main function
  