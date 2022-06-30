
from django.contrib import admin
from django.urls import path

from email_app.views import RegisterView, VerifyOTP

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/', VerifyOTP.as_view(), name='verify'),
    
]
