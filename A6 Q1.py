n = int(input("Enter any number "))
divisors = []
for i in range(1,n):
    if n%i==0:
        divisors.append(i)
s = sum(divisors)
if s == n:
    print("Yes this number is a perfect number")
else:
    print("No, its not a perfect number")
