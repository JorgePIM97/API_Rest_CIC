import django_filters

from .models import DevDetalleCorregida


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