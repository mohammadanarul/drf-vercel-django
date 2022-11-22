from django.contrib import admin
from django.urls import include, path

from task.views import home_view

urlpatterns = [
    path("", home_view, name="home"),
    path("admin/", admin.site.urls),
    path("tasks/", include("task.urls")),
]
