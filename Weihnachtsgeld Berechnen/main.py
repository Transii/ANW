Alter = int(input("Bitte das alter Angeben:"))
Gehalt = int(input("Bitte das Gehalt angeben:"))
BZ = int(input("Bitte die Betriebszugehörigkeit angeben:"))
WG = ""


if Alter >= 50:
	if BZ >= 20:
		WG = (0.45*Gehalt)
	else:
		if Alter > 55:
			WG = (0.4*Gehalt)
		else:
			if BZ >= 15:
				WG = (0.4*Gehalt)
			else:
				WG = (0.3*Gehalt)
else:
	if BZ >= 15:
		WG = (0.4*Gehalt)
	else:
		WG = (0.3*Gehalt)

print(WG)