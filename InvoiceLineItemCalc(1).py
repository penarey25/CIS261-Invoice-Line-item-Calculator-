#!/usr/bin/env python3
def get_price():
    """Get and validate a price from user input"""
# TODO: Implement price input validation
    while True: 
        try: 
            price_input = input("Enter price: ").replace(",", ".")
            price = float(price_input)
            if price < 0: 
                print("Price cannot be negative. Please enter a valid price/")
            else: 
                return price
        except ValueError:
            print("Invalid decimal number. Please try again.")
            pass

def get_quantity():
    """Get and validate a quantity from user input"""
# TODO: Implement quantity input validation
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 1:
                print("Quantity must be at least 1. Please enter a valid quantity.")
            else:
                return quantity
        except ValueError:
            print("Invalid integer. Please try again.") # Should return a valid integer quantity
        pass

def main():
    print("The Invoice Line Item Calculator\n")
# TODO: Implement main program loop
    while True:
        price = get_price()
        quantity = get_quantity()
        total = price * quantity 
        print(f"TOTAL: ${total:.2f}\n")

        another = input("Enter another line item? (y/n): ").strip().lower()
        if another != 'y':
            break

    print("Bye!")

if __name__ == "__main__":
    main()