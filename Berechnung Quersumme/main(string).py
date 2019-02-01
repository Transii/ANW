eingabezahl = str(input("Bitte eine Zahl eingeben: "))
erg = 0

for ein in eingabezahl[0:len(eingabezahl)]:
	erg = erg+int(ein)

print(erg)


