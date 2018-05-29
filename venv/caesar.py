def decipher(cipher_input, offset):
    string = ''
    for char in cipher_input:
        char_value = ord(char)
        char_offset = char_value + offset
        if 65 <= char_value <= 90:
            if char_offset < 90:
                string += chr(char_offset)
            else:
                string += chr(char_offset - 26)
        elif 97 <= char_value <= 122:
            if char_offset < 123:
                string += chr(char_offset)
            else:
                string += chr(char_offset - 26)
    return string