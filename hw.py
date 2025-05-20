n=[10,20,31,40,50]
a=filter(lambda  x:x % 2==0,n)
b=filter(lambda  x:x % 2!=0,n)
print("Even numbers:",list(a))
print("Odd numbers:",list(b))