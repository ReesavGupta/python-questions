books = []
def add_books(book: str):
    books.append(book)
    print("book has been added into the inventory")


def search_book(book: str):
    if book in books : 
        print("your desired book is here : ", book)
    else:
        print(f"{book} not found")


def display_inventory():
    map(print , books)
    for book in books:
        print(book)


if __name__ == "__main__":
    while 1:
        print("""
1. add book
2. search book
3. display inventory
4. exit""")
        option = input("enter your desired operation (1, 2, 3, 4): ")
        if option == "1":
            book_name = input("enter your book name: ")
            add_books(book_name)
        elif option == "2":
            book_name = input("enter your book name: ")
            search_book(book_name)
        elif option == "3":
            display_inventory()
        elif option == "4":
            print("exiting ...")
            break
        else: 
            print("invalid operation`")