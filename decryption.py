def decrypt_cipher_text(cipher_text, key):
    decrypted_text = ""
    for letter in cipher_text:
        if letter.isalpha():
            if letter.isupper():
                key_amount = 65 
            else:
                key_amount = 97
            key_text = chr((ord(letter) - key_amount - key) % 26 + key_amount)
            decrypted_text += key_text
        else:
            decrypted_text += letter 
    return decrypted_text

print(decrypt_cipher_text("Bpm amkzmb xiaaewzl qa Zwamjcl", 8))

def brute_force(cipher_text):
    for key in range(26):
        print(f"Key {key}: {decrypt_cipher_text(cipher_text, key)}")

cipher_text = "NBY HYQ JUMMQILX CM MQILXZCMB"
brute_force(cipher_text)