from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token
from intercambios.urls import router

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token, name='api-token'),
]
