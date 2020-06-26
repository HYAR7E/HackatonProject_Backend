from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/', include('master.urls')),
    path('joboffer/', include('joboffer.urls')),

    path('security/', include('security.urls')),
]
