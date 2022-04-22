import mysql.connector as mysql
import os
from tabulate import tabulate
from DateTime import DateTime

db = mysql.connect(
    host='localhost',
    user='root',
    password='',
    database='majalah_system'
)

def Nambah_data_majalah(db):
    print("\nInsert data majalah")
    print("Syarat 1 : ID distributor suatu majalah harus sama dengan daftar ID distributor")
    print("Syarat 2 : ID penulis suatu majalah harus sama dengan daftar ID penulis")
    Show_majalah(db)
    Show_distributor(db)
    Show_penulis(db)
    kode_majalah = input("Kode majalah : ")
    id_distributor = input("ID distributor : ")
    id_penulis = input("ID penulis : ")
    nama_majalah = input("Nama majalah : ")
    jumlah_stok = input("Jumlah stok : ")
    harga = input("Harga majalah : ")

    val = (kode_majalah, id_distributor, id_penulis, nama_majalah, jumlah_stok, harga)
    mycursor = db.cursor()
    sql = "INSERT INTO majalah (kode_majalah, id_distributor, id_penulis, nama_majalah, jumlah_stok, harga) VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))

def Nambah_data_pegawai(db):
    print("\nInsert data pegawai")
    id_pegawai = input("ID Pegawai : ")
    nama_pegawai = input("Nama : ")
    alamat = input("Alamat : ")
    no_telpon = input("Nomor Telepon : ")

    val = (id_pegawai, nama_pegawai, alamat, no_telpon)
    mycursor = db.cursor()
    sql = "INSERT INTO pegawai (id_pegawai, nama_pegawai, alamat, no_telpon) VALUES (%s,%s,%s,%s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))

def Nambah_data_pelanggan(db):
    print("\nInsert data pelanggan")
    print("Syarat : Kode majalah seorang pelanggan harus sama dengan daftar kode majalah")
    Show_pelanggan(db)
    Show_majalah(db)
    id_pelanggan = input("ID Pelanggan : ")
    kode_majalah = input("Kode Majalah : ")
    no_telepon = input("Nomor Telepon : ")
    nama_pelanggan = input("Nama : ")
    alamat = input("Alamat : ")

    val = (id_pelanggan, kode_majalah, no_telepon, nama_pelanggan, alamat)
    mycursor = db.cursor()
    sql = "INSERT INTO pelanggan (id_pelanggan, kode_majalah, no_telepon, nama_pelanggan, alamat) VALUES (%s,%s,%s,%s,%s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))

def Nambah_data_penulis(db):
    print("\nInsert data penulis")
    id_penulis = input("ID Penulis : ")
    nama_penulis = input("Nama : ")
    email = input("Email : ")
    no_telepon = input("Nomor Telepon : ")

    val = (id_penulis, nama_penulis, email, no_telepon)
    mycursor = db.cursor()
    sql = "INSERT INTO penulis (id_penulis, nama_pelanggan, email, no_telepon) VALUES (%s,%s,%s,%s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))

def Nambah_data_distributor(db):
    print("\nInsert data penulis")
    id_distributor = input("ID distributor : ")
    nama_distributor = input("Nama : ")
    alamat = input("Alamat : ")

    val = (id_distributor, nama_distributor, alamat)
    mycursor = db.cursor()
    sql = "INSERT INTO penulis (id_distributor, nama_distributor, alamat) VALUES (%s,%s,%s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))

