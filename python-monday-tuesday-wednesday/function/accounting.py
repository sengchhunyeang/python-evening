def transfer():
    # Offer applies to first 5 transactions
    max_transactions = 5
    transaction_count = 0

    while transaction_count < max_transactions:
        print("---------------------------")
        amount_input = input("Amount Transfer: $")

        # Check if user input is valid number
        try:
            amount = float(amount_input)

            # Rule 1: Must be more than $1
            if amount <= 1:
                print(" Transfer amount must be greater than $1.\n")
                continue
            # Rule 2: Charge 10% fee if transfer is over $1000
            if amount > 1000:
                fee = amount * 0.10
                total = amount + fee
                print(f" Transfer Success! A 10% fee (${fee:.2f}) was charged. Total deducted: ${total:.2f}")
            else:
                print(" Transfer Success! No fee charged.")

            transaction_count += 1  # Count only successful transfers
            print(f"Transaction {transaction_count} of {max_transactions} completed.\n")

        except ValueError:
            print(" Invalid input. Please enter a number.\n")

    print(" You’ve completed 5 ABA free offer transactions.")


