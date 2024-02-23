# password manager
import pyperclip as pc


password = {}


def addPassword():
    app = input("Enter the app name: ")
    passw = input("Enter the password: ")
    password[app] = passw


def writefile():
    filepath = input("Enter the path of the file: ").strip()
    with open(filepath, "w") as file:
        for key, value in password.items():
            file.write(f"{key}: {value}\n")
        print("Password written to", filepath)
    file.close()


def display():
    star = list(password.values())
    i = 1
    for key in password:
        print(i, key)
        i = i + 1
    print(i, " Go back")
    ch = int(input("Choose to open the password: "))
    if ch == i:
        return
    for i in range(len(star[ch - 1])):
        print("*", end="")
    print()
    while 1:
        cho = int(input("1 show\n2 copy\n3 go back\n"))
        if cho == 1:
            print(star[ch - 1])
        elif cho == 2:
            pc.copy(star[ch - 1])
            print("Copied to clipboard")
        else:
            print("Going back")
            display()


usernam = input("Enter your user name: ")
if usernam == "admin":
    pas = input("Enter your password: ")
    if pas == "PASSWORD":
        while 1:
            print("----------Main Menu----------")
            print("1. Add password\n2. Display password\n3. Generate a file\n4. Exit")
            c = input("Enter your choice: ")
            if c == '1':
                addPassword()
            elif c == '2':
                display()
            elif c == '3':
                writefile()
            elif c == '4':
                exit()
            else:
                print("Invalid choice\n")

    else:
        print("Incorrect password")
else:
    print("User not found")
