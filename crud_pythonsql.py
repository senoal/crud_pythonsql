import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "",
    database = "learn_sql"
    )

mycursor = mydb.cursor()


def main():
    a = int(input("""_______________ Aplikasi Database Python
                  1. Masukkan data
                  2. Tampilkan data
                  3. Ubah data
                  4. Hapus data
                  5. Cari data
                  6. Keluar
_______________ Masukkan Pilihan : """))
    if a == 1:
        masukkan()
    elif a == 2:
        tampilkan()
    elif a == 3:
        ubah()
    elif a == 4:
        hapus()
    elif a == 5:
        cari()
    else:
        print("Keluar")


def masukkan():
    fn = input("Your last name : ")
    ln = input("your first name : ")
    ag = int(input("your age : "))
    val = (fn, ln, ag)
    mycursor.execute("""
                      INSERT INTO personil 
                      (lastname, firstname, age)
                      VALUES (%s, %s, %s)
                      """, val)
    mydb.commit()
    main()


def tampilkan():
    mycursor.execute("SELECT * FROM personil")

    myresult = mycursor.fetchall()
    
    for x in myresult:
        print(x)
    main()

def ubah():
    a = input("nama lama : ")
    b = input("ganti nama : ")
    
    sql = "UPDATE personil SET lastname=%s WHERE lastname = %s"
    mycursor.execute(sql,(b,a))
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    main()

def hapus():
    a = input("Masukkan nama : ")
    
    sql = "DELETE FROM personil WHERE lastname = %s or lastname = %s"
    
    mycursor.execute(sql,(a,a))
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    main()

def cari():
    sql = "SELECT * FROM personil WHERE lastname = %s"

    a = input("Tampilkan daftar berdasarkan nama belakang : ")
    adr = (a,)
    
    mycursor.execute(sql, adr)
    
    myresult = mycursor.fetchall()
    
    for b in myresult:
        if a in b:
            print(b)
        else:
            return ("data tidak ada!")
    main()
    

if __name__ == '__main__':
    main()