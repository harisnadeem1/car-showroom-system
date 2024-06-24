from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('super_admin/', admin.site.urls),
    path('', include('user_portal.urls')),
    path('seller/', include('seller_portal.urls')),
    path('admin/', include('admin_portal.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)