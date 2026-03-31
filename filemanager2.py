import os

def check_file_exists():
    filename = input("Enter file name: ")
    if os.path.exists(filename):
        print('File exists')
    else:
        print('File does not exist')

def delete_file():
    filename = input('Enter file name: ')
    if os.path.exists(filename):
        os.remove(filename)
        print('File deleted successfully')
    else:
        print('File is not found')

def rename_file():
    old_name = input('Enter the current name of your file: ')
    if os.path.exists(old_name):
        new_name = input('Enter the new file name: ')
        os.rename(old_name, new_name)
        print('File renamed successfully')
    else:
        print('File is not found')

def copy_file():
    source = input('Enter sorce file name: ')
    if os.path.exists(source):
        destination = input("Enter destination file name: ")
        with open(source, 'r') as src:
            content = src.read()
        with open (destination, 'w') as dest:
             dest.write(content)
        print('File copied successfully')
    else:
        print('Source file not found')

def file_size():
    filename = input('Enter file name: ')
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print('File size:', size, 'bytes')  
    else:
        print('File not found')

def search_word():
    filename = input('Enter file name: ')
    if os.path.exists(filename):
        word = input('Enter word to search: ')
        with open(filename, 'r') as file:
            content = file.read()
            count = content.lower().count(word.lower())
            print('Word found', count, 'times')
    else:
        print('File not found')

def merge_files():
    file1 = input('Enter first file name: ')
    file2 = input('Enter second file name:')

    try:
        with open(file1, 'r') as f1:
            content1 = f1.read()
        
        with open(file2, 'r') as f2:
            content2 = f2.read()

        new_file = input('Enter new file name to store merged content: ')

        with open(new_file, 'w') as  nf:
            nf.write(content1 + '\n' + content2)

        print('File merged successfully')

    except FileNotFoundError:
        print('One or both files not found')

def menu():
    while True:
        print('\n--- Advanced File Manager ---')
        print('1. Check File Exists')
        print('2. Delete File')
        print('3. Rename File')
        print('4. Copy File')
        print('5. File size')
        print('6. Search Word')
        print('7. Merge Two Files')
        print('8. Exit')

        choice = input('Enter your choice: ')
        
        if choice == '1':
            check_file_exists()
        elif choice == '2':
            delete_file()
        elif choice == '3':
            rename_file()
        elif choice == '4':
            copy_file()
        elif choice == '5':
            file_size()
        elif choice == '6':
            search_word()
        elif choice == '7':
            merge_files()
        elif choice == '8':
            print('Exiting program')
            break
        else:
            print('Invaild choice')

menu()