class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username
    
    def check_password(self, password):
        return self.__password == password
    
    def set_password(self, new_password):
        self.__password = new_password
        print("Password has been updated successfully!")

    def welcome_message(self):
        return f"Welcome, {self.__username}!"
    
class AdminUser(User):
    def __init__(self):
        return f"Welcome, Admin{self.get_username()}! Full access granted."
    
class RegularUser(User):
    def __init__(self):
        return f"Hello{self.get_username()}! You are logged in as a regular user."
    
class LoginSystem:
    def __init__(self):
        self.users = {
            "Admin1": AdminUser("admin1", "TheAdministrator123"),
            "jules": RegularUser("julesacct", "ponies4life345"),
            "andrew": RegularUser("theblackcatlover", "2cutekittie!"),
            "amie": RegularUser("Iamamazingness", "Amzingnessintheflesh123")                     
        }
    
    def login(self, username, password):
        user = self.user.get(username)
        if user and user.check_password(password):
            print(user.welcome_message())
            return user
        print("Invalid usrrname or password.")
        return None
    
if __name__ =="__main__":
    system = LoginSystem()

    print("===== User Login System ===")

    u = input("Enter your username: ")
    p = input("Enter your pasword: ")

    system.login(u,p)