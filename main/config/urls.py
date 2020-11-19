from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from apps.core import views as core_views
from apps.users.views import UserActivate
from apps.api.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.landing, name='landing_url'),
    path('api/', include(router.urls)),
    path('order_email/', core_views.order_email, name='order_email_url'),
    path('activate/<int:pk>/<str:token>', UserActivate.as_view(), name='user_activate_url')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
