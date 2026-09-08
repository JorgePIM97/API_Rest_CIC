from rest_framework.routers import DefaultRouter
from .views import (
    ForceUserViewSet,
    ActivityViewSet,
    CalendarViewSet,
    OpportunityViewSet,
    AccountViewSet,
    DevDetalleCorregidaViewSet,
)


router = DefaultRouter()

router.register(
    r'usuarios',
    ForceUserViewSet,
    basename='usuarios'
)

# urlpatterns = router.urls


router.register(
    r'actividades',
    ActivityViewSet,
    basename='actividades'
)

# urlpatterns = router.urls


router.register(
    r'calendarios',
    CalendarViewSet,
    basename='calendarios'
)

# urlpatterns = router.urls


router.register(
    r'oportunidades',
    OpportunityViewSet,
    basename='oportunidades'
)

router.register(
    r'cuentas',
    AccountViewSet,
    basename='cuentas'
)

router.register(
    r'ventas',
    DevDetalleCorregidaViewSet,
    basename='ventas'
)

urlpatterns = router.urls