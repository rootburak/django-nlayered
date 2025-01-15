from ..abstracts.UserAbstractService import UserService
from ...dataaccess.concrete.Customer import Customer 


class CustomerRepository(UserService):
    def new_user(self, name, email, password):
        if len(name) <5:
            raise ValueError("Name must be at least 5 characters long")
        elif email.find("@") == False:
            raise ValueError("Please enter your email address")
        elif len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return Customer.new_user(name, email, password)
    def all_users(self):
        return Customer.all_users()
    def get_user_by_id(self, user_id):
        return Customer.get_user_by_id(user_id)
