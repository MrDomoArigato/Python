import os
def PriceCheck(price):
    os.system("cls")
    total_1=0
    total_2=0

    #Loop to iterate through key in dictionary and multiply quantity * price
    for key in cart:
        if key in store:

            total_1=cart.get(key)
            total_2=store.get(key)

            price+= float(total_1)*float(total_2)

    print("Total is equal to: €",price)
def AddItem():
    os.system("cls")
    item=input("What item do you want to add?:")
    price=input("How much does it cost (e.g 1.50) ?:")

    #Make the input capital
    item=item.lower()

    store[item]= float(price)
    print("Successfully added ",item.capitalize()," with the price: ",price)
def AddToCart():
    os.system("cls")
    item = input("What item do you want to add?:")
    quantity=input("How many do you want to add?:")

    item=item.lower()

    if item not in cart:
        if item in store:
            cart[item]=store[item]
            cart[item]=quantity
        else:
            print("Item not in store, did not update your cart")
def DeleteCart():
    os.system("cls")
    item = input("What item do you want to delete?:")
    item = item.lower()

    if item in cart:
        cart.pop(item,None)
    else:
        print("Item not in store, did not update your cart")
def DeleteStore():
    os.system("cls")
    item = input("What item do you want to delete?:")
    item = item.lower()

    if item in store:
        store.pop(item,None)
    else:
        print("Item does not exist in store, did not update store")


#Basic store for user, can add more to it 
store= {'apple': 1.00 , 'milk': 2.00 , 'vaseline': 4.00 , 'banana': 0.50}
#Initialize empty cart for user
cart={}
#Initialize global price variable for user
price = 0.0


while 1:
    print("Choose a menu Option:")
    print("[1] Print the store items and prices")
    print("[2] Add item to store")
    print("[3] Delete item from store")
    print("[4] Add item to cart")
    print("[5] Delete items from cart")
    print("[6] Print cart")
    print("[7] Calculate total amount")
    print("[8] Exit")


    #MENU OPTIONS MENU OPTIONS MENU OPTIONS
    choice= input()
    if choice == '1':
        os.system("cls")
        print(store)
        
    if choice == '2':
        AddItem()

    if choice == '3':
        DeleteStore()
    
    if choice == '4':
        AddToCart()

    if choice == '5':
        DeleteCart()
    
    if choice =='6':
        #Check to see if cart is populated
        if cart.__len__() is not 0:
             print(cart)
        else:
            print("Cart is empty, please put items into your cart first")
    
    if choice =='7':
        PriceCheck(price)

    if choice == '8':
        exit(0)