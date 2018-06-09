from django.conf.urls import url

from kopper.event import views

urlpatterns = [
    url('event/', views.handle_event, name='event'),
]
