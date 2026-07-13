from abc import ABC, abstractmethod
from math import ceil

class Cipher(ABC):
    @abstractmethod
    def encrypt(self, text: str) -> str:
        pass
        
    @abstractmethod
    def decrypt(self, text: str) -> str:
        pass

class SymmetricCipher(Cipher):
    def __init__(self, key) -> None:
        self._key : str = key


class AsymmetricCipher(Cipher):
    def __init__(self, key) -> None:
        self._key : str = key
