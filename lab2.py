from item import Item
from receipt import Receipt
flag = "yes"
totalPrice = 0
rate = 0.07
r1 = Receipt(rate)
tax = 0
print("Welcome to the receipt creator")
while(flag == "yes"):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    taxable = input("Is the item taxable (yes/no): ")
    if(taxable == "yes"):
        __taxable = True
        
    else:
        __taxable = False
    
    i1= Item(name, price, __taxable)
    r1.addItem(i1)
    flag = input("Add another item (yes/no):")
    totalPrice = price + totalPrice
print(r1)
for i in range(0, len(r1._Receipt__purchases)):
    print(r1._Receipt__purchases[i])
for i in range(0, len(r1._Receipt__purchases)):
    if(r1._Receipt__purchases[i]._Item__taxable == True):
        tax = tax + (r1._Receipt__purchases[i]._Item__price * rate)
subTotal = tax + totalPrice

print()
print("Sub Total________________________{:.2f}".format(totalPrice))
print("Tax______________________________{:.2f}".format(tax))
print("Total____________________________{:.2f}".format(subTotal))
