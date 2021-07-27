from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.i18n import i18n_patterns

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


admin.site.site_header = 'App'
admin.autodiscover()
admin.site.enable_nav_sidebar = False

schema_view = get_schema_view(
    openapi.Info(
        title='App API',
        default_version='v1',
        description='App API Schema',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', admin.site.urls),
    path('accounts/', include('allauth.urls'), name='socialaccount_signup'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += i18n_patterns(
    path('api/', include('dj_rest_auth.urls')),
    path('api/registration/', include('dj_rest_auth.registration.urls')),
)

