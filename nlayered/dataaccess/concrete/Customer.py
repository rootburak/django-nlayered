from ..abstracts.User import UserModelDataAcces
from ..models import User

class Customer(UserModelDataAcces):
    @staticmethod
    def new_user(name,email,password):
        new_user = User(username=name, email=email, password=password)
        new_user.save()
    @staticmethod
    def all_users():
        return User.objects.all()
    @staticmethod
    def get_user_by_id(user_id):
        return User.objects.get(id=user_id)
