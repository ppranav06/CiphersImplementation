
from interfaces import SymmetricCipher
from caesar import CaesarCipher
from typing import Tuple
from math import ceil

class VigenereCipher(SymmetricCipher):
    """
    Vigenere Cipher
    Caesar cipher for each character
    Unbreakable for 300 years
    """
    def __init__(self, 
        key: str,
        type: str = 'repeatkey',
    ) -> None:
        super().__init__(key)
        if type not in ['autokey', 'repeatkey']:
            raise ValueError('type must be either "autokey" or "repeatkey"')
        self._type = type

    @staticmethod
    def preprocess(text) -> Tuple[str, int]:
        text = ''.join(ch for ch in CaesarCipher.convert_to_uppercase(text) if ch.isalpha())
        return text, len(text)

    def _char_to_shift(self, char: str) -> int:
        return ord(char) - ord('A')

    def _shift_to_char(self, shift: int) -> str:
        return chr((shift % 26) + ord('A'))

    def extendedkey(self, text: str) -> str:
        """
        Extends key until length of text. Can follow repeat-key or autokey.
        Should be provided with the preprocessed text.
        """
        n = len(text)

        # autokey: includes KEY<RESTOFTEXT> as the encrypting key
        if self._type == 'autokey':
            return f"{self._key}{text[:max(0, n - len(self._key))]}"
        
        # default: repeat key
        return f"{self._key * ceil(n / len(self._key))}"[:n]
            

    def encrypt(self, text: str) -> str:
        """
        Encrypts the given text using the Vigenere cipher.
        """
        text, n = VigenereCipher.preprocess(text)

        k = self.extendedkey(text)
        print(k)
        encrypted = ''
        for i in range(n):
            shift = self._char_to_shift(text[i]) + self._char_to_shift(k[i])
            encrypted += self._shift_to_char(shift)

        return encrypted

    def decrypt(self, text: str) -> str:
        """
        Decrypts the given text using the Vigenere cipher.
        """
        text, n = VigenereCipher.preprocess(text)

        decrypted = ''
        if self._type == 'repeatkey':
            k = self.extendedkey(text)
            for i in range(n):
                shift = self._char_to_shift(text[i]) - self._char_to_shift(k[i])
                decrypted += self._shift_to_char(shift)
            return decrypted

        for i in range(n):
            if i < len(self._key):
                key_char = self._key[i]
            else:
                key_char = decrypted[i - len(self._key)]

            shift = self._char_to_shift(text[i]) - self._char_to_shift(key_char)
            decrypted += self._shift_to_char(shift)

        return decrypted

    def encrypt_raw(self, text: str) -> str:
        """
        Encryption formula:
        C_i = (P_i + K_i) % 26
        """
        text, n = VigenereCipher.preprocess(text)
        k = self.extendedkey(text)
        
        encrypted = ''
        for i in range(n):
            encrypted += self._shift_to_char(
                self._char_to_shift(text[i]) + self._char_to_shift(k[i])
            )
        
        return encrypted

    def decrypt_raw(self, text: str) -> str:
        """
        Decryption formula:
        P_i = (C_i - K_i) % 26
        """
        text, n = VigenereCipher.preprocess(text)
        k = self.extendedkey(text)

        decrypted = ''
        if self._type == 'repeatkey':
            for i in range(n):
                decrypted += self._shift_to_char(
                    self._char_to_shift(text[i]) - self._char_to_shift(k[i])
                )
            return decrypted

        for i in range(n):
            if i < len(self._key):
                key_char = self._key[i]
            else:
                key_char = decrypted[i - len(self._key)]

            decrypted += self._shift_to_char(
                self._char_to_shift(text[i]) - self._char_to_shift(key_char)
            )
        return decrypted

if __name__ == '__main__':
    cipher = VigenereCipher(key='OBLIQUEASS', type='autokey')
    encrypted = cipher.encrypt('The quick brown fox jumps over lazy dogs.')
    print(encrypted)
    decrypted = cipher.decrypt(encrypted)
    print(decrypted)