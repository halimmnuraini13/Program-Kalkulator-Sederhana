print("===========================================")
print("       Program Kalkulator Sederhana       ")
print("===========================================")

while True:
    print("\nSelect operation:")
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")
    print("5. keluar")
    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "5":
        print("Terima kasih telah menggunakan kalkulator.")
    
    if pilihan == "1" or pilihan == "2" or pilihan == "3" or pilihan == "4":
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))

        if pilihan == "1":
            def penjumlahan(a, b):
                print(f"{a} + {b} = {a + b}")
            penjumlahan(a, b)

        elif pilihan == "2":
            def pengurangan(a, b):
                print(f"{a} - {b} = {a - b}")
            pengurangan(a, b)

        elif pilihan == "3":
            def perkalian(a, b):
                print(f"{a} * {b} = {a * b}")
            perkalian(a, b)

        elif pilihan == "4":
            def pembagian(a, b):
                print(f"{a} / {b} = {a / b}")
            pembagian(a, b)

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")