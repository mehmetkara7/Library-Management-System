import tkinter as tk
from tkinter import messagebox, simpledialog

class LibraryGUI:
    def __init__(self, master):
        self.master = master
        master.title("Library Management System")
        master.geometry('350x200')
        master.resizable(False, False)
        master.configure(bg="#492E87")


        self.list_button = tk.Button(master, text="List Books", command=self.list_books, bg="#FC6736", fg="black",
                                     height=2, width=10)
        self.list_button.pack(pady=5)

        # add button
        self.add_button = tk.Button(master, text="Add Book", command=self.add_book, bg="#C6DCBA", fg="black", height=2,
                                    width=10)
        self.add_button.pack(pady=5)

        # remove button
        self.remove_button = tk.Button(master, text="Remove Book", command=self.remove_book, bg="#C68484", fg="black",
                                       height=2, width=10)
        self.remove_button.pack(pady=5)

        # quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit, bg="#E1E2C1")
        self.quit_button.pack(pady=5)

    #Kitapları listeler
    def list_books(self):
        with open("books.txt", "r") as file:
            books = file.readlines()
            if not books:
                messagebox.showinfo("List Books", "No books available.")
                print("Books are could not listed")
            else:
                book_list = "\n".join(books)
                messagebox.showinfo("List Books", book_list)
                print("Books are listed succesfuly")

    #kitap ekler
    def add_book(self):
        book_title = simpledialog.askstring("Add Book", "Enter the title of the book:").title()
        book_author = simpledialog.askstring("Add Book", "Enter the author of the book:").title()
        release_date = simpledialog.askstring("Add Book", "Enter the release date of the book:")
        num_pages = simpledialog.askstring("Add Book", "Enter the number of pages:")
        book_info = f"{book_title}, {book_author}, {release_date}, {num_pages}\n"
        with open("books.txt", "a") as file:
            file.write(book_info)
        messagebox.showinfo("Add Book", "Book added successfully.")
        print("New book added")

    #kitap kaldırır
    def remove_book(self):
        book_title = simpledialog.askstring("Remove Book", "Enter the title of the book you want to remove:").title()
        with open("books.txt", "r") as file:
            books = file.readlines()
        with open("books.txt", "w") as file:
            removed = False
            for book in books:
                if book.split(", ")[0] != book_title:
                    file.write(book)
                else:
                    removed = True
            if removed:
                messagebox.showinfo("Remove Book", "Book removed successfully.")
                print("Book removed successfully.")
            else:
                messagebox.showinfo("Remove Book", "Book not found.")
                print("Book not found.")

root = tk.Tk()
gui = LibraryGUI(root)
root.mainloop()