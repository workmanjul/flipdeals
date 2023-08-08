from django.urls import path

from . import views

urlpatterns = [
    path("", views.job_summary, name='home'),
    path("input/", views.input, name='input'),
    path("job-summary", views.job_summary, name='job-summary'),
    path("job-list", views.job_list, name='job-list'),
    path("client-summary", views.client_summary, name='client-summary'),
    path("job-list-client", views.job_list_client, name='job-list-client'),
]