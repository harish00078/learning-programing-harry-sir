#sum(n) = sum(n-1) + n (this is the formula to find out the sum of the first natural_number. 
def sum_naturalnumber(n):
    if n == 1 or n == 0:  # 2. here we gave him a condition.in this way our  function do not gave  us a (zero value)
        return 1
    return n + sum_naturalnumber(n-1)  # 1. we did not use the n * (n-1)formula directly because this will multiply with (zero) and all the values become zero automatically.
    
    
print(sum_naturalnumber(10))
# in between 10 we have a 10 natural numbers like(1,2,3,4,5,6,7,8,9,10) 
 
