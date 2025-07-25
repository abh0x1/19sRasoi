from django.urls import path
from core.views import home , login , signup, about

urlpatterns = [ 
    path('',home,name="home"),
    path('login/',login,name="login"),
    path('signup/', signup,name="signup"),
    path('about/',about,name="about")
]