from tracker import add_transaction, get_balance, list_transactions, delete_transaction

def menu():
    print("\n--- Budget Tracker ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Show Transactions")
    print("5. Delete Transaction")
    print("0. Exit")

while True: 
    menu()
    choice = input("Choose: ")
    
    # Einkommen
    if choice == "1":
        amount = float(input("Income amount: "))
        category = input("Category: ")
        add_transaction("income", amount, category)
    
    # Ausgabe
    elif choice == "2":  
        amount = float(input("Expense amount: "))
        category = input("Category: ")
        add_transaction("expense", amount, category)
    
    # Balance
    elif choice == "3":
        print("Balance: ", get_balance())
    
    # Anzeigen
    elif choice == "4":
        for i, t in enumerate(list_transactions()):
            print(f"{i}: {t}")
    
    # Löschen 
    elif choice == "5": 
        index = int(input("Index: "))
        delete_transaction(index)

    # Beenden
    elif choice == "0":
        break