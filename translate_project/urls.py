from django.contrib import admin
from django.urls import path, include
from translate_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('translate_app.urls')),
    path('', home, name='home'),
]
