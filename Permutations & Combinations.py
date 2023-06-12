# x = int(input(" ENTER ANY NUM : "))
# factorial = 1
# for i in range(1, x+1):
#     factorial = i*factorial
# print(factorial)
# <=============Combinations=============>

import math


def factorial(x):
    factorial = 1
    for i in range(1, x+1):
        factorial = i*factorial
    return factorial


try:
    n = int(input(" ENTER n : "))
    r = int(input(" ENTER r : "))
    desc = int(input('''\n1. Permutations\n2. Combinations\n ======> '''))

    if desc == 1:
        num = factorial(n)
        deno = factorial(r)
        print("nPr : ", int(num/deno))
    elif desc == 2:
        num = factorial(n)
        deno = factorial(r)*(factorial(n-r))
        print("nCr : ", int(num/deno))
    else:
        print(" Invalid descision ")
        

except Exception as e:
    print(" Please enter valid Integer only : "+str(e))