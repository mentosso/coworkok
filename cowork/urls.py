from django.conf.urls import include, url

from cowork import views

urlpatterns = [
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^locations/', include('cowork.locations.urls', namespace='locations')),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^desks/$', views.desks, name='search_desk'),
    url(r'^desks_city/$', views.desksByCity, name='search_desk_city'),
    url(r'^rent/$', views.rentDesk, name='rent_desk')
]