def Show_majalah(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM majalah")
    myresult = mycursor.fetchall()

    print(tabulate(myresult, headers=["kode_majalah", "id_distributor", "id_penulis", "nama_majalah", "jumlah_stok", "harga"], tablefmt="grid"))

def Show_pelanggan(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM pelanggan")
    myresult = mycursor.fetchall()

    print(tabulate(myresult, headers=["id_pelanggan", "kode_majalah", "no_telepon", "nama_pelanggan", "alamat"], tablefmt="grid"))

def Show_pegawai(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM pegawai")
    myresult = mycursor.fetchall()

    print(tabulate(myresult, headers=["id_pegawai", "nama_pegawai", "alamat", "no_telpon"], tablefmt="grid"))

def Show_penulis(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM penulis")
    myresult = mycursor.fetchall()

    print(tabulate(myresult, headers=["id_penulis", "nama_penulis", "email", "no_telepon"], tablefmt="grid"))

def Show_distributor(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM distributor")
    myresult = mycursor.fetchall()

    print(tabulate(myresult, headers=["id_distributor", "nama_distributor", "alamat"], tablefmt="grid"))

def Update_data_majalah(db):
    print("\nUpdate data majalah")
    print("Syarat 1 : ID distributor tidak bisa diubah")
    print("Syarat 2 : ID penulis tidak bisa diubah")
    Show_majalah(db)
    kode_majalah = input("Kode majalah : ")
    nama_majalah = input("Nama majalah baru : ")
    jumlah_stok = input("Jumlah stok baru : ")
    harga = input("Harga majalah baru : ")

    mycursor = db.cursor()
    val = (kode_majalah, nama_majalah, jumlah_stok, harga)
    sql = "UPDATE pegawai SET nama_majalah = (%s), jumlah_stok = (%s), harga = (%s) WHERE kode_majalah = (%s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))

def Update_data_pegawai(db):
    print("\nUpdate data pegawai")
    Show_pegawai(db)
    id_pegawai = input("ID Pegawai : ")
    nama_pegawai = input("Nama baru : ")
    alamat = input("Alamat baru : ")
    no_telpon = input("Nomor telepon baru : ")
    
    mycursor = db.cursor()
    val = (id_pegawai, nama_pegawai, alamat, no_telpon)
    sql = "UPDATE pegawai SET nama_pegawai = (%s), alamat = (%s), no_telepon = (%s) WHERE id_pegawai = (%s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))

def Update_data_pelanggan(db):
    print("\nUpdate data pelanggan")
    print("Syarat : Kode majalah tidak bisa diubah")
    Show_pelanggan(db)
    id_pelanggan = input("ID Pelanggan : ")
    no_telepon = input("Nomor telepon baru : ")
    nama_pelanggan = input("Nama baru : ")
    alamat = input("Alamat baru : ")
    
    mycursor = db.cursor()
    val = (no_telepon, nama_pelanggan, alamat, id_pelanggan)
    sql = "UPDATE pelanggan SET no_telepon = (%s), nama_pelanggan = (%s), alamat = (%s) WHERE id_pelanggan = (%s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))

def Update_data_penulis(db):
    print("\nUpdate data penulis")
    Show_penulis(db)
    id_penulis = input("ID Penulis : ")
    nama_penulis = input("Nama baru : ")
    email = input("Email baru : ")
    no_telepon = input("Nomor telepon baru : ")
    
    mycursor = db.cursor()
    val = (id_penulis, nama_penulis, email, no_telepon)
    sql = "UPDATE penulis SET nama_penulis = (%s), email = (%s), no_telepon = (%s) WHERE id_penulis = (%s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))

def Update_data_distributor(db):
    print("\nUpdate data distributor")
    Show_distributor(db)
    id_distributor = input("ID distributor : ")
    nama_distributor = input("Nama baru : ")
    alamat = input("Alamat baru : ")
    
    mycursor = db.cursor()
    val = (id_distributor, nama_distributor, alamat)
    sql = "UPDATE distributor SET nama_distributor = (%s), nama_distributor = (%s), alamat = (%s) WHERE id_pegawai = (%s)"
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil disimpan".format(mycursor.rowcount))

def Delete_data_majalah(db):
    print("\nDelete data majalah")
    mycursor = db.cursor()
    Show_majalah(db)
    kode_majalah = input("Pilih kode_majalah : ")
    sql = "DELETE FROM majalah WHERE kode_majalah=%s"
    val = [kode_majalah]
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil dihapus".format(mycursor.rowcount))

def Delete_data_pegawai(db):
    print("\nDelete data pegawai")
    mycursor = db.cursor()
    Show_pegawai(db)
    id_pegawai = input("Pilih id pegawai : ")
    sql = "DELETE FROM pegawai WHERE id_pegawai=%s"
    val = [id_pegawai]
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil dihapus".format(mycursor.rowcount))

def Delete_data_pelanggan(db):
    print("\nDelete data pelanggan")
    mycursor = db.cursor()
    Show_pelanggan(db)
    id_pelanggan = input("Pilih id pelanggan : ")
    sql = "DELETE FROM pelanggan WHERE id_pelanggan=%s"
    val = [id_pelanggan]
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil dihapus".format(mycursor.rowcount))

def Delete_data_penulis(db):
    print("\nDelete data penulis")
    mycursor = db.cursor()
    Show_penulis(db)
    id_penulis = input("Pilih id penulis : ")
    sql = "DELETE FROM pelanggan WHERE id_penulis=%s"
    val = [id_penulis]
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil dihapus".format(mycursor.rowcount))

def Delete_data_distributor(db):
    print("\nDelete data distributor")
    mycursor = db.cursor()
    Show_distributor(db)
    id_distributor = input("Pilih id distributor : ")
    sql = "DELETE FROM pelanggan WHERE id_distributor=%s"
    val = [id_distributor]
    mycursor.execute(sql,val)
    db.commit()
    print("{} data berhasil dihapus".format(mycursor.rowcount))

def Subquery_majalah(db):
    kode_majalah = input("Masukkan kode majalah : ")
    mycursor = db.cursor()
    val1 = [kode_majalah]
    sql1 = "SELECT * FROM majalah WHERE kode_majalah = (%s)"
    mycursor.execute(sql1, val1)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=["kode_majalah", "id_distributor", "id_penulis", "nama_majalah", "jumlah_stok", "harga"], tablefmt="grid"))

def Subquery_pelanggan(db):
    id_pelanggan = input("Masukkan id pelanggan : ")
    mycursor = db.cursor()
    val1 = [id_pelanggan]
    sql1 = "SELECT * FROM pelanggan WHERE id_pelanggan = (%s)"
    mycursor.execute(sql1, val1)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=["id_pelanggan", "kode_majalah", "no_telepon", "nama_pelanggan", "alamat"], tablefmt="grid"))

def Subquery_pegawai(db):
    id_pegawai = input("Masukkan id pegawai : ")
    mycursor = db.cursor()
    val1 = [id_pegawai]
    sql1 = "SELECT * FROM pegawai WHERE id_pegawai = (%s)"
    mycursor.execute(sql1, val1)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=["id_pegawai", "nama_pegawai", "alamat", "no_telpon"], tablefmt="grid"))

