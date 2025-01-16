from abc import ABC,abstractmethod

class UserService(ABC):
    @abstractmethod
    def new_user(name, email, password):
        pass
    @abstractmethod
    def all_users():
        pass
    @abstractmethod
    def get_user_by_id(user_id):
        pass
