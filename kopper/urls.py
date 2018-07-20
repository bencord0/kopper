from django.conf.urls import url

from kopper import views

urlpatterns = [
    url('event/', views.event, name='event'),
]
