nama = input("Masukan Nama: ")
gaji_pokok = float(input("Masukan gaji pokok: "))

tunjangan = 0.20 * gaji_pokok
pajak = 0.15 * (gaji_pokok + tunjangan)
gaji_bersih = gaji_pokok + tunjangan - pajak

print("nama: ", nama)
print("gaji_pokok: ", gaji_pokok)
print("gaji_bersih", gaji_bersih)