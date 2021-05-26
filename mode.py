from enum import Enum


class Mode(Enum):
    default = ["Главное меню", "main_menu"]

    in_cezar = ["В шифре цезаря", "In chiffre of cezar"]
    in_qr = ["В qr коде", "In qr code"]
    in_indechiffrable = ["В шифре виженеро", "In chiffre of indechiffrable"]

    cezar_encrypt = ["Шифровать цезарь", "Encrypt cezar"]
    cezar_decrypt = ["Дешифровать цезарь", "Decrypt cezar"]

    indechiffrable_encrypt = ["Шифровать виженера", "Encrypt indechiffrable"]
    indechiffrable_decrypt = ["Дешифрование виженера", "Decrypt indechiffrable"]

    in_indechiffrable_encrypt = ["В шифрование виженера", "In encrypt indechiffrable"]
    in_indechiffrable_decrypt = ["В дешифрование виженера", "In decrypt indechiffrable"]
