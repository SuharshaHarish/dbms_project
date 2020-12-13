from django.contrib import admin
from django.urls import path
from dbms_app import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'dbms_app'

urlpatterns = [
    path('home/',views.home,name='home'),
    path('cust-register/',views.cust_register, name="cust_register"),
    path('emp-register/',views.emp_register, name="emp_register"),
    path('supp-register/',views.supp_register, name="supp_register"),
    path('login/',LoginView.as_view(template_name='dbms_app/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='dbms_app/logout.html'),name='logout'),
    path('buy-porsche',views.buy_porsche,name='buy_porsche'),
    path('buy-lamborghini',views.buy_lamborghini,name='buy_lamborghini'),    
    path('buy-harley',views.buy_harley,name='buy_harley'),  
    path('buy-royal',views.buy_royal,name='buy_royal'),  
    path('buy-benz',views.buy_benz,name='buy_benz'),
    path('success',views.success,name='success'),   
    path('profile',views.profile,name='profile'), 
    path('emp-profile',views.emp_profile,name='emp_profile'),
    path('cust-profile',views.cust_profile,name='cust_profile'),
    path('supp-profile',views.supp_profile,name='supp_profile')
]