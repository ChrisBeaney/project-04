from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django-admin/', admin.site.urls),
    # 'admin/' route not working.
    path('admin/', include('rest_framework.urls')),
    path('holes/', include('rounds.urls'))
]
