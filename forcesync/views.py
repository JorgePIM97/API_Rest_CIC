from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from django.db.models import Sum, Count, Avg
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models.functions import TruncMonth

from .filters import (
    DevDetalleCorregidaFilter,
    ActivityFilter,
    CalendarFilter,
    OpportunityFilter,
    AccountFilter,
)

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
    filterset_class = ActivityFilter

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        'accountid_value',
        'comment',
        'salesrepid_value',
        'typeid_value',
    ]

    ordering_fields = [
        'date',
        'checkoutdate',
        'salesrepid_id',
        'accountid_id',
        'typeid_id',
    ]

    ordering = ['id']

    def get_serializer_context(self):
        context = super().get_serializer_context()

        vendedor_ids = (
            self.get_queryset()
            .exclude(salesrepid_id__isnull=True)
            .exclude(salesrepid_id=0)
            .values_list('salesrepid_id', flat=True)
            .distinct()
        )

        vendedores = ForceUser.objects.filter(
            id__in=vendedor_ids
        )

        context['vendedores_cache'] = {
            vendedor.id: vendedor
            for vendedor in vendedores
        }

        return context


class CalendarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = (
        Calendar.objects
        .select_related('sales_rep')
        .order_by('id')
    )

    serializer_class = CalendarSerializer
    filterset_class = CalendarFilter

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        'subject',
        'comment',
        'salesrepid_value',
    ]

    ordering_fields = [
        'enddate',
        'sales_rep',
        'accountid',
        'typeid_id',
    ]

    ordering = ['id']


class OpportunityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Opportunity.objects.all().order_by('id')
    serializer_class = OpportunitySerializer
    filterset_class = OpportunityFilter

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        'reference',
        'comments',
        'salesrepid_value',
        'statusid_value',
        'typeid_value',
    ]

    ordering_fields = [
        'datecreated',
        'closeddate',
        'wondate',
        'lostdate',
        'salesforecastdate',
        'total',
    ]

    ordering = ['id']

    def get_serializer_context(self):
        context = super().get_serializer_context()

        vendedor_ids = (
            self.get_queryset()
            .exclude(salesrepid_id__isnull=True)
            .exclude(salesrepid_id=0)
            .values_list('salesrepid_id', flat=True)
            .distinct()
        )

        vendedores = ForceUser.objects.filter(
            id__in=vendedor_ids
        )

        context['vendedores_cache'] = {
            vendedor.id: vendedor
            for vendedor in vendedores
        }

        return context


class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Account.objects.all().order_by('id')
    serializer_class = AccountSerializer
    filterset_class = AccountFilter

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        'name',
        'vatnumber',
        'city',
        'region',
        'email',
    ]

    ordering_fields = [
        'name',
        'city',
        'region',
        'datecreated',
        'dateupdated',
    ]

    ordering = ['id']

    def get_serializer_context(self):
        context = super().get_serializer_context()

        filas = self.get_queryset().values_list(
            'salesrepid1_id',
            'salesrepid2_id',
            'salesrepid3_id',
            'salesrepid4_id',
            'salesrepid5_id',
        )

        vendedor_ids = set()

        for fila in filas:
            for vendedor_id in fila:
                if vendedor_id:
                    vendedor_ids.add(vendedor_id)

        vendedores = ForceUser.objects.filter(
            id__in=vendedor_ids
        )

        context['vendedores_cache'] = {
            vendedor.id: vendedor
            for vendedor in vendedores
        }

        return context

class DevDetalleCorregidaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DevDetalleCorregida.objects.all().order_by('id')
    serializer_class = DevDetalleCorregidaSerializer
    filterset_class = DevDetalleCorregidaFilter

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        'nombrecliente',
        'representantedeventas',
        'articulo',
        'numerodedocumento',
    ]

    ordering_fields = [
        'fecha',
        'ingresos',
        'ingresosusd',
        'representantedeventas',
        'nombrecliente',
        'articulo',
    ]

    ordering = ['id']

    @action(detail=False, methods=['get'], url_path='resumen')
    def resumen(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        resultado = queryset.aggregate(
            total_ingresos_usd=Sum('ingresosusd'),
            total_ingresos_mxn=Sum('ingresos'),
            promedio_ingresos_usd=Avg('ingresosusd'),
            registros=Count('id'),
        )

        return Response({
            'total_ingresos_usd': resultado['total_ingresos_usd'] or 0,
            'total_ingresos_mxn': resultado['total_ingresos_mxn'] or 0,
            'promedio_ingresos_usd': resultado['promedio_ingresos_usd'] or 0,
            'registros': resultado['registros'],
        })

    @action(detail=False, methods=['get'], url_path='por-vendedor')
    def por_vendedor(self, request):
        queryset = self.filter_queryset(
            self.get_queryset().filter(id_vendedor_fm__gt=0)
        )

        resultado = (
            queryset
            .values(
                'id_vendedor_fm',
                'representantedeventas',
            )
            .annotate(
                total_ingresos_usd=Sum('ingresosusd'),
                registros=Count('id'),
            )
            .order_by('-total_ingresos_usd')
        )

        return Response(resultado)

    @action(detail=False, methods=['get'], url_path='sin-vendedor')
    def sin_vendedor(self, request):
        queryset = self.filter_queryset(
            self.get_queryset().filter(id_vendedor_fm=0)
        )

        resultado = (
            queryset
            .values('representantedeventas')
            .annotate(
                total_ingresos_usd=Sum('ingresosusd'),
                registros=Count('id'),
            )
            .order_by('-total_ingresos_usd')
        )

        return Response(resultado)

    @action(detail=False, methods=['get'], url_path='por-mes')
    def por_mes(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        resultado = (
            queryset
            .annotate(mes=TruncMonth('fecha'))
            .values('mes')
            .annotate(
                total_ingresos_usd=Sum('ingresosusd'),
                registros=Count('id'),
                vendedores=Count(
                    'id_vendedor_fm',
                    distinct=True,
                ),
            )
            .order_by('mes')
        )

        return Response(resultado)

    @action(detail=False, methods=['get'], url_path='por-cliente')
    def por_cliente(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        resultado = (
            queryset
            .values('nombrecliente')
            .annotate(
                total_ingresos_usd=Sum('ingresosusd'),
                promedio_ingresos_usd=Avg('ingresosusd'),
                registros=Count('id'),
            )
            .order_by('-total_ingresos_usd')
        )

        # Obtener límite enviado en la URL
        limit = request.query_params.get('limit')

        if limit:
            try:
                limit = int(limit)

                if limit > 0:
                    resultado = resultado[:limit]

            except ValueError:
                pass

        # Convertir NULL de ingresos a 0
        resultado = [
            {
                **fila,
                'total_ingresos_usd': fila['total_ingresos_usd'] or 0,
                'promedio_ingresos_usd': fila['promedio_ingresos_usd'] or 0,
            }
            for fila in resultado
        ]

        return Response(resultado)