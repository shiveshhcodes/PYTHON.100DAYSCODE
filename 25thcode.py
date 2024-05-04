# here we are gonna learn about recursion methods!! they are 
# different from functions , as they call inside the functions of a number

# def ap_nth_term(a1, d, n):
#     """
#     Calculate the nth term of an arithmetic progression.

#     Parameters
#     ----------
#     a1 : int
#         The first term of the arithmetic progression.
#     d : int
#         The common difference.
#     n : int
#         The term to calculate.

#     Returns
#     -------
#     int
#         The value of the nth term.
#     """
#     return a1 + (n - 1) * d  # Formula for nth term in AP


# def ap_sum(a1, d, n):
#     """
#     Calculate the sum of the first n terms in an arithmetic progression.

#     Parameters
#     ----------
#     a1 : int
#         The first term of the arithmetic progression.
#     d : int
#         The common difference.
#     n : int
#         The number of terms.

#     Returns
#     -------
#     int
#         The sum of the first n terms.
#     """
#     # Formula for sum of first n terms in AP
#     return (n / 2) * (2 * a1 + (n - 1) * d)


# # Example usage:
# # First term
# a1 = 3
# # Common difference
# d = 5
# # Number of terms
# n = 10

# # Calculate the nth term
# nth_term = ap_nth_term(a1, d, n)
# print("The 10th term of the arithmetic progression is:", nth_term)

# # Calculate the sum of the first 10 terms
# sum_terms = ap_sum(a1, d, n)
# print("The sum of the first 10 terms is:", sum_terms)


# print("please give values as asked - ")
# a1 = int(input("Give me value of a : "))
# d = int(input("Give me value of d : "))
# n = int(input("Give me value of n : "))


# def APnthTerm (a1 , d , n):
#     return a1 + (n - 1) * d

# def APsum (a1 , d , n):
#     return (n / 2) * (2 * a1 + (n - 1) * d)
#     # return (n / 2) * (2 * a1 + (n-1) * d)
 

# Nthterm = APnthTerm(a1,d,n)
# print("The Nth term of AP is : " , Nthterm)

# Sum = APsum (a1 , d , n)
# print("The sum of AP is " ,  Sum)

# now lets create a euqation for fibonacci sequence.

# def Fibo(f):
#     if (f==0 or f==1):
#         return 1
#     else:
#         return f(f - 1) + f(f - 2)
    
# print("Enter a value , and i will create a Fibonacci Equation for that")
# f = int(input("Value = "))
# print("The fibonacci sequence is - " , Fibo)



# FIBONACCHI EQUATION 


# def fibo_sequence(n):
#     fib_sequence = [0 , 1]
    
#     for i in range (1 , n):
#      next_term = (fib_sequence[-1] + fib_sequence[-2])
#      fib_sequence.append(next_term)
#     #  fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#         # if i == 0: 
#         #  fib_sequence.append(0)
#         # elif i == 1:
#         #     fib_sequence.append(1)
#         # else:
#     return fib_sequence
# n = int(input("Enter a value to get Fibo Sequence : "))

# result = fibo_sequence(n)

# print("The Fibonacci sequnce of" , n , "terms is" , result )


# AP

def AP(a1 , n , d):
    AP_sequence = []
    for i in range(n):
     AP_sequence.append(a1 + i * d )
    return AP_sequence

a1 = int(input("Enter a value of a : "))
n = int(input("Enter a value of n : "))
d = int(input("Enter a value of d : "))

result = AP(a1 ,n , d)

print("The AP of given values are"  , result )