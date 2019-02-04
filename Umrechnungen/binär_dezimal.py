eingabe = str(input("Bitte die Binärzahl eingeben: "))
x = len(eingabe)-1
ausgabe = int()

for i in eingabe :
	if i == "1":
		ausgabe = ausgabe + 2**x
	x = x-1

print(ausgabe)