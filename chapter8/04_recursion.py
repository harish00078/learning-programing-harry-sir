# recursion = recursion is a function which calls itself .it is used to directly use a mathematical formula as a function.

# n! = 1 * 2 * 3 * 4.....*n
# 
# n = 4
# product = 1
# for i in range(n):
#     product =  product * (i+1) # here we use(i+1) because if we use simply(i) here this will gave us a zero value beacuse our factorial system will we work acc to the binary value.that by we use (i+1) this start the factorial value from the (one) instead of starting from zero 
# # print(product)


# we create function that will find out the factorials of any  numbers.          



# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product


# #print(factorial_iter(5))
# f = factorial_iter(5)
# print(f)

# using recursion to find out the factorial.

# n! = 1 * 2 * 3 * 4.....*n
# n! = [1 * 2 * 3 * 4....n-1] *n
# n! = n * [n-1]!

def factorial_recursive(n):
    if n == 1 or n == 0:  # 2. here we gave him a condition.in this way our  function do not gave  us a (zero value)
        return 1
    return n * factorial_recursive(n-1)  # 1. we did not use the n * (n-1)formula directly because this will multiply with (zero) and all the values become zero automatically.
    
    
print(factorial_recursive(5))

                    


