from django.urls import path
from . import views
#URLs start from here
urlpatterns = [
    path('',views.post_list,name='post list'),
]
