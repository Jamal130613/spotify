from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title='Spotify',
        default_version='v1',
        description='Spotify'
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),
    path('account/', include ('applications.account.urls')),
    path('songs/', include ('applications.song.urls')),
    path('contact/', include ('applications.spam.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

