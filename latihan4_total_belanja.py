# Latihan 4: Menghitung total belanja dengan PPN 11%
#
# Rumus:
#   subtotal = jumlah semua (harga * jumlah barang)
#   ppn      = subtotal * 11%
#   total    = subtotal + ppn

# Tarif PPN
TARIF_PPN = 0.11

# Data barang belanjaan: harga satuan (Rupiah) dan jumlahnya
harga_buku = 15000
jumlah_buku = 3

harga_pensil = 3000
jumlah_pensil = 5

harga_penghapus = 2500
jumlah_penghapus = 2

# Menghitung harga per barang
total_buku = harga_buku * jumlah_buku
total_pensil = harga_pensil * jumlah_pensil
total_penghapus = harga_penghapus * jumlah_penghapus

# Menghitung subtotal, PPN, dan total bayar
subtotal = total_buku + total_pensil + total_penghapus
ppn = subtotal * TARIF_PPN
total_bayar = subtotal + ppn


def format_rupiah(angka):
    """Mengubah angka menjadi format Rupiah, contoh: Rp 72.150"""
    return "Rp " + f"{angka:,.0f}".replace(",", ".")


# Menampilkan struk belanja
print("=" * 40)
print("            STRUK BELANJA")
print("=" * 40)
print(f"Buku       {jumlah_buku} x {format_rupiah(harga_buku):>10} = {format_rupiah(total_buku):>10}")
print(f"Pensil     {jumlah_pensil} x {format_rupiah(harga_pensil):>10} = {format_rupiah(total_pensil):>10}")
print(f"Penghapus  {jumlah_penghapus} x {format_rupiah(harga_penghapus):>10} = {format_rupiah(total_penghapus):>10}")
print("-" * 40)
print(f"Subtotal         : {format_rupiah(subtotal):>15}")
print(f"PPN 11%          : {format_rupiah(ppn):>15}")
print(f"Total Bayar      : {format_rupiah(total_bayar):>15}")
print("=" * 40)
