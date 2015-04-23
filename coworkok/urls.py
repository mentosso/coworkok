from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

import settings
from coworkok import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^cowork/', include('cowork.urls', namespace='cowork')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
