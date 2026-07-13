
from interfaces import SymmetricCipher
from caesar import CaesarCipher
from typing import Tuple
from math import ceil

class VigenereCipher(SymmetricCipher):
    """
    Vigenere Cipher
    Caesar cipher for each character
    Repeat-key implementation
    Unbreakable for 300 years
    """
    def __init__(self, key) -> None:
        super().__init__(key)
        self._key = key
        print(self._key)

    @staticmethod
    def preprocess(text) -> Tuple[str, int]:
        text = CaesarCipher.remove_spaces(CaesarCipher.convert_to_uppercase(text))
        return text, len(text)

    def extendedkey(self, n):
        k: str = f"{ self._key * ceil(n/len(self._key)) }"[:n]
        return k

    def encrypt(self, text: str) -> str:
        """
        Encrypts the given text using the Vigenere cipher.
        """
        text, n = VigenereCipher.preprocess(text)
        
        # the key used (extended to length of text)
        k = self.extendedkey(n)
        
        encrypted = ''
        for i in range(n):
            encrypted += CaesarCipher(
                    shift = ord(k[i]) - ord('A')
                ).encrypt(text[i])

        return encrypted

    def encrypt_raw(self, text: str) -> str:
        """
        Encryption formula:
        C_i = (P_i + K_i) % 26
        """
        text, n = VigenereCipher.preprocess(text)
        k = self.extendedkey(n)
        
        encrypted = ''
        for i in range(n):
            encrypted += chr( (ord(text[i]) + ord(k[i])) % 26 )
        
        return encrypted

    def decrypt(self, text: str) -> str:
        """
        Decrypts the given text using the Vigenere cipher.
        """
        text, n = VigenereCipher.preprocess(text)
        k = self.extendedkey(n)
        
        decrypted = ''
        for i in range(n):
            decrypted += CaesarCipher(
                    shift = ord(k[i]) - ord('A')
                ).decrypt(text[i])

        return decrypted

    def decrypt_raw(self, text: str) -> str:
        """
        Decryption formula:
        P_i = (C_i - K_i) % 26
        """
        text, n = VigenereCipher.preprocess(text)
        k = self.extendedkey(n)

        decrypted = ''
        for i in range(n):
            decrypted += chr( (ord(text[i]) - ord(k[i])) % 26 )
        return decrypted

if __name__ == '__main__':
    cipher = VigenereCipher(key='OBLIQUEASS')
    encrypted = cipher.encrypt('The quick brown fox jumps over lazy dogs.')
    print(encrypted)
    decrypted = cipher.decrypt(encrypted)
    print(decrypted)