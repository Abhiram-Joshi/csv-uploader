from django.conf.urls import url
from . import views

urlpatterns = [
    url("^upload", views.ExtractContactsAPIView.as_view(), name="extract_contacts"),
    url("^get", views.ExtractContactsAPIView.as_view(), name="get_contacts"),
]