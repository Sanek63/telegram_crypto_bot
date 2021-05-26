import uuid
import qrcode


def enctypr_caesar(text, key=3):
    c = ''
    for char in text:
        if char == ' ':
            c += char
        elif char.isupper():
            c = c + chr((ord(char) + key - 1040) % 33 + 1040)
        else:
            c = c + chr((ord(char) + key - 1072) % 33 + 1072)
    return c


def decrypt_caesar(text, key=3):
    c = ''
    for char in text:
        if char == ' ':
            c += char
        elif char.isupper():
            c = c + chr((ord(char) - key - 1040) % 33 + 1040)
        else:
            c = c + chr((ord(char) - key - 1072) % 33 + 1072)
    return c


def qr_code(message):
    img = qrcode.make(message)

    filename = f"./images/{uuid.uuid4()}.jpg"
    img.save(filename)

    return filename
