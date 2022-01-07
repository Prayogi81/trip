from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, CurrentUserViewSet


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('current/', CurrentUserViewSet.as_view({'get': 'list'})),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
]



