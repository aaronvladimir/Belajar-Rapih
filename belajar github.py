print(
    "Halo kawan kawan, ini adalah project python pertama saya " \
    "yang saya akan masukan github menggunakan terminal, belajar github..."
    "Projectnya adalah membuat kalkulator " \
    "sederhana dengan python, semoga berhasil" \
)

angka1=int(input("Masukan angka pertama: "))
angka2=int(input("Masukan angka kedua: "))
opsi=input("Pilih operasi (+, -, *, /): ")
if opsi == "+":
    hasil = angka1 + angka2
elif opsi == "-":
    hasil = angka1 - angka2
elif opsi == "*":
    hasil = angka1 * angka2
elif opsi == "/":
    hasil = angka1 / angka2
else:
    hasil=print("Opsi tidak valid,silakan pilih operasi yang benar")
print("hasilnya adalah:", hasil)