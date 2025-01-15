from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GastoViewSet
from django.urls import path
from .views import totales_por_departamento

router = DefaultRouter()
router.register(r'gastos', GastoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns = [
    path('totales/', totales_por_departamento, name='totales_por_departamento'),
]
