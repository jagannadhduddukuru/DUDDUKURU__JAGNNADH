#Problem -2 : generate series 1, 3, 5 ................ till n terms
n = int(input("Enter a number : "))
series = []
for i in range(n):
    series.append(2 * i + 1)
print("series: ",series)