
from django.urls import path
from . import views


urlpatterns = [
    path('',views.main,name='main'),
    path('index/',views.index,name='index'),
    path('delete_transaction/<id>/',views.delete_transaction,name='delete_transaction'),
    path('login/',views.login_view,name='login_view'),
    path('register/',views.register_view,name='register_view'),
]
