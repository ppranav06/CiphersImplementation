
from interfaces import SymmetricCipher

class CaesarCipher(SymmetricCipher):
    """
    Simple shift cipher. Uses only one case (uppercase).
    """

    def __init__(self, shift: int) -> None:
        if shift not in range(0,26):
            raise ValueError("shift must be in range [0,25]")
        self.__shift = shift
    
    def shift_char(self, char):
        """shifts the character by the shift amount"""
        return chr((ord(char) - ord('A') + self.__shift) % 26 + ord('A'))
    
    @staticmethod
    def remove_spaces(text):
        """splits the word by spaces and merges them together"""
        return ''.join(text.split())        
        
    @staticmethod
    def convert_to_uppercase(text):
        """converts the text to uppercase"""
        return text.upper()
        
    def encrypt(self, text):
        """encrypts by shifting characters by selected shift amount"""
        text = CaesarCipher.remove_spaces(text)
        text = CaesarCipher.convert_to_uppercase(text)
        encrypted = ''
        for char in text:
            encrypted += self.shift_char(char)
        return encrypted

    def decrypt(self, text: str) -> str:
        """dumbass cipher. same decryption method as encrypt. encrypting twice gives back original text."""
        text = CaesarCipher.convert_to_uppercase(text)
        decrypted = self.encrypt(text)
        return decrypted

if __name__ == "__main__":
    ROT13 = CaesarCipher(13)
    encrypted = ROT13.encrypt("Red Wheelbarrow BBQ")
    print(encrypted)
    decrypted = ROT13.decrypt(encrypted)
    print(decrypted)