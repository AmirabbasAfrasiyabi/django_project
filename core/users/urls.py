from django.urls import path
from users.views import SignupView

urlpatterns = [
    path('sign-up',SignupView.as_view() , name='sign-up')
]
