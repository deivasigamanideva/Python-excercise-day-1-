def odd(num):
    if num % 2:
        return print( num,"is odd")
    else :
        return print(num,"is not odd")
  
def eve(num):
    if num / 2 :
        return print (num,"is even")
    else :
        return print (num,"is not enen")
def pri(num):
    if num<=1:
        return False
    if num <=3:
        return True
    if num % 2 == 0 or num % 3 ==0:
        return False
    i = 5
    while i * i <= num:
        if num % i==0 or num % (i+2)==0:
            return False
        i += 6
        return True        
n = int(input("enter a number "))
od=odd(n)
ev=eve(n)
if pri(n):
    print(n,"is prime")
else:
    print(n,"not prime")
