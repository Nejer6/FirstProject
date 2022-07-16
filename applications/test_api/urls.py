from rest_framework.routers import DefaultRouter

from .api import *

test_router = DefaultRouter()
test_router.register(r'person', PersonViewSet, 'person')
test_router.register(r'pet', PetViewSet, 'pet')
