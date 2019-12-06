print("==================================================================================")
print("|                             PROGRAM INPUT NILAI NILAI                          |")
print("==================================================================================")

while True:
    print("")
    c = input ("L)ihat, T)ambah, U)bah, H)apus, C)ari, K)eluar: ")
    if c.lower() == 'l' :
        break
print("Daftar Nilai")
print("==================================================================================")
print("| NO |   NAMA    |    NIM     |  TUGAS     |     UTS     |   UAS     |   AKHIR   |")
print("==================================================================================")
print("                                  TIDAK ADA DATA                                  ")
print("==================================================================================")
while True:
    print("")
    c = input ("L)ihat, T)ambah, U)bah, H)apus, C)ari, K)eluar: ")
    if c.lower() == 't' :
        break
print("Tambah Data")
nilai = []
nim = input("NIM: ")
nama = input("Nama: ")
nilaiUts = int(input("Nilai UTS: "))
nilaiUas = int(input("Nilai UAS: "))
nilaiTugas = int(input("Nilai Tugas: "))
nilaiAkhir = (nilaiUts * 35/100) + (nilaiUas * 35/100) + (nilaiTugas * 35/100)

nilai.append([nama, nim, nilaiTugas, nilaiUts, nilaiUas, int(nilaiAkhir)])l

while True:
    print("")
    c = input ("L)ihat, T)ambah, U)bah, H)apus, C)ari, K)eluar: ")
    if c.lower() == 'l' :
        break
print("\n    Daftar Nilai   ")
print("==================================================================================")
print("| NO |   NAMA    |    NIM     |  TUGAS     |     UTS     |   UAS     |   AKHIR   |")
print("==================================================================================")
i = 0
for item in nilai:
    i += 1
    print("| {no:2d} | {nama:12s} | {nim:9s} | {nilaitugas:5d} | {nilaiUTS:5d} | {nilaiUAS:5d} | {nilaiAKHIR:6.2f} |"
        .format(no=i, nama=item[0], nim=item[1], nilaitugas=item[2], nilaiUTS=item[3], nilaiUAS=item[4], nilaiAKHIR=item[5]))
print("==================================================================================")

