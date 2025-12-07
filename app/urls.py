from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('models.urls')),
    path('api/v1/', include('scales.urls')),
    path('api/v1/', include('sections.urls'))
]
