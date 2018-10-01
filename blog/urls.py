from django.urls import path
from . import views

#URLs start from here
urlpatterns = [
    path('',views.post_list,name='post list'),
    path('register',views.register,name='register'),
    path('inbox',views.inbox,name='inbox'),
    path('login',views.login,name='login'),
    path('post/<int:pk>)/', views.post_detail, name='post_detail'),
]
