"""
COMP.CS.100
Tekijä: Patrick Selin
Opiskelunumero: tuni.fi:
Tehtävä: 6.11
"""
def read_message():
    """
    This function ask user to input messages. Then it appends the
    inputs to a list.

    :param no parameters
    :return: list, List of words
    """

    lst_of_inputs = []

    while True:
        user_string = input()
        if user_string == "":
            break
        lst_of_inputs.append(user_string)

    return lst_of_inputs

def encrypt(char):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  character to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    flag = True

    if not char.isalpha():
        return char

    if char.isupper():
        char = char.lower()
        flag = False

    reg_inx = regular_chars.index(char)
    enc_char = encrypted_chars[reg_inx]

    if flag == True:
        return enc_char
    else:
        return enc_char.upper()

def row_encryption(input_word):
    """
    Encrypts string given. It iterates through the string and
    calls the encrypt()-function to get the encrypted character
    and then it replaces that and returns.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    encrypted_str = ''
    # iterate word and replace with encrypted character
    # using encrypt()-function
    for char in input_word:
        encrypted_str += char.replace(char, encrypt(char), 1)

    return encrypted_str

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    # iterate strings in list, encrypt them and print.
    for i in msg:
        print(row_encryption(i))

if __name__ == "__main__":
    main()