from django.urls import path
from . import views


urlpatterns = [
    path("", views.textbooks, name="textbooks"),
    path("<str:url>", views.render_text, name="render_text")
]