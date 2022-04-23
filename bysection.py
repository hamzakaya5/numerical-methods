import math #this library is used to be able to use naturel logarith function

"""
def f(x):       # function given in the question
    return x**(1/3) + math.log(x)
"""

def f(x):               #function to find its roots
    return x**4 + 7 * x**3 -11 * x**2 +5

def sign(a):        #checks wheter a number is pozitif or negative 
    if a < 0:       
        return -1
    elif  a > 0:
        return 1
    elif a == 0:
        return 0


def iterate(lower, upper):          # taking input from user as lowest and highest numbers of the domain
    lower_list = []                 
    upper_list = []                 # data will be saved to this arrays
    interval_holder_list = []    
    func_value_list = []                  
    while True:
        interval_holder = (lower+upper)/2          # middle point of our domain
        midValue = f(interval_holder)
        lower_value = f(lower)
        higher_value = f(upper)
        lower_list.append(lower)
        upper_list.append(upper)
        interval_holder_list.append(interval_holder)
        func_value_list.append(f(midValue))


        if sign(midValue) == sign(higher_value):    # if the value of middle point is equals to the higher value, that means
            upper = interval_holder                # root is nearer to the lower value
                                                    # and higher boundry is being equal to the previous middle point
 
        elif sign(midValue) == sign(lower_value):   # the same process with the "if" block
            lower = interval_holder
        
        elif sign(midValue) == 0:                   # if value is equal to zero, that means we finally found the root
            print("your root is => {}".format(interval_holder)) # printing the root to the screen
            break
        print("\n")
    return lower_list, upper_list, interval_holder_list, func_value_list



def plot_graph(arr1, arr2, arr3, arr4):
    print("---------DATA---------")
    print(" n       Xl       Xu         Xr          Xu-Xr       f(Xr)")
    for i in range(len(arr1)):
        print(" {}      {}       {}      {}         {}          {}".format(i, round(arr1[i],5), round(arr2[i],5), round(arr3[i],5), round(arr3[i]-arr2[i],5),round(arr4[i],5)))

def main():
    while True:
        try:

            lower = float(input("type lower boundary"))
            higher = float(input("type upper boundary"))
            if not sign(f(lower)) == sign(f(higher)):
                arr1, arr2,arr3, arr4 = iterate(lower, higher)
                plot_graph(arr1, arr2, arr3, arr4)
                break
            else:
                print("wrong number interval!! Sign of the value of the function in two boundary are equal")
        except ValueError as a:
            print(a)
            print("you cannot write a number in the natural logarithm function less than or equal to 0")

main()