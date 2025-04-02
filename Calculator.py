def calculate_discount(price, discount_percent):
    """
    Calculates the final price in KES after applying a discount (if 20% or higher).
    
    Args:
        price (float): Original price in KES
        discount_percent (float): Discount percentage (0-100)
        
    Returns:
        float: Final price in KES after discount (or original price if discount < 20%)
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# Get user input in KES
try:
    original_price = float(input("Enter the original price of the item (KES): "))
    discount = float(input("Enter the discount percentage (0-100): "))
    
    # Validate inputs
    if original_price < 0 or discount < 0 or discount > 100:
        print("❌ Invalid input: Price must be positive and discount must be 0-100%.")
    else:
        final_price = calculate_discount(original_price, discount)
        
        if discount >= 20:
            print(f"✅ Discount applied! Final price: KES {final_price:,.2f}")
        else:
            print(f"ℹ️ No discount applied (minimum 20% required). Original price: KES {original_price:,.2f}")

except ValueError:
    print("❌ Error: Please enter a valid number for price and discount.")