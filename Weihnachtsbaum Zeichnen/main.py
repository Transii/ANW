eingabe = int(input("Bitte die Breite des Baumes angeben:"))
leer = " "
x = "x"
n = 1 
stamm = f'{eingabe*leer}{x*n}'

for m in range(eingabe):
	print(f'{eingabe*leer}{x*n}')
	print(f'{eingabe*leer}{x*n}')	
	n = (n+2)
	eingabe = (eingabe -1)

print(stamm)
print(stamm)