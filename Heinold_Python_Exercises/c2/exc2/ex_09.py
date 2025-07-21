""" The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
 number thereafter is the sum of the two preceding numbers. Write a program that asks the
 user how manyFibonacci numbers to print and then prints that many.
 1,1,2,3,5,8,13,21,34,55,89..."""

# F(0) = F(n-1) + F(n-2)

fibonacci_count = int(input("How many fibonacci numbers do you want to print? "))
curr = 0
prev = 1
for i in range(0, fibonacci_count):
    next_ = prev + curr
    prev = curr
    curr = next_
    print(next_)
    print(f"the value of counter is {curr}")
    print(f"the value of counter is {prev}")
