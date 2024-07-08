def encrypt_plain_text(plain_text, key):
    encrypted_text = ""
    for letter in plain_text:
        if letter.isalpha():
            if letter.isupper():
                key_amount = 65 # ASCII value for "A"
            else:
                key_amount = 97 # ASCII value for "a"
            key_text = chr((ord(letter) - key_amount + key) % 26 + key_amount)
            encrypted_text += key_text
        else:
            encrypted_text += letter # if there is a non-alphabetic character, it is added to the encrypted text
    return encrypted_text

print(encrypt_plain_text("The secret password is Rosebud", 8))


def brute_force(plain_text):
    for key in range(26): # finds all the possible encryptions 
        print(f"Key {key}: {encrypt_plain_text(plain_text, key)}")

plain_text = "THE NEW PASSWORD IS SWORDFISH"
brute_force(plain_text)
            