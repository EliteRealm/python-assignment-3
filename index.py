def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount
    
    Args:
        price: Original price
        discount_percent: Discount percentage
        
    Returns:
        Final price after discount (if applicable)
    """
    # Only apply discount if it's 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    
    # Otherwise return the original price
    return price


def main():
    try:
        # Prompt user for price and discount percentage
        price = float(input("Enter the original price: $"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Validate inputs
        if price <= 0:
            print("Price must be greater than zero.")
            return
            
        if discount_percent < 0 or discount_percent > 100:
            print("Discount must be between 0 and 100.")
            return
        
        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)
        
        # Display the result
        if discount_percent >= 20:
            discount_amount = price * (discount_percent / 100)
            print(f"Original Price: ${price:.2f}")
            print(f"Discount Applied: {discount_percent}% (-${discount_amount:.2f})")
            print(f"Final Price: ${final_price:.2f}")
        else:
            print(f"Original Price: ${price:.2f}")
            print(f"Final Price: ${price:.2f} (No discount applied)")
            
    except ValueError:
        print("Please enter valid numbers for price and discount.")


if __name__ == "__main__":
    main()

