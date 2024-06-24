# atm_interface.py

class ATM:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 1000.0  # initial balance

    def authenticate(self):
        if self.card_number == "1234-5678-9012-3456" and self.pin == "1234":
            return True
        else:
            return False

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal successful! New balance: ${self.balance:.2f}"
        else:
            return "Insufficient funds or invalid amount"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit successful! New balance: ${self.balance:.2f}"
        else:
            return "Invalid deposit amount"

    def transfer(self, recipient_card_number, amount):
        if amount > 0 and amount <= self.balance:
            # simulate transfer to another card
            print(f"Transferring ${amount:.2f} to card {recipient_card_number}...")
            self.balance -= amount
            return f"Transfer successful! New balance: ${self.balance:.2f}"
        else:
            return "Insufficient funds or invalid amount"

def main():
    print("Welcome to Advanced ATM Interface!")
    card_number = input("Enter your card number: ")
    pin = input("Enter your PIN: ")

    atm = ATM(card_number, pin)

    if atm.authenticate():
        print("Authentication successful!")
        while True:
            print("\nMenu:")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print(atm.check_balance())
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                print(atm.withdraw(amount))
            elif choice == "3":
                amount = float(input("Enter deposit amount: "))
                print(atm.deposit(amount))
            elif choice == "4":
                recipient_card_number = input("Enter recipient's card number: ")
                amount = float(input("Enter transfer amount: "))
                print(atm.transfer(recipient_card_number, amount))
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again!")
    else:
        print("Authentication failed. Try again!")

if __name__ == "__main__":
    main()