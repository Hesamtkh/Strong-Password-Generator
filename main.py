from password_generator import generate_password
passwords = [generate_password() for i in range(5)]

with open('passwords.txt', 'w') as file1:
    for password in passwords:
        file1.write(f"{password}\n")