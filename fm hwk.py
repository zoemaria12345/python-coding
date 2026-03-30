def create_file():
    filename = input("enter the name of your enchated writing: ")
    with open(filename, 'w') as file:
        content = input('enter the name of your enchated writing: ')
        file.write(content)

def read_file():
    filename = input('enter the name of your enchanted writing: ')
    try:
        with open(filename, 'r') as file:
            print('\nFile Content:\n')
            content = file.read()
            print(content)
    except FileNotFoundError:
        print('your faboulously ghostly text was not found')

def count_words():
    filename = input('enter the name of your enchated writing: ')
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            print('the total number of your gloriously evil words:', len(words))
    except FileNotFoundError:
        print('your faboulously ghostly text was not found')

def count_lines():
    filename = input('enter the name of your enchated writing: ')
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print('the total of your sickly and haunted lines: ', len(lines))
    except FileNotFoundError:
        print('your faboulously ghostly text was not found')

def replace_word():
    filename = input('enter the name of your enchated writing: ')
    try:
        with open(filename, 'r') as file:
            content = file.read()

        old_word = input("the supernatrurally evil word you would like to switch out: ")
        new_word = input("enter the equally evil word you would like to exchange it with: ")

        content = content.replace(old_word, new_word)

        with open(filename, 'w') as file:
            file.write(content)

        print("evil replacment carried out perfectly")

    except FileNotFoundError:
        print('your faboulously ghostly text was not found')

def append_content():
    filename = input('enter the name of your enchated writing: ')
    try:
        with open(filename, 'a') as file:
            content = input('enter the glamourously evil text you would like to add: ')
            file.write('\n' + content)
        print('evil section added')
    except FileNotFoundError:
        print('your faboulously ghostly text was not found')

def menu():
    while True:
        print("\n--- The Whimsy Witch's Magical Text Managing Portal ---")
        print('1. bibity bobity boo a file into existance') 
        print('2. have a file printed before you in magical black letters')
        print('3. magically count the words in your witchy text')
        print('4. brew a potion to count the lines in your glorious text')
        print('5. supernatrurally exchange a toady little word')
        print('6. add a equally mystical section of text')
        print('7. leave the witch lair') 

        choice = input("enter the magically splendid option you have selected: ")

        if choice == '1':
            create_file()
        elif choice == '2':
            read_file()
        elif choice == '3':
            count_words()
        elif choice == '4':
            count_lines()
        elif choice == '5':
            replace_word()
        elif choice == '6':
            append_content()
        elif choice == '7':
            print('leaving the witch lair')
            break
        else:
            print('invalid spell cast')        

menu()