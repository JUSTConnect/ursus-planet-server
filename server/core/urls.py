from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.api.urls')),
    path('api/web3auth/', include('apps.web3auth.urls'))
]
