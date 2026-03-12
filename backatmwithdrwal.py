import random

# Custom exceptions — professional style
class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class DailyLimitError(Exception):
    pass

DAILY_LIMIT = 10000  # constant — use CAPS for constants in Python

def account_creation():
    try:
        print("\n💳 Welcome to Puneeth Bank!")
        name = input("Enter your name: ").strip()  # .strip() removes extra spaces
        
        if not name:                               # edge case — empty name!
            raise ValueError("Name cannot be empty")
        
        account_number = random.randint(100000, 999999)
        bank_balance = 0.0
        
        print(f"Account created for: {name}")
        print(f"   Account Number     : {account_number}")
        print(f"   Initial Balance    : ₹{bank_balance:.2f}")
        
        return name, account_number, bank_balance  # return everything!
    
    except ValueError as e:
        print(f"Account creation failed: {e}")
        return None, None, 0.0
    finally:
        print("--- account creation attempt complete ---")


def amount_deposit(bank_balance):
    try:
        raw = input("Enter amount to deposit: ").strip()
        amount = float(raw)                        # let THIS raise ValueError
        
        if amount <= 0:                            # negative deposit check!
            raise InvalidAmountError("Deposit amount must be positive")
        
        bank_balance += amount
        print(f"Deposited          : ₹{amount:.2f}")
        print(f"   Updated Balance    : ₹{bank_balance:.2f}")
    
    except ValueError:
        print(" Invalid input — please enter a number")
    except InvalidAmountError as e:
        print(f" {e}")
    finally:
        print("--- deposit attempt complete ---")
    
    return bank_balance                            # always return balance


def amount_withdrawal(bank_balance):
    try:
        raw = input("Enter amount to withdraw: ").strip()
        amount = float(raw)                        # type check first
        
        if amount <= 0:                            # must be positive
            raise InvalidAmountError("Withdrawal amount must be positive")
        if amount > DAILY_LIMIT:                   # daily limit check
            raise DailyLimitError(f"Cannot withdraw more than ₹{DAILY_LIMIT:,} at once")
        if amount > bank_balance:                  # funds check
            raise InsufficientFundsError(
                f"Insufficient funds. Balance: ₹{bank_balance:.2f}, "
                f"Requested: ₹{amount:.2f}"
            )
        
        bank_balance -= amount                     # actually deduct it!
        print(f" Withdrawn          : ₹{amount:.2f}")
        print(f"   Updated Balance    : ₹{bank_balance:.2f}")
    
    except ValueError:
        print(" Invalid input — please enter a number")
    except InvalidAmountError as e:
        print(f" {e}")
    except DailyLimitError as e:
        print(f" Daily Limit: {e}")
    except InsufficientFundsError as e:
        print(f"{e}")
    finally:
        print("--- withdrawal attempt complete ---")
    
    return bank_balance                            #  return updated balance


def main():
    bank_balance = 0.0
    account_created = False
    
    while True:
        print("\n" + "="*35)
        print("welcome to PUNEETH BANK")
        print("="*35)
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")          #  added missing feature!
        print("5. Exit")
        
        choice = input("\nEnter your choice: ").strip()
        
        match choice:
            case '1':
                name, acc_no, bank_balance = account_creation()
                if name:
                    account_created = True
            case '2':
                if not account_created:    # can't deposit without account!
                    print(" Please create an account first!")
                else:
                    bank_balance = amount_deposit(bank_balance)
            case '3':
                if not account_created:
                    print(" Please create an account first!")
                else:
                    bank_balance = amount_withdrawal(bank_balance)
            case '4':
                if not account_created:
                    print(" No account found!")
                else:
                    print(f"\n Current Balance: ₹{bank_balance:.2f}")
            case '5':
                print("\n Thank you for using Puneeth Bank. Goodbye!")
                break
            case _:
                print(" Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()