class User:
    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
    def describe_user(self):
        print(f'This is a summary for {self.first_name} {self.last_name}!')
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Email: {self.email}')
        print(f'Username: {self.username}')
        print(f'Password: {self.password}')
    def greet_user(self):
        print(f'Hello {self.username}!')
