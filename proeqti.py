# წიგნების მართვის კონსოლ აპლიკაცია.
#  პირველ რიგში შევქმენი csv ფაილი,რომელსაც გამოვიყენებ წიგნების მართვის კონსოლ აპლიკაციისთვის, ფუნქციის საშუალებით შედის წიგნების სია და ის ფაილი სადაც უნდა ჩაიწეროს.
# ფუნქციაში გავწერე დიქშენარის ქიები, შევქმენი csv ფაილი სადაც უნდა ჩაწერილიყო ქიების მიხედვით მონაცემები.
#for ციკლის საშუალებით გავირბენ წიგნების სიაში და ჩავწერ csv ფაილში.



import csv
def input_book_list(books, csv_file):
   
    headers = ['Title', 'Author', 'Publication Year']
    
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        
        
        writer.writeheader()
        
        
        for book in books:
            writer.writerow(book)
books=[ {'Title': 'Mgzavris werilebi', 'Author': 'Ilia chavchavadze', 'Publication Year': 1861},
    {'Title': 'Didostatis marjvena', 'Author': 'Konstantine Gamsakhurdia', 'Publication Year': 1947, },
    {'Title': 'Gmirta varami', 'Author': 'Levan Gotua', 'Publication Year': 1958}
]



csv_file = 'book_list.csv'
input_book_list(books, csv_file)

# შევქმენი კლასი რომელიც საჭიროებს, რომ გადავცე სათაური, ავტორი და წელი.
class Book:
    def __init__(self, title, author, year):
        self.title=title
        self.author=author
        self.year=year
        
# შევქმენი კლასი სადაც შექმნილ csv ფაილს გამოვიყენებ. იმისთვის, რომ დავამატო ახალი წიგნი ფაილს გავხსნი იმისთვის, რომ ჩავწერო ახალი წიგნი.
# მეორე ფუნქციით ფაილიდან ამოვიღებ მთლიან მონაცემებს და მთლიან სიას ვაჩვენებ კონსოლში. თუ სია ცარიელი იქნება გამოიტანს რომ ფაილი ცარიელია, თუ მასში იქნება მონაცემები for ციკლით გაირბენს, გადანომრავს და გამოიტანს მონაცემებს.
# მესამე ფუნქცია კვლავ გახსნის ფაილს და გაირბენს სიაში და სათაურის მიხედვით მოძებნის წიგნს და დაბეჭდავს მის ავტორს და გამოქვეყნების წელს.
class BookManager:
    def add(self,book):
        with open("book_list.csv", "a", newline='') as file:
            self.book_list=csv.writer(file)
            self.book_list.writerow([book.title, book.author, book.year])

    def show_books(self):
        with open("book_list.csv", "r", newline='') as file:
            self.book_list=csv.reader(file)
            books=list(self.book_list)

        if not self.book_list:
            print("No books in the list")
        else:
            for i,book in enumerate(books,0):
                print(f"{i} {book}")

    def search_book(self, title):
        with open("book_list.csv", "r", newline='') as file:
            self.book_list=csv.reader(file)
            books=list(self.book_list)

            for book in books:
                if book[0].lower()==title.lower():
                    print(book)
            return 
        
#შემოდის მომხმარებელი რომელიც ინფუთის საშვალებით ამატებს წიგნს სიაში. 
class user:
    def __init__(self,name, book_manager):
        self.name=name
        self.book_manager = book_manager

    def add_book(self):
    
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = input("Enter the publication year of the book: ")
        book = Book(title, author, year)
        self.book_manager.add(book)
        print("Book added successfully!")


    def show_books(self):
        self.book_manager.show_books()

    def search_books(self):
        title = input("Enter the title of the book: ")
        self.book_manager.search_book(title)

def main():
    
    book_manager=BookManager()
    user_name=input("Enter your name: ")
    user1=user(user_name, book_manager)

    while True:
        print("\n1. Add a book")
        print("2. Show all books")
        print("3. Search for a book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice=="1":
            user1.add_book()
        elif choice=="2":
            user1.show_books()
        elif choice=="3":
            user1.search_books()
        elif choice=="4":
            print("you exiting program.")
            break
        else:
            print("you enterd ancorect number, pleas try again.")


if __name__ == "__main__":
    main()



u=Book("Franit morbenali", "khalil khoseini", 2016)
w=Book("davitiani", "davit guramishvili", 1787)
book_manager = BookManager()

#book_manager.add(u)
#book_manager.show_books()
#book_manager.search_book("didostatis marjvena")















