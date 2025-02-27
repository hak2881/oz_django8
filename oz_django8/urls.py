from django.contrib import admin
from django.http import HttpRequest
from django.urls import URLPattern, path
from ninja import NinjaAPI

from tabom.services.like_service import do_like

api = NinjaAPI()


@api.get("like")
def api_do_like(request: HttpRequest, user_id: int, article_id: int) -> None:
    do_like(user_id, article_id)
    return None


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
