def main():
    option = True
    while True:
        print("Encode Decode Menu")
        print("-"*18)
        print("1. Encode \n 2. Decode \n 3. Exit")
        choice = int(input("Select an option:"))

        if choice == 1:
            password = input("Type string of numbers to encode: ")
            encoder = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == 2:
            decoder = decode(encoder)
            print(f"The encoded password is is {encoder}, and the original password is {decoder}.")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again")
def encode(password):
    encoder = ""
    for i in password:
        password_encode = int(i)
        password_encode += 3
        password_encode %= 10
        encoder += str(password_encode)
    return encoder

def decode(password_string):   # brenda added decode function
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
