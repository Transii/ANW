zahl = int(input("Bitte Zahl eingeben: "))
quersumme = 0

while zahl != 0:
	quersumme = quersumme + int((zahl % 10))
	zahl = int(zahl/10)


print(quersumme)