from phone import Phone
from item import Item

Item.instantiate_from_csv() 

print(Item.all)

phone1 = Phone("Redmi", 1500, 16, 2)

print(phone1)
print(Phone.all)
print(phone1.calculate_total_price())