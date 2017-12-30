from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^persons/$', views.person_list, name='person_list'),
    url(r'^api-auth/', include('rest_framework.urls'))
]
