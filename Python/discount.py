"""
You work for a retail store that wants to increase sales on Tuesday
and Wednesday, which are the store's slowest sales days. On Tuesday
and Wednesday, if a customer's subtotal is greater than $50, the
store will discount the customer's purchase by 10%.

The datetime module comes with a weekday() function, which returns the day of the week as an integer (where Monday is 0 and Sunday is 6).
"""
print()
from datetime import datetime
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
# print(day_of_week)
disc_rate = 0.10
sales_tax_rate = 0.06
subtotal = 1000

while subtotal != 0:

    unitprice = float(input('Please enter the unit price: '))
    quantity = float(input('Please enter the quantity: '))
    subtotal = unitprice*quantity
    subtotal_with_discount = subtotal-subtotal*disc_rate

    if subtotal>=50 and (day_of_week==1 or day_of_week==2):
        # print("It's Tuesday or Wednesday")
        salestax = subtotal_with_discount*sales_tax_rate
        print(f"Dicount amount: ${subtotal*disc_rate}")
        print(f"Sales tax amount: ${salestax:.2f}")
        total = subtotal_with_discount+salestax
        print(f"Total: ${total:.2f}")
    elif subtotal<50 and (day_of_week==1 or day_of_week==2):
        # print("It's Tuesday or Wednesday")
        difference = 50-subtotal 
        print(f"You need to purchase ${difference:.2f} more to get the discount")
    else:
        # print("It's another day of the week")
        salestax = subtotal*sales_tax_rate
        print(f"Sales tax amount: ${salestax:.2f}")
        total = subtotal+salestax
        print(f"Total: ${total:.2f}")
