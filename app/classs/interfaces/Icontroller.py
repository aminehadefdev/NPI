##contrat des controllers
from abc import abstractmethod

class Icontroller:
    @abstractmethod
    def post():
        pass
    @abstractmethod
    def get():
        pass