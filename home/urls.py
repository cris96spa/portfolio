from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views

admin.site.site_header = 'Login to Cristian'
admin.site.site_title = 'Welcome to Dashboard'
admin.site.index_title = 'Welcome my Portal'

urlpatterns = [
    path('', views.home, name='home'),
]
