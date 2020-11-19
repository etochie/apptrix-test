from rest_framework import routers

from apps.users.views import UserView

router = routers.DefaultRouter()
router.register('user', UserView, basename='user')