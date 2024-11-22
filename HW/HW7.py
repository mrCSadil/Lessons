import sqlite3

connect = sqlite3.connect('HW.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS HW (
    age INTEGER NOT NULL,
    only_name VARCHAR(20) NOT NULL
)
''')

connect.commit()

def add_user(only_name, age):
    cursor.execute(
        'INSERT INTO HW(only_name, age) VALUES (?,?)',
        (only_name, age))
    connect.commit()
    print(f"Пользователь {only_name} добавлен")


# add_user("Олег", 35)
# add_user("Егор", 33)
# add_user("Игорь", 32)

Int= int(input("write which row it will be ''it start from 0 "))
int2= int(input("write and choose from name and age.   1 or 2 "))

def print_users(Int, int2):
    cursor.execute('SELECT * FROM HW')
    rows = cursor.fetchall()

    if 0 <= Int < len(rows):
        user = rows[Int]

        if int2 == 1:
            print(f"Name: {user[1]}")
        elif int2 == 2:
            print(f"Age: {user[0]}")
        else:
            print("something went wrong")

    else:
        print("Неверный номер строки.")

print_users(Int, int2)

# def delete_all_users():
#     cursor.execute('DELETE FROM HW')
#     connect.commit()
#     print("All users have been deleted.")