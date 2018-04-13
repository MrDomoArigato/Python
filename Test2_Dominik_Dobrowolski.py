#Written by Dominik Dobrowolski C16347703
#23.11.2017


import pprint
#Store in list
authors=[]
titles=[]
prices=[]
f=open("books.txt","r")

#Split into lines and put into 3 lists
for line in f:
    name=line.split(",")
    titles.append(name[1])
    authors.append(name[2])
    prices.append(name[3])
def save():
    with open("books1.txt","w") as file:
        for i in range(0,len(authors)):
            #line=titles[i],authors[i],prices[i]
            file.write(str(i+1))
            file.write(",")
            file.write(titles[i])
            file.write(",")
            file.write(authors[i])
            file.write(",")
            file.write(prices[i])
            file.write("\n")
def search():
    user=input("What is the exact title of the book?")
    if user in titles:
        print()
        auth=(titles.index(user))
        print("The author is",authors[auth])
    else:
        print(user,"Not found in library")
def book_print():
    print("All the books in the library are: ")
    for i in range(0, len(authors)):
        print(titles[i],"by",authors[i],"it costs:",prices[i])
def check_price():
    total=0
    sum=0
    for i in range(0,len(prices)):
       print(prices[i])
        #total=i.split("\n")
        #print(total)
        #for i in range(0,len(prices)):
        #print(prices[i])
    print("The total for all the books is ",sum)
def add():
    user_title=input("What is the title of the book?")
    user_author=input("Who is the author of the book?")
    user_price=input("What is the price of the book?")
    titles.append(user_title)
    authors.append(user_author)
    prices.append(user_price)
def discount():
    print("10% discount has been applied")

while 1:
    print("----MENU----")
    print("B.) Add a new book ")
    print("C.) Search for author fo book , by title ")
    print("D.) Print all books in library ")
    print("E.) Calculate total price ")
    print("F.) Apply 10% discount ")
    print("G.) Save the list of books to file books1.txt")
    choice=input()
    choice=choice.lower()

    #ADDS THE BOOK TO THE LISTS
    if choice =="b":
        add()
    #Must input it exactly the way it's written
    if choice =="c":
        search()
    #Prints all titles,authors and prices
    if choice =="d":
        book_print()

    if choice =="e":
        check_price()

    if choice=="f":
        discount()

   #Save into a file
    if choice=="g":
        save()