from  django.urls import path
from .views import NicUserView


urlpatterns = [
    path('', NicUserView.as_view())
]