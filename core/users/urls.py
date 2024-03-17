from django.urls import path
from users.views import AboutUSView

urlpatterns = [
    path('',AboutUSView.as_view())
]
