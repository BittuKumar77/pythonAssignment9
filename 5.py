# 5. Write a python script to print first N odd natural numbers in reverse order

n=int(input("Enter the Number: "))
i=1
while i<=n:
    print(n*2-i,end=" ")
    n -= 1
print()