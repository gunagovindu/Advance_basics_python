n=10
try:
    res=n/0
except ZeroDivisionError:
    print("can't divisible by Zero!")

   # cjdhvdk

try:
    num=int(input("enter a number:"))
    res=100/num
except ZeroDivisionError:
    print("can't divisible!")
except ValueError:
   print("please enter valid number")
else:
    print("result:",res)
finally:
    print("finally block executed")

