import os

class TextFileManager:
    def __init__(self):
        self.running = True

    def display_menu(self):
            print("\n--- Text File Managment System ---")
            print("1. Open and read a file")
            print("2. Create new file and add text")
            print("3. Edit (overwrite) an existing file")
            print("4. Append text to existing file")
            print("5. Exit menu")

    def open_file(self):
            filename = input("Enter file name: ")
            if not os.path.exists(filename):
                print("File does not exist.")
                return
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
                print("\n--- File Content ---")
                print(content if content else "[File is empty]")

    def create_file(self):
            filename = input("Enter new file name: ")
            if not os.path.exists(filename):
                print("File already exist.")
                return
            text = input("Enter text to write: ")
            with open(filename, "w", encoding="utf-8") as file:
                file.write(text)
                print("File created successfully")

    def edit_file(self):
            filename = input("Enter file name to edit: ")
            if not os.path.exists(filename):
                print("File does not exist.")
                return
            text = input("Enter new text (existing content will be replaced): ")
            with open(filename, "w", encoding="utf-8") as file:
                file.write(text)
                print("File updated successfully")
        
    def append_file(self):
            filename= input("Enter file name to append text: ")
            if not os.path.exists(filename):
                print("File does not exist.")
                return
            text = input("Enter text to append: ")
            with open(filename, "a", encoding="utf-8") as file:
                file.write("\n" + text)
            print("Text appended successfully. ")

    def run(self):
        while self.running:
            self.display_menu()
            choice = input("Select an option(1-5):")
            if choice == "1":
                  self.open_file
            elif choice == "2":
                 self.create_file()
            elif choice == "3":
                 self.edit_file()
            elif choice == "4":
                 self.append_file()
            elif choice == "5":
                 self.running_file()
                 print("Exiting system.")
            else:
                 print("Invalid selection.")

if __name__ == "__main__":
     manager = TextFileManager()
     manager.run()