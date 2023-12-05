#Get input from the user of n to calculate its number in
#the Fibbonacci Sequece

def Fibonacci(n):
    if n<=1:
        return n
    
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
    

n = int(input("Enter a positive number: "))

if n < 0:
    print("Invalid entry! Please enter a positive integer.")

result = Fibonacci(n)

print(f"Number in the Fibonacci Sequence is {result}")