from django.conf.urls import include, url

from cowork import views

urlpatterns = [
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^offices/', include('cowork.offices.urls', namespace='offices')),
]
