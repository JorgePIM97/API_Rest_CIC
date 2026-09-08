from rest_framework import viewsets

from .models import (
    ForceUser,
    Activity,
    Calendar,
    Opportunity,
    Account,
    DevDetalleCorregida,
)

from .serializers import (
    ForceUserSerializer,
    ActivitySerializer,
    CalendarSerializer,
    OpportunitySerializer,
    AccountSerializer,
    DevDetalleCorregidaSerializer,
)


class ForceUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ForceUser.objects.all().order_by('id')
    serializer_class = ForceUserSerializer


class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all().order_by('id')
    serializer_class = ActivitySerializer


class CalendarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = (
        Calendar.objects
        .select_related('sales_rep')
        .order_by('id')
    )
    serializer_class = CalendarSerializer


class OpportunityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Opportunity.objects.all().order_by('id')
    serializer_class = OpportunitySerializer


class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Account.objects.all().order_by('id')
    serializer_class = AccountSerializer


class DevDetalleCorregidaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DevDetalleCorregida.objects.all().order_by('id')
    serializer_class = DevDetalleCorregidaSerializer