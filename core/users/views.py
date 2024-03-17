
from django.views.generic import CreateView 
from users.forms import UserRegisterForm
from django.urls import reverse_lazy

# Create your views here.

class SignupView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/sign_up.html'
    success_url = reverse_lazy('sign_up')   