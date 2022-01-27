# Author: MOG 1/27/22

# Question 1
def food_costs(groceries,costs):
    for n, x in enumerate(groceries):
        for i, y in enumerate(x):
            groceries[n][i] += ": ${}".format(costs[n * 3 + i])
    return groceries

print(food_costs([['apple','pear','banana'],['salmon','tuna','cod'],['milk','eggs','yogurt']],[1.99,2.99,0.99,9.99,10.99,6.99,3.49,2.49,1.49]))

# Question 2
def factorial(x):
    product = 1
    for i in range(1,x + 1):
        product *= i
    return product

print(factorial(5))

# Question 3
def fib_nums(n):
    seq = [0,1]
    if n == 1:
        return [0]
    if n == 2:
        return [0,1]
    else:
        for x in range(n - 2):
            seq.append(seq[x] + seq[-1])
    return seq

fib_nums(10)