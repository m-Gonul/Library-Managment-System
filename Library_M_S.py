class Library():  
    def __init__(self):
        try:
            # Open The 'Books.txt' File When Class Is Called
            self.file = open("Books.txt","a+")
            print("Hello There!")
            self.menu_template()
        except Exception as err:
            print(f"Error: {err} at Calling Class Stage")

    def list_file(self):
        try:
            # List File Contents
            self.file.seek(0)
            contents = self.file.read().splitlines()
            for content in contents:
                content = content.split(",")
                print("-"*25)
                print(f"Name: {content[0]}\nAuthor: {content[1]}\nFirst Release Year: {content[2]}\nPage Number: {content[3]}")
        except Exception as err:
            print(f"Error: {err} at Listing File Stage")
    
    def add_book(self):
        try:
            # Adds A Book To List
            book_title = input("Title: ")
            book_author = input("Author: ")
            book_fr_year = input("First Release Year(Enter With Numbers): ")
            book_pg_number = input("Page Number(Enter With Numbers): ")
            if isinstance(book_title, str) and isinstance(book_author, str) and book_fr_year.isdigit() and book_pg_number.isdigit():
                self.file.write(f"{book_title},{book_author},{book_fr_year},{book_pg_number}\n")
            else:
                print("Invalid Values Please Try Again")
                self.add_book()
        except Exception as err:
            print(f"Error: {err} at Adding Book Stage")

    def del_book(self):
        try:
            # Deletes A Book From List
            searched_value = input("Please Entry The Book's Name You Want To Delete: ")
            self.file.seek(0)
            contents = self.file.read().splitlines()
            updated_contents = []
            for content in contents:
                content_value = content.split(",")
                if(searched_value.lower() != content_value[0].lower()):
                    updated_contents.append(content)
            self.file.seek(0)
            self.file.truncate()
            for updated_content in updated_contents:
                self.file.write(f"{updated_content}\n")
        except Exception as err:
            print(f"Error: {err} at Deleting Book Stage")
    
    def menu_template(self):
        # Creates Menu Template And
        try:
            functions = ["List File", "Add Book", "Delete Book", "Shut Down"]
            print("***MENU***")
            for i in range(len(functions)):
                print(f"{i+1}) {functions[i]}")
            user_input = input("What Do You Want: ")
            try:
                user_input = user_input.lower()
                if (user_input == "list") or (user_input == "list file") or (user_input == "1"):
                    self.list_file()
                    self.menu_template()
                elif (user_input == "add") or (user_input == "add book") or (user_input == "2"):
                    self.add_book()
                    self.menu_template()
                elif (user_input == "delete") or (user_input == "delete book") or (user_input == "3"):
                    print("Invalid Option")
                    self.menu_template()
                elif (user_input == "quit") or (user_input == "close") or (user_input == "shut down") or (user_input == "4"):
                    print("Good Bye!")
                else:
                    print("Invalid Option")
                    self.menu_template()
            except Exception as err:
                print(f"Error: {err} at Input Info From User Stage")
        except Exception as err:
            print(f"Error: {err} at Menu Stage")
        
    def __del__(self):
        try:
            # Closer The File Link 
            self.file.close()
        except Exception as err:
            print(f"Error: {err} at Closing Class Stage")

lib = Library()