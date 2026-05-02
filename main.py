import asyncio

# Fake database
books = [
    {"id": 1, "title": "Things Fall Apart", "available": True},
    {"id": 2, "title": "Half of a Yellow Sun", "available": True}
]

borrowed_books = []


# GET /books
def get_books():
    print("\nAvailable Books:")
    for book in books:
        print(book)


# POST /borrow
async def borrow_book(user, book_id):
    for book in books:
        if book["id"] == book_id and book["available"]:
            print(f"{user} is borrowing book {book_id}...")
            await asyncio.sleep(2)  # simulate delay
            book["available"] = False
            borrowed_books.append({"user": user, "book_id": book_id})
            print(f"{user} successfully borrowed book {book_id}")
            return
    print(f"{user} failed to borrow book {book_id}")


# POST /return
async def return_book(book_id):
    for book in books:
        if book["id"] == book_id:
            print(f"Returning book {book_id}...")
            await asyncio.sleep(2)
            book["available"] = True
            print("Book returned successfully")
            return
    print("Book not found")


# GET /overdue
def overdue_books():
    print("\nOverdue Books:")
    overdue = [{"book_id": 1, "user": "Joel", "days_overdue": 3}]
    for item in overdue:
        print(item)


# MAIN FUNCTION (simulate multiple users)
async def main():
    get_books()

    print("\n--- Borrowing Books (Multiple Users) ---")
    await asyncio.gather(
        borrow_book("Joel", 1),
        borrow_book("Mary", 2)
    )

    get_books()

    print("\n--- Returning Book ---")
    await return_book(1)

    get_books()

    overdue_books()


# RUN PROGRAM
asyncio.run(main())