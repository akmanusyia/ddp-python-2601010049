# Latihan 2: Menghitung luas dan keliling persegi panjang
#
# Rumus:
#   luas    = panjang * lebar
#   keliling = 2 * (panjang + lebar)
#
# Trace table (nilai variabel setelah setiap baris dijalankan):
#
# | Baris | Perintah                              | panjang | lebar | luas | keliling |
# |-------|---------------------------------------|---------|-------|------|----------|
# | 1     | panjang = 12                          | 12      | -     | -    | -        |
# | 2     | lebar = 5                             | 12      | 5     | -    | -        |
# | 3     | luas = panjang * lebar                | 12      | 5     | 60   | -        |
# | 4     | keliling = 2 * (panjang + lebar)      | 12      | 5     | 60   | 34       |
# | 5     | print(...) menampilkan hasil          | 12      | 5     | 60   | 34       |

# Input data (dalam satuan cm)
panjang = 12
lebar = 5

# Proses perhitungan
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

# Output hasil
print("=== Persegi Panjang ===")
print(f"Panjang  : {panjang} cm")
print(f"Lebar    : {lebar} cm")
print(f"Luas     : {luas} cm^2")
print(f"Keliling : {keliling} cm")
