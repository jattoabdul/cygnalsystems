from django.conf.urls import url
from django.conf.urls import include
from app import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^about/', views.about, name='about'),
    # url(r'^services/', views.services, name='services'),
    # url(r'^service/(?P<pk>\d+)/$', views.services_detail, name='services_detail'),
    # url(r'^cservice/(?P<pk>\d+)/$', views.cservices_detail, name='cservices_detail'),
    url(r'^contact/', views.contact, name='contact'),
    # url(r'^staff/', views.staff, name='staff'),
    url(r'^blog/', include('blog.urls')),
    # url(r'^portfolio/', include('work.urls')),
]

