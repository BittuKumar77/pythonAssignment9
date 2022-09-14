# 10. Write a python script to print first 10 multiples of N.

n=int(input("Enter the Number: "))
i=1
while i<=10:
    print(n,"*",i,"=",i*n)
    i+=1
print()