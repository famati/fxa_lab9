# My name: Federica Amati

def encode_password(password):
    constant_value = 3  # Making sure each digit gets shifted up by 3 numbers
    encoded_password = []  # Creating empty list to store new encoded password
    for digit in password:
        encoded_digit = str((int(digit) + constant_value) % 10)  # Adding 3 to each digit
        encoded_password.append(encoded_digit)
    return ''.join(encoded_password)  # returning the encoded password


def decode_password(encoded_password):
    constant_value = 3  # Making sure each digit gets shifted down by 3 numbers
    original_password = []  # Creating empty list to store original password
    for digit in encoded_password:
        original_digit = str((int(digit) - constant_value + 10) % 10)  # Subtract 3 from each digit
        original_password.append(original_digit)
    return ''.join(original_password)  # returning the original password


def mainmenu():
    encoded_password = None  # Dummy Variable for encoded password
    original_password = None  # Dummy Variable for original password

    while True:  # while loop for when opt is 1, 2, 3
        # Printing main menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        opt = input("Please enter an option: ")  # user input variable

        if opt == '1':  # If user selects opt 1, encode the original password
            original_password = input("Please enter your password to encode: ")
            encoded_password = encode_password(original_password)
            print("Your password has been encoded and stored!")
        elif opt == '2':  # If user selects opt 2, decode the encoded password
            if encoded_password is not None and original_password is not None:
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
        elif opt == '3':
            break

def main():
    mainmenu()


if __name__ == "__main__":
    main()




