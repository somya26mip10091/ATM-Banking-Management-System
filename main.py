# ============================================================
# ATM BANKING MANAGEMENT SYSTEM

accounts = {}


# CREATE NEW ACCOUNT

def create_account():

    print("\n................................")
    print("CREATE NEW ACCOUNT")
    print("...............................")

    name = input("Enter your name: ")

    account_number = input("Create account number: ")

    # Check whether account already exists
    if account_number in accounts:
        print("Account number already exists.")
        return

    # Account number validation
    if not account_number.isdigit():
        print("Account number must contain numbers only.")
        return

    pin = input("Create a 4-digit PIN: ")

    # PIN validation
    if len(pin) != 4 or not pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return

    initial_balance = float( input("Enter initial deposit: ₹") )

    if initial_balance < 0:
        print("Invalid initial balance.")
        return

    # Create account
    accounts[account_number] = {"name": name, "pin": pin,"balance": initial_balance,"transactions": []}

    # Add initial deposit to transaction history
    if initial_balance > 0:
        accounts[account_number]["transactions"].append( ("Initial Deposit", initial_balance))

    print("\nAccount created successfully!")
    print("Account Holder :", name)
    print("Account Number :", account_number)
    print("Balance  :₹", initial_balance)  


# CHECK BALANCE  


def check_balance(account):

    print("/n..................................")
    print("          CHECK BALANCE")
    print("..................................")

    print("Account Holder :", account["name"])
    print("Available Balance : ₹", account["balance"])


# ACCOUNT DETAILS


def account_details(account, account_number):

    print("\n................................")
    print("         ACCOUNT DETAILS")
    print("...............................")

    print("Account Number :", account_number)
    print("Account Holder :", account["name"])
    print("Current Balance: ₹", account["balance"])
    print("Total Transactions:",
          len(account["transactions"]))



def deposit(account):

    print("\n................................")
    print("          DEPOSIT MONEY")
    print("..................................")

    amount = float(input("Enter amount to deposit: ₹"))

    if amount <= 0:

        print("Invalid amount.")

    else:

        account["balance"] += amount

        account["transactions"].append(("Deposit", amount))

        print("\nAmount deposited successfully!")
        print("Deposited Amount : ₹", amount)
        print("New Balance      : ₹", account["balance"])


# WITHDRAW MONEY


def withdraw(account):

    print("\n...............................")
    print("         WITHDRAW MONEY")
    print("................................")

    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:

        print("Invalid amount.")

    elif amount > account["balance"]:

        print("Insufficient balance.")

    else:

        account["balance"] -= amount

        account["transactions"].append( ("Withdrawal", amount) )

        print("\nPlease collect your cash.")
        print("Withdrawn Amount : ₹", amount)
        print("Remaining Balance: ₹", account["balance"])



# MONEY TRANSFER


def transfer(account, account_number):

    print("\n...............................")
    print("          MONEY TRANSFER")
    print("....................................")

    receiver_number = input( "Enter receiver account number: ")

    if receiver_number not in accounts:

        print("Receiver account does not exist.")
        return

    if receiver_number == account_number:

        print("You cannot transfer money to yourself.")
        return

    amount = float( input("Enter amount to transfer: ₹") )

    if amount <= 0:

        print("Invalid amount.")

    elif amount > account["balance"]:

        print("Insufficient balance.")

    else:

        receiver = accounts[receiver_number]

        account["balance"] -= amount
        receiver["balance"] += amount

        account["transactions"].append( ("Transfer to " + receiver["name"], amount) )

        receiver["transactions"].append(("Received from " + account["name"], amount))

        print("\nTransfer successful!")
        print("Transferred Amount : ₹", amount)
        print("Receiver           :", receiver["name"])
        print("Remaining Balance  : ₹", account["balance"])


# TRANSACTION HISTORY


def transaction_history(account):

    print("\n................................")
    print("       TRANSACTION HISTORY")
    print("................................")

    if len(account["transactions"]) == 0:

        print("No transactions available.")

    else:

        number = 1

        for transaction in account["transactions"]:

            print(number, ".", transaction[0], "₹", transaction[1] )

            number += 1



# SEARCH TRANSACTION


def search_transaction(account):

    print("\n.................................")
    print("       SEARCH TRANSACTION")
    print("......................................")

    keyword = input("Enter transaction type: " ).lower()

    found = False

    for transaction in account["transactions"]:

        if keyword in transaction[0].lower():

            print(transaction[0],"₹",transaction[1] )

            found = True

    if found == False:

        print("No matching transaction found.")

