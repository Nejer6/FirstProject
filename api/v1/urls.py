from django.urls import path, include
from rest_framework.authentication import SessionAuthentication
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from applications.test_api.urls import test_router

# router = DefaultRouter()
# urlpatterns = router.urls
urlpatterns = test_router.urls

urlpatterns += [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('schema/', get_schema_view(title="API TITLE",
                                    description="API DISCRIPTION",
                                    version='1.0',
                                    )
         ),
    path('docs/', include_docs_urls(title="API TITLE",
                                    description="API DISCRIPTION",
                                    authentication_classes=[SessionAuthentication]),
         name='docs',
         ),
]
