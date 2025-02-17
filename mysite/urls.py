from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin entrance
    path('polls/', include('polls.urls')),  # Your poll booth
]
