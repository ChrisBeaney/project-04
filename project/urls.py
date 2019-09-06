from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django-admin/', admin.site.urls),
    # 'admin/' route not working.
    path('admin/', include('rest_framework.urls')),
    path('api/', include('jwt_auth.urls')),
    path('holes/', include('rounds.urls'))
]






#
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('auth/', include('rest_framework.urls')),
#     path('api/', include('movies.urls')),

#     path('', include('frontend.urls'))
# ]
