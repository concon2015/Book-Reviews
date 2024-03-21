current_users = 'Connor', 'Admin', 'rUdder', 'ellIe', 'keNnedy'
new_users = 'connor' , 'keith', 'ana', 'ellie', 'ben'

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() not in current_users_lower:
        print(f"Username {new_user} accepted")
    else:
        print(f'Username {new_user} already in use. Please select another username')