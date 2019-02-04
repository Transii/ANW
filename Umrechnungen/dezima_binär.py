eingabe = int(input("Gebe deine Zahl ein: "))
binär_zahl = int()
n=0
while eingabe > 0:
	binär_zahl = ((eingabe % 2 )*10**n) + binär_zahl
	eingabe = int(eingabe/2)
	n = n+1
print(binär_zahl)
