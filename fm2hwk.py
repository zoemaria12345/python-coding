import os

def check_file_exists():
    filename = input("Enter shell name: ")
    if os.path.exists(filename):
        print('Shell exists')
    else:
        print('Shell does not exist')

def delete_file():
    filename = input('Enter shell name: ')
    if os.path.exists(filename):
        os.remove(filename)
        print('Shell left on the beach!')
    else:
        print('Shell is not found')

def rename_file():
    old_name = input('Enter the current name of your file: ')
    if os.path.exists(old_name):
        new_name = input('Enter the new file name: ')
        os.rename(old_name, new_name)
        print('Shell renamed successfully')
    else:
        print('Shell is not found')

def copy_file():
    source = input('Enter original shell name: ')
    if os.path.exists(source):
        destination = input("Enter new shell name: ")
        with open(source, 'r') as src:
            content = src.read()
        with open (destination, 'w') as dest:
             dest.write(content)
        print('Shell found successfully')
    else:
        print('Original shell not found')

def file_size():
    filename = input('Enter file name: ')
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print('Shell size:', size, 'bytes')  
    else:
        print('Shell not found')

def search_word():
    filename = input('Enter shell name: ')
    if os.path.exists(filename):
        word = input('Enter inscription to search: ')
        with open(filename, 'r') as file:
            content = file.read()
            count = content.lower().count(word.lower())
            print('Inscription found', count, 'times')
    else:
        print('Shell not found')

def merge_files():
    file1 = input('Enter the nickname you have given your first shell: ')
    file2 = input('Enter the nickname you have given your second shell:')

    try:
        with open(file1, 'r') as f1:
            content1 = f1.read()
        
        with open(file2, 'r') as f2:
            content2 = f2.read()

        new_file = input('Name your bubblicious necklace!: ')

        with open(new_file, 'w') as  nf:
            nf.write(content1 + '\n' + content2)

        print('Necklace made! How cute xxx')

    except FileNotFoundError:
        print('One or both shells cant be not found')

def menu():
    while True:
        print('\n--- Bubblicious Mermaid Shell Organiser ---')
        print('1. Check If Shell Exists')
        print('2. Leave Shell On The Beach')
        print('3. Give Your Favourite Shell A New Name')
        print('4. Find A Shell That Looks The Same')
        print('5. Check Shell Size')
        print('6. Check Shell Surface For Inscription Word')
        print('7. Make A Shell Necklace With Two Shells')
        print('8. Leave The Mermaid Organising Reef')

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
            print('Leaving The Mermaid Reef')
            break
        else:
            print('Invalid Choice :l ')

menu()