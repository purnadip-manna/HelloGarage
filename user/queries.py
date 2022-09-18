from .models import User

def is_exist(email):
    return User.objects.filter(email=email).exists()

def create_user(fname, lname, email, password):
    new_user = User.objects.create_user(email=email.strip(), password=password.strip(), first_name=fname.strip(), last_name=lname.strip(), username=fname.strip())
    new_user.save()