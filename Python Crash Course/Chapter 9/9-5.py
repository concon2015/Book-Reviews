class User:
    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.login_attempts = 0
    def describe_user(self):
        print(f'This is a summary for {self.first_name} {self.last_name}!')
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Email: {self.email}')
        print(f'Username: {self.username}')
        print(f'Password: {self.password}')
        print(f'Login Attempts:  {self.login_attempts}')
    def greet_user(self):
        print(f'Hello {self.username}!')
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'hunter2')

eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(eric.login_attempts)
eric.reset_login_attempts()
print(eric.login_attempts)
