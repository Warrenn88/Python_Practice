letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
           "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z"]

while True:
    request = input("Welcome to Caesar Cypher.\nPlease select encrypt or decrypt")
    if request.lower() == "encrypt":
        user_input = input("Please provide an input")
        shift = int(input("Please provide a positive shift number"))
        def encrypt(user_input, shift):
            cipher_text = ''
            for i in user_input:
                position = letters.index(i)
                if position + shift < 25:
                    new_position = position + shift
                    new_letter = letters[new_position]
                    cipher_text += new_letter
                else:
                    new_position = (position + shift) - 26
                    new_letter = letters[new_position]
                    cipher_text += new_letter
            print(cipher_text)
        encrypt(user_input, shift)

    elif request.lower() == "decrypt":
        user_input = input("Please provide an input")
        shift = int(input("Please provide a positive shift number"))
        def decrypt(user_input, shift):
            cipher_text = ''
            for i in user_input:
                position = letters.index(i)
                if (position - shift) >= 0:
                    new_position = position - shift
                    new_letter = letters[new_position]
                    cipher_text += new_letter
                else:
                    new_position = (position - shift) + 26
                    new_letter = letters[new_position]
                    cipher_text += new_letter
            print(cipher_text)
        decrypt(user_input, shift)




