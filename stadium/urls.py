from django.urls import path
from .views import StadiumAddView,StadiumFilter,BookingView,WeeksView,StadiumSingle
urlpatterns = [
    path('', StadiumAddView.as_view()),
    path('week/',WeeksView.as_view()),
    path('filter/', StadiumFilter.as_view()),
    path('booking/', BookingView.as_view()),
    path('<int:pk>/',StadiumSingle.as_view())
]