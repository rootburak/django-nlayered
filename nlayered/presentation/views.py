from django.http import JsonResponse
from django.shortcuts import render
from business.concrete.CustomerRepo import CustomerRepository
def home(req):
    return render(req,"index.html")
def newUser(req):
    user_name = req.POST.get("name")
    user_email = req.POST.get("email")
    user_password = req.POST.get("password")
    print(user_name, user_email, user_password)
    try:
        CustomerRepository.new_user(name=user_name,email=user_email,password=user_password)
        return render(req,"index.html")
    except:
        return JsonResponse({"error":"getting error"})
def allUsers(req):
    users = CustomerRepository.all_users()
    data = [{"name":user.name} for user in users]
    return JsonResponse(data, safe=False)
