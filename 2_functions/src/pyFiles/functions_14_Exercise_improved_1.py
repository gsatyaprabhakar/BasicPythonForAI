'''
## Exercise: The Chai Bill Calculator

You run a chai stall. Customers order multiple cups of chai, sometimes with add-ons
(extra ginger, masala, biscuits). Write a function to calculate their bill.

Task:
Write a function, chai_bill(cups, *addons, **discount), that:
- charges ₹15 per cup of chai
- adds ₹5 for each addon passed via *args
- applies a discount only if discount_percent is passed via **kwargs
- returns the final bill amount

Example calls:
print(chai_bill(2))
print(chai_bill(3, "ginger", "masala"))
print(chai_bill(4, "biscuit", discount_percent=10))
print(chai_bill(5, "ginger", "masala", "biscuit", discount_percent=20))

Expected outputs:
- 30
- 55
- 58.5
- 72.0
'''


def chai_bill(cups, *addons, **discount):
    discount_percent = discount.get("discount_percent", 0)

    subtotal = cups * 15 + len(addons) * 5
    if discount_percent:
        subtotal -= subtotal * (discount_percent / 100)

    return subtotal


print(chai_bill(2))
print(chai_bill(3, "ginger", "masala"))
print(chai_bill(4, "biscuit", discount_percent=10))
print(chai_bill(5, "ginger", "masala", "biscuit", discount_percent=20))
