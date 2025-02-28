from django.contrib import admin
from django.http import HttpRequest
from django.urls import URLPattern, path


from tabom.services.like_service import do_like




urlpatterns = [
    path("admin/", admin.site.urls),

]
