# Latihan 3: Konversi suhu Celsius ke Fahrenheit dan Kelvin
#
# Rumus:
#   fahrenheit = (celsius * 9 / 5) + 32
#   kelvin     = celsius + 273.15

# Input suhu dalam Celsius
suhu_celsius = 25

# Proses konversi
suhu_fahrenheit = (suhu_celsius * 9 / 5) + 32
suhu_kelvin = suhu_celsius + 273.15

# Output hasil dengan 2 angka di belakang koma
print("=== Konversi Suhu ===")
print(f"Celsius    : {suhu_celsius:.2f} C")
print(f"Fahrenheit : {suhu_fahrenheit:.2f} F")
print(f"Kelvin     : {suhu_kelvin:.2f} K")
