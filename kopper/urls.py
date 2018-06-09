from django.conf.urls import url

from kopper.event import views

urlpatterns = [
    url('event/', views.event, name='event'),
]
