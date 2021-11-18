from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^auth", views.AuthAPIView.as_view(), name="user_authentication"),
    url(r"^update", views.UserUpdateDeleteAPIView.as_view(), name="user_update"),
    url(r"^delete", views.UserUpdateDeleteAPIView.as_view(), name="user_delete"),
]
