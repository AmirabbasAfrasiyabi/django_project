
from django.views.generic import CreateView 
from users.forms import UserRegisterForm

# Create your views here.

class SignupView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/sign_up.html'
