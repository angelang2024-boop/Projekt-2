from datetime import datetime 
from storage import load_data, save_data

# Transaktion hinzufügen
def add_transaction(t_type, amount, category):
    data = load_data()

    transaction = {
        "type": t_type, 
        "amount": amount,
        "category": category, 
        "date": str(datetime.now().date())
    }

    data.append(transaction)
    save_data(data)

# Kontostand berechnen
def get_balance():
    data = load_data()

    income = sum(t["amount"] for t in data if t["type"] == "income")
    expense = sum(t["amount"] for t in data if t["type"] == "expense")

    return income - expense

# Transaktionen anzeigen
def list_transactions(): 
    return load_data()

# Transaktion löschen 
def delete_transaction(index):
    data = load_data()

    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)
        return True 
    return False
