from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dbapp.urls')),  # Include the app's URLs without a circular import
]

