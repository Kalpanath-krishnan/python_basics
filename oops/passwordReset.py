class User:
    def __init__(self, username):
        self.username = username
        self.password = ""  

    def set_password(self, password):
        self.password = password
        print("Password has been set successfully.")

    def reset_password(self, new_password):
        if self.password=="":
            print("Set a password first")
        else:
            self.password = new_password
            print("Password has been reset successfully.")

    def display_info(self):
        print(f"Username: {self.username}")
        if self.password:
            print(f"Password: {'*' * len(self.password)}")  
        else:
            print("Password is not set.")


username = input("Enter your username: ")
user = User(username)

password = input("Set your password: ")
user.set_password(password)

user.display_info()

new_password = input("Enter a new password to reset: ")
user.reset_password(new_password)

user.display_info()
