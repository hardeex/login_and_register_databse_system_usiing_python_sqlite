import hashlib

class User:
    def __init__(self, username, first_name, last_name, email, password):
        self.username = input("Enter username")
        self.first_name = input("first_name")
        self.last_name = input("last_name")
        self.email = input("email")
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.is_logged_in = False


def login(self, password):
    if hashlib.sha256(password.encode()).hexdigest() == self.password_hash:
        self.is_logged_in = True
        return True

    else:
        return False
    

def logout(self):
    self.is_logged_in = False

def access_dashboard(self):
    if self.is_logged_in:
        print(f"Welcome to your dashboard, {self.first_name}!")
    else:
        print("You must be logged in to access your dashboard.")


class UserAccountSystem:
    def __init__(self):
        self.users = []

def create_user(self, username, first_name, last_name, email, password):
    new_user = User(username, first_name, last_name, email, password)
    self.users.append(new_user)


def login_user(self, username, password):
    for user in self.users:
        if user.username == username:
            return user.login(password)
        return False

def logout_user(self, username):
    for user in self.users:
        if user.username == username:
            user.logout()
        return True
    return False

def access_dashboard(self, username):
    for user in self.users:
        if user.username == username:
            user.access_dashboard()
            return True
    return False