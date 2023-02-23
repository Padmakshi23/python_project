from e_commerce_project.item_module import Item_package

item1=Item_package()
item2=Item_package()
item3= Item_package()

item1.item_id= 1
item1.item_descr="sugar"
item1.item_quanity= 2
item1.item_price= 7000

item2.item_id= 2
item2.item_descr="tea"
item2.item_quanity= 4
item2.item_price= 1000

item3.item_id= 3
item3.item_descr="cofee"
item3.item_quanity= 6
item3.item_price= 3000

print(item1.item_descr)
print(item2.item_descr)
print(item3.item_descr)

item1.discounted_price()
item2.discounted_price()
item3.discounted_price()
