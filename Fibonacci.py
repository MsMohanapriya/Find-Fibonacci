def FibonacciRecursion(number):
    
    if number==0:
        return 0
    if number==1:
        return 1
    return FibonacciRecursion(number-1)+FibonacciRecursion(number-2)

    
    
number=int(input("enter the input: "))
print(FibonacciRecursion(number))
