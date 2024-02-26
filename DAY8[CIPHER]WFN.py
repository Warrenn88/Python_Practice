import string
def shift(offset):
    new_message = ''
    alphabet = string.ascii_lowercase
    for letter in user_input:
        letter = letter.lower()
        if letter.isalpha():
            shift_pos = (alphabet.index(letter) + offset) % len(alphabet)
            new_pos = alphabet[shift_pos]
            new_message += new_pos
        elif ' ' or '/t' or '/n' in letter:
            new_message += letter
        elif letter.isnumeric():
            new_message += letter
        else:
            print("An error took place in recording the message. Check input.\n")
    return new_message

while True:
    user_input = input("Welcome to Warren's cypher.\nType 'encode' to encrypt, type 'decode' to decrypt")
    if user_input.lower() == "encode":
        user_input = input("Type your message here: ")
        shift_number1 = int(input("Type your shift number: "))
        print(shift(shift_number1))
        yes_no1 = input("Type 'yes' if you want to go again. Otherwise type 'no'")
        if yes_no1.lower() == "no":
            print("Thanks for using my cipher!")
            break

    elif user_input.lower() == "decode":
        user_input = input("Type your message: ")
        shift_number1 = -1*(int(input("Type your shift number: ")))
        print(shift(shift_number1))
        yes_no2 = input("Type 'yes' if you want to go again. Otherwise type 'no'")
        if yes_no2.lower() == "no":
            print("Thanks for using my cipher!")
            break







