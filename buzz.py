# find BUZZ Number from n tu m
# BUZZ number: A number divisible by 7 and end with 7
n=int(input("Enter a number: "))

m=int(input("Enter a number: "))
i=n

for i in range(n,m+1,++i):

    if(i%7==0 and i%10==7):
        print(i, end=" ")
   