# SORT TRANSACTIONS


def sort_transactions(account):

    print("\n...............................")
    print("        SORT TRANSACTIONS")
    print("...................................")

    if len(account["transactions"]) == 0:

        print("No transactions available.")
        return

    sorted_transactions = sorted(account["transactions"], key=lambda x: x[1] )

    print("\nTransactions from lowest to highest:")

    for transaction in sorted_transactions:

        print( transaction[0], "₹", transaction[1] )



# MINI STATEMENT


def mini_statement(account):

    print("\n=................................")
    print("          MINI STATEMENT")
    print("..................................")

    print("Account Holder :", account["name"])
    print("Current Balance: ₹", account["balance"])

    print("\nLast Transactions:")

    if len(account["transactions"]) == 0:

        print("No transactions available.")

    else:

        last_transactions = account["transactions"][-5:]

        for transaction in last_transactions:

            print( transaction[0], "₹", transaction[1] )



# CHANGE PIN


def change_pin(account):

    print("\n...............................")
    print("             CHANGE PIN")
    print("...................................")

    old_pin = input("Enter current PIN: ")

    if old_pin != account["pin"]:

        print("Incorrect current PIN.")
        return

    new_pin = input("Enter new 4-digit PIN: ")

    if len(new_pin) == 4 and new_pin.isdigit():

        account["pin"] = new_pin

        print("PIN changed successfully.")

    else:

        print("PIN must contain exactly 4 digits.")


# ATM MENU


def atm_menu(account, account_number):

    while True:

        print("\n...............................................")
        print("             ATM BANKING SYSTEM")
        print("...................................................")

        print("Welcome,", account["name"])

        print("......................................")
        print("1.  Check Balance")
        print("2.  Account Details")
        print("3.  Deposit Money")
        print("4.  Withdraw Money")
        print("5.  Transfer Money")
        print("6.  Transaction History")
        print("7.  Search Transaction")
        print("8.  Sort Transactions")
        print("9.  Mini Statement")
        print("10. Change PIN")
        print("11. Logout")
        print(".....................................")

        choice = input("Enter your choice: ")

        if choice == "1":

            check_balance(account)

        elif choice == "2":

            account_details( account, account_number )

        elif choice == "3":

            deposit(account)

        elif choice == "4":

            withdraw(account)

        elif choice == "5":

            transfer( account,account_number)

        elif choice == "6":

            transaction_history(account)

        elif choice == "7":

            search_transaction(account)

        elif choice == "8":

            sort_transactions(account)

        elif choice == "9":

            mini_statement(account)

        elif choice == "10":

            change_pin(account)

        elif choice == "11":

            print("\nYou have been logged out.")
            print("Please collect your card.")
            break

        else:

            print("\nInvalid choice.")
            print("Please enter a valid option.")



# MAIN PROGRAM


while True:

    print("\n")
    print("==============================================")
    print("          WELCOME TO ATM BANKING")
    print("==============================================")

    print("1. Create New Account")
    print("2. Login")
    print("3. Exit")

    print("----------------------------------------------")

    main_choice = input("Enter your choice: ")


    
    # CREATE ACCOUNT
    

    if main_choice == "1":

        create_account()



    # LOGIN

    elif main_choice == "2":

        if len(accounts) == 0:

            print("\nNo accounts available.")
            print("Please create an account first.")

        else:

            attempts = 3
            login_successful = False

            while attempts > 0:

                print("\n----------- LOGIN -----------")

                account_number = input("Enter Account Number: ")

                pin = input( "Enter 4-digit PIN: " )

                if account_number in accounts:

                    account = accounts[account_number]

                    if account["pin"] == pin:

                        print("\nLogin successful!")
                        print("Welcome", account["name"])

                        login_successful = True

                        atm_menu(account,account_number)

                        break

                    else:

                        attempts -= 1

                        print("\nIncorrect PIN.")
                        print("Attempts remaining:", attempts)
                        

                else:

                    attempts -= 1

                    print("\nAccount not found.")
                    print ("Attempts remaining:",
                        attempts)
                    

            if login_successful == False:

                print("\n..............................")
                print("          ACCESS DENIED")
                print("..................................")

                print("Too many incorrect attempts.")


    
    # EXIT
    

    elif main_choice == "3":

        print("\n================================")
        print("       THANK YOU FOR USING")
        print("          ATM BANKING SYSTEM")
        print("================================")

        break


    
    # INVALID CHOICE
    

    else:

        print("\nInvalid choice.")
        print("Please select 1, 2 or 3.")