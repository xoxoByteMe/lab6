
def main():
    print("Encode Decode Menu")
    print("-"*18)
    print("1. Encode \n 2. Decode \n 3. Exit")

def encode():
    
    ...

def decode(password_string):
    password = ""
    for i in password_string:
        password_int = int(i)
        password_int -= 3
        if password_int < 0:
            password_int += 10
        password += str(password_int)
    return password

if __name__ == "__main__":
    main()
