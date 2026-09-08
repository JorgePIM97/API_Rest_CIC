from rest_framework import serializers
from .models import (
    ForceUser,
    Activity,
    Calendar,
    Opportunity,
    Account,
    DevDetalleCorregida,
)


class ForceUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForceUser
        fields = [
            'id',
            'name',
            'lastname',
            'email',
            'phone',
            'isactive',
        ]

class ActivitySerializer(serializers.ModelSerializer):
    vendedor = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = [
            'id',
            'accountid_id',
            'accountid_value',
            'date',
            'checkoutdate',
            'comment',
            'latitude',
            'longitude',
            'salesrepid_id',
            'salesrepid_value',
            'typeid_id',
            'typeid_value',
            'vendedor',
        ]

    def get_vendedor(self, obj):
        user = ForceUser.objects.filter(id=obj.salesrepid_id).first()

        if user is None:
            return None

        return {
            'id': user.id,
            'name': user.name,
            'lastname': user.lastname,
            'email': user.email,
        }

class CalendarSerializer(serializers.ModelSerializer):
    vendedor = ForceUserSerializer(
        source='sales_rep',
        read_only=True
    )

    class Meta:
        model = Calendar
        fields = [
            'id',
            'accountid',
            'subject',
            'comment',
            'startdate',
            'starthour',
            'enddate',
            'endhour',
            'completed',
            'task',
            'sales_rep',
            'salesrepid_value',
            'typeid_id',
            'typeid_value',
            'vendedor',
        ]

class OpportunitySerializer(serializers.ModelSerializer):
    vendedor = serializers.SerializerMethodField()

    class Meta:
        model = Opportunity
        fields = [
            'id',
            'reference',
            'accountid1_id',
            'accountid1_value',
            'city',
            'region',
            'datecreated',
            'closeddate',
            'lostdate',
            'wondate',
            'salesforecastdate',
            'salesprobability',
            'salesrepid_id',
            'salesrepid_value',
            'statusid_id',
            'statusid_value',
            'total',
            'typeid_id',
            'typeid_value',
            'vendedor',
        ]

    def get_vendedor(self, obj):
        user = ForceUser.objects.filter(id=obj.salesrepid_id).first()

        if user is None:
            return None

        return {
            'id': user.id,
            'name': user.name,
            'lastname': user.lastname,
            'email': user.email,
        }


class AccountSerializer(serializers.ModelSerializer):
    vendedores = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = [
            'id',
            'name',
            'vatnumber',
            'email',
            'phone',
            'website',
            'address1',
            'address2',
            'city',
            'region',
            'postcode',
            'latitude',
            'longitude',
            'typeid_id',
            'typeid_value',
            'segmentid_id',
            'segmentid_value',
            'statusid_id',
            'statusid_value',
            'salesrepid1_id',
            'salesrepid1_value',
            'salesrepid2_id',
            'salesrepid2_value',
            'salesrepid3_id',
            'salesrepid3_value',
            'salesrepid4_id',
            'salesrepid4_value',
            'salesrepid5_id',
            'salesrepid5_value',
            'vendedores',
        ]

    def get_vendedores(self, obj):
        vendedor_ids = [
            obj.salesrepid1_id,
            obj.salesrepid2_id,
            obj.salesrepid3_id,
            obj.salesrepid4_id,
            obj.salesrepid5_id,
        ]

        vendedores = []

        for vendedor_id in vendedor_ids:
            if not vendedor_id:
                continue

            user = ForceUser.objects.filter(id=vendedor_id).first()

            if user is not None:
                vendedores.append({
                    'id': user.id,
                    'name': user.name,
                    'lastname': user.lastname,
                    'email': user.email,
                })

        return vendedores


class DevDetalleCorregidaSerializer(serializers.ModelSerializer):

    class Meta:
        model = DevDetalleCorregida
        fields = [
            'id',
            'nombrecliente',
            'clase',
            'descripcion',
            'articulo',
            'tipo',
            'numerodedocumento',
            'fecha',
            'cantidadvendida',
            'preciodeventa',
            'ingresos',
            'numerosdeserie',
            'representantedeventas',
            'id_cliente_fm',
            'cliente_rfc',
            'moneda',
            'importe',
            'tipodecambio',
            'preciounitario',
            'id_vendedor_fm',
            'tipodecambiousd',
            'ingresosusd',
            'estadotransaccion',
        ]