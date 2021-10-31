# this function removes spaces and new lines for column from right and left
def strip(string):
    return string.strip()

# this function reads database from contacts.txt file
def read_database():
    file = open("C:/Projects/python-algajatele/11_test_of_input_output_arrays_conditionals/contacts.txt", encoding="utf-8")
    rows = []
    for row in file:
        rows.append(list(map(strip, row.split(", "))))
    return rows

# this function writes contacts to file
def write_database(db):
    file = open("C:/Projects/python-algajatele/11_test_of_input_output_arrays_conditionals/contacts.txt", mode="w", encoding="utf-8")
    rows = []
    for row in db: 
        rows.append(", ".join(row))
    file.write("\n".join(rows))
    file.close()

# this function prints all contacts from db that is in memory
def print_out_database(db):
    print("Index \t Name \t\t Phone \t\t Age \t Email")
    for i in range(0, len(db)):
        row = db[i]
        print(i, "\t", row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t")

def add_user():
    name = input("Name: ")
    phone =input("Phone: ")
    age = input("Age: ")
    email = input("Email: ")
    user = "\n" + name + ", " + phone + ", " + age + ", " + email
    f = open("C:/Projects/python-algajatele/11_test_of_input_output_arrays_conditionals/contacts.txt", mode="a", encoding="utf-8")
    f.write(user)
    f.close()

def delete_user():
    db = read_database()
    print_out_database(db)
    index = int(input("enter user to delete ?: "))
    db.pop(index)
    write_database(db)


def print_out_commands():
    print("Commands are:")
    print("1. list users")
    print("2. edit user")
    print("3. add user")
    print("4. delete user")
    print("5. Users avarage age")
    return int(input("What is your command?: "))


def group_avarage_age(db):
    age_sum = 0
    for i in range(0, len(db)):
        row = db[i]
        age_sum = age_sum +int(row[2])
    return age_sum / len(db)
    

def main():
  db = read_database()
  command = print_out_commands()
  if command == 1:
    print_out_database(db)
  elif command == 2:
    print("Edit")
  elif command == 3:
    add_user()
  elif command == 4:
    delete_user()
  elif command == 5:
    print("Avarage age of users: ", group_avarage_age(db))


main()
