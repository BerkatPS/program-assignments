nama = input("Masukkan nama karyawan: ")
nomor_pegawai = input("Masukkan nomor pegawai: ")
gaji = float(input("Masukkan gaji pokok: "))
jam_lembur = int(input("Masukkan jumlah jam lembur: "))
hari_tidak_masuk = int(input("Masukkan jumlah hari tidak masuk kerja: "))
status_menikah = input("Apakah karyawan sudah menikah? (y/n): ")

bpjs = 0.15
pajak = 0.05
tarif_lembur_perjam = 50000

potongan_bpjs = gaji * bpjs
potongan_pajak = gaji * pajak
potongan_lembur = jam_lembur * tarif_lembur_perjam
potongan_tidak_masuk = hari_tidak_masuk * 50000

gaji_bersih = gaji - potongan_bpjs - potongan_pajak - potongan_lembur - potongan_tidak_masuk

if status_menikah == 'y' or status_menikah == "Y":
    gaji_bersih += 500000

print("==================================")
print("\nRincian Gaji:")
print("Nama Karyawan:", nama)
print("Nomor Pegawai:", nomor_pegawai)
print("Gaji Pokok: Rp.", gaji)
print("Potongan BPJS: Rp.", potongan_bpjs)
print("Potongan Pajak: Rp.", potongan_pajak)
print("Potongan Lembur: Rp.", potongan_lembur)
print("Potongan Tidak Masuk Kerja: Rp.", potongan_tidak_masuk)
if status_menikah == 'y':
    print("Tunjangan Menikah: Rp. 500.000")
print("Gaji Bersih: Rp.", gaji_bersih)
print("===================================")