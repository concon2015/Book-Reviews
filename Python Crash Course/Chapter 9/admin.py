from users import User

class Admin(User):
    def __init__(self, first_name, last_name, username, email, password):
        super().__init__(first_name, last_name, username, email, password)
        self.privileges = Privileges()


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        for priv in self.privileges:
            print(f'- {priv}')