def Subquery_penulis(db):
    id_penulis = input("Masukkan id penulis : ")
    mycursor = db.cursor()
    val1 = [id_penulis]
    sql1 = "SELECT * FROM penulis WHERE id_penulis = (%s)"
    mycursor.execute(sql1, val1)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=["id_penulis", "nama_penulis", "email", "no_telepon"], tablefmt="grid"))

def Subquery_distributor(db):
    id_distributor = input("Masukkan id distributor : ")
    mycursor = db.cursor()
    val1 = [id_distributor]
    sql1 = "SELECT * FROM distributor WHERE id_distributor = (%s)"
    mycursor.execute(sql1, val1)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=["id_distributor", "nama_distributor", "alamat"], tablefmt="grid"))

def Majalah_distributor(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT id_distributor, kode_majalah, nama_majalah, jumlah_stok, harga, nama_distributor, alamat FROM majalah NATURAL JOIN distributor")
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=["id_distributor", "kode_majalah", "nama_majalah", "jumlah_stok", "harga", "nama_distributor", "alamat"], tablefmt="grid"))

def Majalah_penulis(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT id_penulis, kode_majalah, nama_majalah, jumlah_stok, harga, nama_penulis, email, no_telepon FROM majalah NATURAL JOIN penulis")
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=["id_penulis", "kode_majalah", "nama_majalah", "jumlah_stok", "harga", "nama_penulis", "email", "no_telepon"], tablefmt="grid"))

def Pelanggan_majalah(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM pelanggan NATURAL JOIN majalah")
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=["kode_majalah", "id_pelanggan", "nama_pelanggan", "no_telepon", "alamat", "nama_majalah", "jumlah_stok", "harga"], tablefmt="grid"))

def Majalah_distributor_penulis(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM majalah NATURAL JOIN distributor")
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=["id_distributor", "kode_majalah", "id_penulis", "nama_majalah", "jumlah_stok", "harga", "nama_distributor", "alamat"], tablefmt="grid"))

def Majalah_penulis_distributor(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM majalah NATURAL JOIN penulis")
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=["id_penulis", "kode_majalah", "id_distributor", "nama_majalah", "jumlah_stok", "harga", "nama_penulis", "email", "no_telepon"], tablefmt="grid"))

