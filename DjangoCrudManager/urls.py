from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud1/', include('crud1.urls')),
    path('crud2/', include('crud2.urls')),
]
