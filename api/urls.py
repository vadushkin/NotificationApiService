from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'mailings', MailingViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'operators', OperatorViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('', home_page, name='home'),
]
