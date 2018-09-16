from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/olimpiada/', include('olimpiada.urls')),
	url(r'^api-auth/', include('rest_framework.urls')),
]