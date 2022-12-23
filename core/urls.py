from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('login/', views.LogIn , name='login'),
    path('signup/', views.SignUp , name='signup'),
    path('logout/', views.LogOut , name='logout'),
    path('aboutask/<int:pk>/', views.aboutask , name='aboutask'),
    path('showstats/', views.showstats , name='showstats'),
    path('nothing/', views.nothing , name='nothing'),

]