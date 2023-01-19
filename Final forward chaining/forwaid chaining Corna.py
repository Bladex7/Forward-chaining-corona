
hasil = []

H1 = ("Berpotensi besar positif Korona")
H2 = ("Berpotensi kecil positif Korona")
H3 = ("beresiko")

def kali(gejala) :
	result = 1
	for x in gejala:
		result = result * x
	return result

print("-"*28)
nama = input (" Nama\t: ")
print(" Hallo "+ nama )
while True:
	while True:
		G1 = input("\n Apakah anda mengalami Demam? (y/n): ")
		if (G1 == "y"):
			hasil.append(1)
			break
		elif (G1 == "n") :
			hasil.append(6)
			break
		else :
			print("\n Maaf inputan hanya (y/n) ")
	while True:
		G2 = input("\n Apakah anda mengalami Pusing? (y/n): ")
		if (G2 == "y"):
			hasil.append(2)
			break
		elif (G2 == "n") :
			hasil.append(1)
			break
		else :
			print("\n Maaf inputan hanya (y/n) ")
	while True:
		G3 = input("\n Apakah anda mengalami Bersin Bersin? (y/n): ")
		if (G3 == "y"):
			hasil.append(3)
			break
		elif (G3 == "n") :
			hasil.append(2)
			break
		else :
			print("\n Maaf inputan hanya (y/n) ")
	while True:
		G4 = input("\n Apakah anda mengalami Batuk? (y/n): ")
		if (G4 == "y"):
			hasil.append(4)
			break
		elif (G4 == "n") :
			hasil.append(3)
			break
		else :
			print("\n Maaf inputan hanya (y/n) ")
	while True:
		G5 = input("\n Apakah anda mengalami sakit Tenggorokan? (y/n): ")
		if (G5 == "y"):
			hasil.append(5)
			break
		elif (G5 == "n") :
			hasil.append(4)
			break
		else :
			print("\n Maaf inputan hanya (y/n) ")
	while True:
		G6 = input("\n Apakah anda mengalami Kelelahan? (y/n): ")
		if (G6 == "y"):
			hasil.append(6)
			break
		elif (G6 == "n") :
			hasil.append(5)
			break
		else :
			print("\n Maaf inputan hanya (y/n) ")
	while True:
		G7 = input("\n Apakah anda mengalami Bersin Nyeri Dada? (y/n): ")
		if (G7 == "y"):
			hasil.append(7)
			break
		elif (G7 == "n") :
			hasil.append(6)
			break
		else :
			print("\n Maaf inputan hanya (y/n) ")

	if kali(hasil) == 5040:
		print(H1)
	elif kali(hasil) == 2520:
		print(H1)
	elif kali(hasil) == 2016:
		print(H1)
	elif kali(hasil) == 1728:
		print(H1)
	elif kali(hasil) == 1800 and hasil[1] == 1 :
		print(H2)
	elif kali(hasil) == 2700:
		print(H2)
	elif kali(hasil) == 21600 :
		print(H2)
	elif kali(hasil) == 2880 :
		print(H2)
	elif kali(hasil) == 10800 :
		print(H3)
	elif kali(hasil) == 16200 :
		print(H3)
	elif kali(hasil) == 1350 :
		print(H3)
	elif kali(hasil) == 1800 and hasil[1] == 2 :
		print(H3)
	else :
		print("maaf sistem kami belom bisa menjawab pertanyaan anda")

	#print(kali(hasil))

	pilihan = input("ingin mengulangi program? (y/n) ")
	if  (pilihan =="n" or pilihan =="N") :
		print("\n semoga harimu senin teros")
		break
	hasil.clear ()