def Menu(db):
    print('\n--- SELAMAT DATANG DI SISTEM PENDATAAN MAJALAH ---')
    print("Masuk Sebagai : ")
    print("1. Admin Majalah")
    print("2. Pelanggan")
    print("3. Pegawai")
    print("4. Distributor")
    print("5. Penulis")
    print("6. Fungsi Lainnya")
    print("7. Keluar")
    pilih_menu = input("Pilih Menu : ")

    if pilih_menu == "1":
        print('\n--- MENU ---')
        print('1. Menambah data majalah')
        print('2. Menambah data pegawai')
        print('3. Menampilkan data majalah')
        print('4. Menampilkan data pelanggan')
        print('5. Menampilkan data pegawai')
        print('6. Menampilkan data penulis')
        print('7. Menampilkan data distributor')
        print('8. Mengupdate data majalah')
        print('9. Menghapus data majalah')
        print('10. Menghapus data pegawai')
        print('11. Menampilkan data majalah dengan kode tertentu')
        print('12. Keluar')
        pilih_menu1 = input("Pilih aksi : ")
        if pilih_menu1 == "1":
            Nambah_data_majalah(db)
        elif pilih_menu1 == "2":
            Nambah_data_pegawai(db)
        elif pilih_menu1 == "3":
            Show_majalah(db)
        elif pilih_menu1 == "4":
            Show_pelanggan(db)
        elif pilih_menu1 == "5":
            Show_pegawai(db)
        elif pilih_menu1 == "6":
            Show_penulis(db)
        elif pilih_menu1 == "7":
            Show_distributor(db)
        elif pilih_menu1 == "8":
            Update_data_majalah(db)
        elif pilih_menu1 == "9":
            Delete_data_majalah(db)
        elif pilih_menu1 == "10":
            Delete_data_pegawai(db)
        elif pilih_menu1 == "11":
            Subquery_majalah(db)
        elif pilih_menu1 == "12":
            pass
        else:
            print("You inputed the wrong menu, please try again")

    elif pilih_menu == "2":
        print('\n--- MENU ---')
        print('1. Menambah data')
        print('2. Mengupdate data')
        print('3. Menghapus data')
        print('4. Menampilkan data pelanggan dengan id tertentu')
        print('5. Keluar')
        pilih_menu1 = input("Pilih aksi : ")
        if pilih_menu1 == "1":
            Nambah_data_pelanggan(db)
        elif pilih_menu1 == "2":
            Update_data_pelanggan(db)
        elif pilih_menu1 == "3":
            Delete_data_pelanggan(db)
        elif pilih_menu1 == "4":
            Subquery_pelanggan(db)
        elif pilih_menu1 == "5":
            pass
        else:
            print("You inputed the wrong menu, please try again")
            
    elif pilih_menu == "3":
        print('\n--- MENU ---')
        print('1. Menampilkan data')
        print('2. Menampilkan data pegawai dengan id tertentu')
        print('3. Keluar')
        pilih_menu1 = input("Pilih aksi : ")
        if pilih_menu1 == "1":
            Show_pegawai(db)
        elif pilih_menu1 == "2":
            Subquery_pegawai(db)
        elif pilih_menu1 == "3":
            pass
        else:
            print("You inputed the wrong menu, please try again")
    
    elif pilih_menu == "4":
        print('\n--- MENU ---')
        print('1. Menambah data')
        print('2. Menghapus data')
        print('3. Menampilkan data distributor dengan id tertentu')
        print('4. Keluar')
        pilih_menu1 = input("Pilih aksi : ")
        if pilih_menu1 == "1":
            Nambah_data_distributor(db)
        elif pilih_menu1 == "2":
            Delete_data_distributor(db)
        elif pilih_menu1 == "3":
            Subquery_distributor(db)
        elif pilih_menu1 == "4":
            pass
        else:
            print("You inputed the wrong menu, please try again")
    
    elif pilih_menu == "5":
        print('\n--- MENU ---')
        print('1. Menambah data')
        print('2. Mengupdate data')
        print('3. Menghapus data')        
        print('4. Menampilkan data penulis dengan id tertentu')
        print('5. Keluar')
        pilih_menu1 = input("Pilih aksi : ")
        if pilih_menu1 == "1":
            Nambah_data_penulis(db)
        elif pilih_menu1 == "2":
            Update_data_penulis(db)
        elif pilih_menu1 == "3":
            Delete_data_penulis(db)
        elif pilih_menu1 == "4":
            Subquery_penulis(db)
        elif pilih_menu1 == "5":
            pass
        else:
            print("You inputed the wrong menu, please try again")
    
    elif pilih_menu == "6":
        print('\n--- MENU ---')
        print('1. Menampilkan data dari kombinasi tabel majalah dan distributor')
        print('2. Menampilkan data dari kombinasi tabel majalah dan penulis')
        print('3. Menampilkan data dari kombinasi tabel pelanggan dan majalah')
        print('4. Menampilkan data dari kombinasi tabel majalah, penulis, dan distributor')
        print('5. Keluar')
        pilih_menu1 = input("Pilih aksi : ")
        if pilih_menu1 == "1":
            Majalah_distributor(db)
        elif pilih_menu1 == "2":
            Majalah_penulis(db)
        elif pilih_menu1 == "3":
            Pelanggan_majalah(db)
        elif pilih_menu1 == "4":
            print('\n--- MENU ---')
            print('1. Menampilkan detail data distributor')
            print('2. Menampilkan detail data penulis')
            print('3. Keluar')
            pilih_menu2 = input("Pilih aksi : ")
            if pilih_menu2 == "1":
                Majalah_distributor_penulis(db)
            elif pilih_menu2 == "2":
                Majalah_penulis_distributor(db)
            elif pilih_menu2 == "3":
                pass
            else :
               print("You inputed the wrong menu, please try again") 
        elif pilih_menu1 == "5":
            pass
        else:
            print("You inputed the wrong menu, please try again")
    
    elif pilih_menu == "7":
        exit()
    else:
        print("You inputed the wrong menu, please try again")

while(True):
	Menu(db)