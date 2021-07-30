from django.contrib import admin
from django.urls import path
from easy_parser.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
]
