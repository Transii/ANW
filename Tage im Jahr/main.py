tag = int(input("Bitte Tag eingeben:"))
monat = int(input("Bitte Monat eingeben:"))
jahr = int(input("Bitte Jahr eingeben:"))
erg = int()

for m in range(1,monat+1):

	if (m == 2 or m== 4 or m==6 or m==9 or m==11):
		erg = (erg+30)
	else:
		erg = (erg+31)

	erg = erg+tag

	if monat > 2:
		if jahr/4==0:
			if jahr/100==0:
				if jahr/400==0:
					erg=(erg-1)
				else:
					erg=(erg-2)
			else:
				erg=(erg-1)
		else:
			erg=(erg-2)

print(erg)