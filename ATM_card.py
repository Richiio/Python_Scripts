import sqlite3

# Login function
def login():
    print("Kindly login")
    balance = 1000000
    account_number = int(input("Enter your account number: "))
    password = input("Enter your password: ").lower()
    conn = sqlite3.connect("Customers_data.db")
    cur = conn.cursor()
    create_table = "CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, account_number int, password text)"
    cur.execute(create_table)
    conn.commit()
    query = "SELECT account_number, PASSWORD FROM customers WHERE account_number = account_number"
    result = cur.execute(query, (account_number,))
    # cur.execute("SELECT ACCOUNT_NUMBER, PASSWORD FROM  AND password = password Customers WHERE ACCOUNT_NUMBER = ACCOUNT_NUMBER", {'ACCOUNT_NUMBER': account_number})
    if result.fetchone()[1] == account_number:
        print("Login Successful")

        print("1. DEPOSIT\n2. WITHDRAWAL\n3. COMPLAINT")
        user_options = int(input("What would you like to do? ENTER 1, 2 or 3: "))

        if user_options == 1:
            deposit(balance)
        elif user_options == 2:
            withdrawal(balance)
        elif user_options == 3:
            complaint()
        else:
            print("Invalid input. Try again!")
        return customer


    else:
        print("Invalid account number or password")
        user_choice = input("Do you want to try again? Press (y) for YES and (n) for NO: ").lower()
        if user_choice == "y":
            login()
        else:
            exit()

# Register function
def register():
    print("****************REGISTERATION PAGE************")
    first_name = input("Enter your first_name: ").lower()
    last_name = input("Enter your last name: ").lower()
    password = input("Enter your password: ").lower()
    account_number = account_number_generator()

    # database()
    conn = sqlite3.connect('Customers_data.db')

    cursor = conn.cursor()

    # usernamecheck = conn.execute("SELECT COUNT(*) FROM Customers WHERE  FIRST_NAME = :FIRST_NAME", {'FIRST_NAME': first_name})
    # if usernamecheck != 0:
    #     return "Username already exists."
    # login()

    params = (first_name, last_name, password, account_number)
    cursor.execute("INSERT INTO Customers VALUES (?,?,?,?)", params)
    conn.commit()
    print(f"Thanks for signinig up into our bank. Your account number is {account_number}")
    conn.close()
    login()
# Generate account number
def account_number_generator():
    return random.randint(1111111111, 9999999999)
# Generate database
def database():
    conn = sqlite3.connect("Customers_data.db")
    conn.execute("CREATE TABLE Customers (FIRST_NAME         BLOB NOT NULL, LAST_NAME           BLOB NOT NULL,PASSWORD            BLOB NOT NULL,ACCOUNT_NUMBER      INT NOT NULL, BALANCE      INT NOT NULL);")
    conn.commit()
    conn.close()

# withdraw function
def withdrawal(balance):
    amount = int(input("Enter withdrawal amount: "))
    if amount > balance:
        print("Balance insufficient")
        withdrawal(balance)

    else:
        balance =- amount
        print(f"Withrawal successful. #{balance} is your balance")

# deposit
def deposit(balance):
    amount = int(input("Enter deposit amount: "))
    balance += amount
    print(f"Your balance is #{balance}")


# complaint
def complaint():
    complain = input("Please enter your complaints: ")
    print(f"Thanks for your time. Our customer care service will get to you as soon as possible")

from datetime import datetime
import sqlite3
import random

now = datetime.now()

print(f"{now}\n")



def atm():
    print("Welcome to Zuri Banking system! \n")
    user_choice = input("Do you have an account with us? Enter (y) for YES or (n) for NO: ").lower()
    if user_choice == "y":
        login()
    elif user_choice == "n":
        register()
    else:
        print("Invalid operation! Try Again.")


atm()
