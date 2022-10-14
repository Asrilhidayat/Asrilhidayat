# Deskriptif
# membuat variabel nama barang = kosmetik
# membuat variabel harga barang = 100000
# membuat variabel persen barang = 
# input nama barang 
# input harga barang
# menghitung harga barang
# harga barang * persen / 100
# print harga barang beserta nama barang

while(True):
    nama_barang = input("masukan nama barang : ")
    harga_barang =int(input("masukan harga barang : "))
    persen = input("masukan persen barang : ")
    harga_keuntungan = int(harga_barang) * int(persen) / 100
    harga_jual = int(harga_barang) + harga_keuntungan
    print(nama_barang, "dijual dengan: ", harga_jual)


    apakah_lanjut = input ("apakah anda ingin melanjutkan?Y untuk Ya N untuk No : ")
    if(apakah_lanjut !="Y"):
        break


