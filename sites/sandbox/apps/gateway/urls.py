from django.conf.urls import patterns, url

from apps.gateway import views
from oscar.apps.catalogue.views import ProductListView

urlpatterns = patterns('',
    url(r'^$', views.GatewayView.as_view(), name='gateway'),

)
