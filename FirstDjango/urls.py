from django.contrib import admin
from django.urls import path, include

from applications.test_api.views import PersonViewSet, PersonView, PersonPetsViewSet, PersonPetsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name='api'),
    path('person/',
         include(([
             path('', PersonViewSet.as_view(), name='persons'),
             path('<int:pk>/',
                  include(([
                      path('', PersonView.as_view(), name='detail'),
                      path('pets/',
                           include(([
                               path('', PersonPetsViewSet.as_view(), name='pets'),
                               path('<int:pk_pet>/', PersonPetsView.as_view(), name='pet')
                           ], 'person-pets')))
                  ], 'detail')))
         ], 'person'))),
    # path('person/', PersonViewSet.as_view(), name='person-list'),
    # path('person/<int:pk>/', PersonView.as_view(), name='person-detail'),
    # path('person/<int:pk>/pets/', PersonPetsViewSet.as_view(), name='person-pets'),
    # path('person/<int:pk>/pets/<int:pk_pet>', PersonPetsView.as_view(), name='person-pet-detail'),
]
