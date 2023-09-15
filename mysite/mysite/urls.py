
from django.contrib import admin
from django.urls import path, include
#comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('app_blog.urls')),
]
