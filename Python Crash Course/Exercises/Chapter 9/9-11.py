from users import Admin

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'hunter2')

eric.privileges.privileges = ['delete', 'edit', 'create']
eric.privileges.show_privileges()