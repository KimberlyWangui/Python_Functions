def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_price = price * (discount_percentage / 100)
        final_price = price - discount_price
    else:
        final_price = price
    return final_price

price_input = float(input("Enter the price of the item: "))
discount_input = float(input("Enter the discount percentage: "))

final = calculate_discount(price_input, discount_input)
    
if discount_input >= 20:
    print(f"The final price after discount is: {final}")
else:
    print(f"No discount applied. The final price is: {final}")