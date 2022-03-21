from . import views
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='/'),
    path('notifications',views.notifications,name='notifications'),
    path('add',views.add,name='add'),
    path('register',views.register,name='register'),
    path('faq',views.faq,name='faq'),
    path('login',views.login,name='login'),
    path('apply',views.apply,name='apply'),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)