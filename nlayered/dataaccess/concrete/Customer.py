from dataaccess.abstracts.User import UserModelDataAccess
from dataaccess.models import User as usermodel

class Customer(UserModelDataAccess):
    @staticmethod
    def new_user(name,email,password):
        new_user = usermodel(name=name, email=email, password=password)
        new_user.save()
    @staticmethod
    def all_users():
        return usermodel.objects.all()
    @staticmethod
    def get_user_by_id(user_id):
        return usermodel.objects.get(id=user_id)
