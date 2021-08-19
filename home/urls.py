from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Admin Login"
admin.site.site_title = "Welcome to the Bus Pass Portal Dashboard"
admin.site.index_title = "Welcome to this Portal"
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('buypass', views.buypass, name='buypass'),
    path('buyticket', views.buyticket, name='buyticket'),
    path('renew', views.renew, name='renew')

]  
