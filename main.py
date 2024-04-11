# My name: Federica Amati

def encode_password(password):
    constant_value = 3  # Making sure each digit gets shifted up by 3 numbers
    encoded_password = []  # Creating empty list to store new encoded password
    for digit in password:
        encoded_digit = str((int(digit) + constant_value) % 10)  # Adding 3 to each digit
        encoded_password.append(encoded_digit)
    return ''.join(encoded_password)  # returning the encoded password


def decode_password(encoded_password):
    decode = []
    new_num = 0
    for digit in range(0, len(encoded_password)):
        if int(encoded_password[digit]) <= 2: # if num less than 2 adds back 10 to get ori. digit
           new_num = (10 + int(encoded_password[digit])) - 3
        else:
           new_num = (int(encoded_password[digit]) - 3) # otherwise just sub 3
        decode.append(str(new_num))
    return "".join(decode)


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
            encoded_pwd = encode_password(original_password)
            print("Your password has been encoded and stored!")
        elif opt == '2':  # If user selects opt 2, decode the encoded password
            original_pwd = decode_password(encoded_pwd)
            print(f"The encoded password is {encoded_pwd}, and the original password is {original_pwd}.")
        elif opt == '3':
            break

def main():
    mainmenu()


if __name__ == "__main__":
    main()




