from abc import ABC,abstractmethod

class UserService(ABC):
    @abstractmethod
    def new_user(self, name, email, password):
        pass
    @abstractmethod
    def all_users(self):
        pass
    @abstractmethod
    def get_user_by_id(self, user_id):
        pass
