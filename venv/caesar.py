def encipher(cipher_input, key):
    string = ''
    for char in cipher_input:
        if ord('a') <= ord(char) <= ord('z'):
            num = ord(char) - 97
            num = (num + key)%26
            num += 97
            string += chr(num)
        elif ord('A') <= ord(char) <= ord('Z'):
            num = ord(char) - 65
            num = (num + key)%26
            num += 65
            string += chr(num)
    return string

    return string
def decipher(cipher_input, key):
    string = ''
    for char in cipher_input:
        if ord('a') <= ord(char) <= ord('z'):
            num = ord(char) - 97
            num = (num - key) % 26
            num += 97
            string += chr(num)
        elif ord('A') <= ord(char) <= ord('Z'):
            num = ord(char) - 65
            num = (num - key) % 26
            num += 65
            string += chr(num)
    return string