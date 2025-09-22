#Problem-3 : generate odd number series with condition
n = int(input("Enter a number: "))
length = n//2 if n % 2 ==0 else (n//2)+1
series =[]
for i in range(length):
    series.append(2 * i+1)
print("Series:",series)