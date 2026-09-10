import django_filters
from django.db.models import Q


from .models import (
    DevDetalleCorregida,
    Activity,
    Calendar,
    Opportunity,
    Account,
)


class DevDetalleCorregidaFilter(django_filters.FilterSet):

    fecha_desde = django_filters.DateFilter(
        field_name='fecha',
        lookup_expr='gte'
    )

    fecha_hasta = django_filters.DateFilter(
        field_name='fecha',
        lookup_expr='lte'
    )

    ingresosusd_min = django_filters.NumberFilter(
        field_name='ingresosusd',
        lookup_expr='gte'
    )

    ingresosusd_max = django_filters.NumberFilter(
        field_name='ingresosusd',
        lookup_expr='lte'
    )

    class Meta:
        model = DevDetalleCorregida

        fields = [
            'id_vendedor_fm',
            'representantedeventas',
            'nombrecliente',
            'articulo',
            'estadotransaccion',
            'fecha_desde',
            'fecha_hasta',
            'ingresosusd_min',
            'ingresosusd_max',
        ]

class ActivityFilter(django_filters.FilterSet):

    fecha_desde = django_filters.DateFilter(
        field_name='date',
        lookup_expr='gte'
    )

    fecha_hasta = django_filters.DateFilter(
        field_name='date',
        lookup_expr='lte'
    )

    class Meta:
        model = Activity

        fields = [
            'salesrepid_id',
            'accountid_id',
            'typeid_id',
            'checkintypeid',
            'fecha_desde',
            'fecha_hasta',
        ]

class CalendarFilter(django_filters.FilterSet):

    fecha_desde = django_filters.DateFilter(
        field_name='enddate',
        lookup_expr='gte'
    )

    fecha_hasta = django_filters.DateFilter(
        field_name='enddate',
        lookup_expr='lte'
    )

    class Meta:
        model = Calendar

        fields = [
            'sales_rep',
            'accountid',
            'completed',
            'task',
            'typeid_id',
            'fecha_desde',
            'fecha_hasta',
        ]

class OpportunityFilter(django_filters.FilterSet):

    fecha_desde = django_filters.DateFilter(
        field_name='datecreated',
        lookup_expr='gte'
    )

    fecha_hasta = django_filters.DateFilter(
        field_name='datecreated',
        lookup_expr='lte'
    )

    class Meta:
        model = Opportunity

        fields = [
            'salesrepid_id',
            'statusid_id',
            'typeid_id',
            'accountid1_id',
            'fecha_desde',
            'fecha_hasta',
        ]

class AccountFilter(django_filters.FilterSet):

    vendedor = django_filters.NumberFilter(
        method='filter_vendedor'
    )

    def filter_vendedor(self, queryset, name, value):
        return queryset.filter(
            Q(salesrepid1_id=value) |
            Q(salesrepid2_id=value) |
            Q(salesrepid3_id=value) |
            Q(salesrepid4_id=value) |
            Q(salesrepid5_id=value)
        )

    class Meta:
        model = Account

        fields = [
            'segmentid_id',
            'statusid_id',
            'typeid_id',
            'city',
            'region',
            'vendedor',
        ]