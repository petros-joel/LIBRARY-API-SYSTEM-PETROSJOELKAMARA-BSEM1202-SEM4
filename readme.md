 Async Library Management System (Python)

## Overview
This is a simple library management system built using Python. It simulates real-life library operations such as borrowing and returning books using asynchronous programming with `asyncio`. It also demonstrates how multiple users can interact with the system at the same time.

## Features
- View available books
- Borrow books asynchronously
- Return books asynchronously
- Simulate multiple users borrowing at the same time
- Simple overdue books display (sample data)

## How It Works
The system stores books in a simple list inside the program. Each book has an ID, title, and availability status. When a user borrows a book, the system checks if it is available, simulates a short delay, and then marks it as unavailable. Returning a book restores its availability. The system also simulates overdue books using sample data.

## Asynchronous Concept
The project uses Python’s `asyncio` to allow multiple operations to run at the same time. This helps simulate real-world behavior where multiple users can borrow books without waiting for each other to finish.

## How to Run
1. Open the project in VS Code  
2. Make sure Python is installed  
3. Run the main file using:
   python main.py

## Future Improvements
- Add a real database instead of in-memory data
- Build a web API using Flask or FastAPI
- Add user login system
- Track real due dates and fines
- Add search and filter for books

## Author
Joel PK  
Software Engineering Student 🇸🇱
