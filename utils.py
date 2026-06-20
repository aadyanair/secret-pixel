def text_to_binary(message):
    binary = ''.join(format(ord(char), '08b') for char in message)
    return binary


def binary_to_text(binary_data):
    chars = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))
    return ''.join(chars)