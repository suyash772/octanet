def authenticate(pin, correct_pin):
    """Authenticate user based on PIN."""
    return pin == correct_pin


def account_balance_inquiry(balance):
    """Display the account balance."""
    print(f"Your current balance is: {balance:.2f}")


def cash_withdrawal(balance, amount):
    """Withdraw amount from balance if sufficient funds are available."""
    if amount <= 0:
        return balance, "Invalid amount."
    if amount > balance:
        return balance, "Insufficient funds."
    balance -= amount
    return balance, f"Withdrew {amount:.2f}"


def cash_deposit(balance, amount):
    """Deposit amount into balance."""
    if amount <= 0:
        return balance, "Invalid amount."
    balance += amount
    return balance, f"Deposited {amount:.2f}"


def main():
    correct_pin = '1234'
    balance = 10000

    # Authenticate user
    entered_pin = input("Enter your PIN: ")
    if not authenticate(entered_pin, correct_pin):
        print("Authentication failed.")
        return

    print("Authentication successful.")

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Logout")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            account_balance_inquiry(balance)
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            balance, message = cash_deposit(balance, amount)
            print(message)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            balance, message = cash_withdrawal(balance, amount)
            print(message)
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
