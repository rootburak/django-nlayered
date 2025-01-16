from business.abstracts.UserAbstractService import UserService
from dataaccess.concrete.Customer import Customer 


class CustomerRepository(UserService):
    @staticmethod
    def new_user(name, email, password):
        if len(name) <5:
            print("name error")
            raise ValueError("Name must be at least 5 characters long")
        elif email.find("@") == False:
            print("email error")
            raise ValueError("Please enter your email address")
        elif len(str(password)) < 5:
            print("password error")
            raise ValueError("Password must be at least 8 characters long")
        Customer.new_user(name, email, password)
        return "success"
    @staticmethod
    def all_users():
        return Customer.all_users()
    @staticmethod
    def get_user_by_id(user_id):
        return Customer.get_user_by_id(user_id)
