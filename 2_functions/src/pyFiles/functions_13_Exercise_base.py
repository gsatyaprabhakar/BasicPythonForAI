'''
## Exercise: The Chai Bill Calculator

You run a chai stall. Customers order multiple cups of chai, sometimes with add-ons (extra ginger, masala, biscuits). Write a function to calculate their bill.
Your task:
Write a function chai_bill(cups, *addons, **discount) that:

Charges ₹15 per cup of chai
Adds ₹5 for each addon passed via *args (like "ginger", "masala", "biscuit")
Applies a discount only if discount_percent is passed via **kwargs
Returns the final bill amount

Test it with these calls:

print(chai_bill(2))                                              
print(chai_bill(3, "ginger", "masala"))                          
print(chai_bill(4, "biscuit", discount_percent=10))              
print(chai_bill(5, "ginger", "masala", "biscuit", discount_percent=20))

Expected output:

* 30
* 55
* 58.5
* 72.0
'''
# Chai Bill Calculator
def chai_bill(cups, *addons, **discount):
#    print(type(cups))
#    print(type(addons))
#    print(type(discount))
    total_bill = 0
    # Total Cups Charge
    total_bill += cups*15
    # Total AddOns Charge
    if len(addons) > 0:
        total_bill += len(addons)*5
    # Apply Discounts
    if len(discount) > 0:
        total_bill -= total_bill*discount["discount_percent"]/100
    return total_bill

print(chai_bill(2))                                              
print(chai_bill(3, "ginger", "masala"))                          
print(chai_bill(4, "biscuit", discount_percent=10))              
print(chai_bill(5, "ginger", "masala", "biscuit", discount_percent=20))
