from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls))
]

# serve media files from project root in development only.
if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {
                "document_root": settings.MEDIA_ROOT,
            }
        )
    ]
