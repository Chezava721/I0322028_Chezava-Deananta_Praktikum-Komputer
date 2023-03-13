print("Daftar Gaji")
nama =  input("Masukkan Nama")
keljamkerja = int(input("Masukkan Kelebihan Jam Kerja"))
golongan = int(input("Masukkan Golongan"))

gajipokok = golongan * 1000000
lembur = keljamkerja * 200000
pendapatan = gajipokok + lembur

print("Nama = ", nama)
print("Golongan = ", golongan)
print("Gaji Pokok = ", gajipokok)
print("Lembur = ", lembur)
print("Pendapatan = ", pendapatan)