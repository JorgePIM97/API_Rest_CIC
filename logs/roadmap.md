# CIC API — Roadmap

## Fase 0 — Preparación
- [x] Crear entorno virtual.
- [x] Crear proyecto Django.
- [x] Crear app `forcesync`.
- [x] Instalar dependencias.
- [x] Configurar `.env` y `.gitignore`.
- [x] Crear carpeta `logs`.

## Fase 1 — SQL Server
- [x] Configurar `DATABASES`.
- [x] Usar ODBC Driver 17.
- [x] Conectar con `ForceSyncDB_Worker`.
- [x] Validar con `dbshell`.
- [x] Consultar datos reales de `Users`.

## Fase 2 — Modelos existentes
- [x] Inspeccionar `Users`.
- [x] Inspeccionar `Activities`.
- [x] Inspeccionar `Calendars`.
- [x] Inspeccionar `Opportunities`.
- [x] Inspeccionar `Accounts`.
- [x] Inspeccionar `dev_Detalle_Corregida`.
- [x] Renombrar `Users` a `ForceUser`.
- [x] Mantener `managed = False`.
- [x] Validar ORM de `ForceUser`.
- [x] Validar ORM de `Activity`.
- [x] Analizar relaciones lógicas con `Users`.
- [x] Confirmar ausencia de FK físicas en SQL Server.
- [x] Probar temporalmente `ForeignKey` en `Activity`.
- [x] Detectar problema con valores `0` e IDs huérfanos.
- [x] Decidir mantener `Activity.salesrepid_id` como `IntegerField`.
- [x] Analizar `dev_Detalle_Corregida.Id_Vendedor_FM`.
- [x] Documentar los casos `Piso` y representantes especiales.
- [ ] Incorporar y validar `Calendar`.
- [ ] Incorporar y validar `Opportunity`.
- [ ] Incorporar y validar `Account`.
- [ ] Incorporar y validar `DevDetalleCorregida`.
- [ ] Revisar `models.py` completo.

## Fase 3 — API GET
- [ ] Crear `serializers.py`.
- [ ] Crear serializers iniciales.
- [ ] Crear endpoints GET.
- [ ] Configurar URLs.
- [ ] Probar con Postman.
- [ ] Resolver vendedores inexistentes de forma segura.

## Fase 4 — Relaciones y serializers enriquecidos
- [ ] Resolver asociaciones lógicas con `ForceUser`.
- [ ] Manejar valores `0`.
- [ ] Manejar IDs huérfanos.
- [ ] Incorporar datos de vendedor cuando exista.
- [ ] Crear serializers anidados donde aporte valor.

## Fase 5 — JWT
- [ ] Configurar SimpleJWT.
- [ ] Login y refresh.
- [ ] Proteger endpoints.
- [ ] Mantener separación entre `ForceUser` y usuarios de autenticación Django.

## Fase 6 — Permisos
- [ ] Definir roles.
- [ ] Implementar permisos.
- [ ] Diferenciar usuario normal y administrador.

## Fase 7 — Tablas manuales CIC
- [ ] `MovilidadRegistro`.
- [ ] `NotificacionesVendedores`.
- [ ] `PresupuestoSegmentos`.
- [ ] `ResumenMovilidad`.
- [ ] `StrikesVendedores`.
- [ ] `UsuariosCIC`.

## Fase 8 — Carga de Excel
- [ ] Diseñar endpoint.
- [ ] Validar archivo.
- [ ] Procesar datos.
- [ ] Manejar errores y duplicados.

## Fase 9 — Análisis y filtros
- [ ] Filtros por vendedor.
- [ ] Filtros por fechas.
- [ ] Filtros por cliente.
- [ ] Filtros por segmento.
- [ ] Indicadores comerciales.

## Fase 10 — Flutter
- [ ] Definir contratos API/frontend.
- [ ] Autenticación.
- [ ] Consumo de endpoints.
- [ ] Vistas CIC.

## Fase 11 — Calidad y despliegue
- [ ] Pruebas automatizadas.
- [ ] Manejo uniforme de errores.
- [ ] Logging.
- [ ] Documentación API.
- [ ] Configuración de producción.


## Flujo objetivo

```text
Force Manager
     ↓
Cliente existente
     ↓
ForceSyncDB_Worker
     ↓
Django ORM
     ↓
Django REST Framework
     ↓
JWT + permisos
     ↓
API CIC
     ↓
Flutter
```

## Próximo objetivo

**Terminar la Fase 2:** revisar `Activities`, `Calendars`, `Opportunities` y `Accounts`, validar sus relaciones con `Users` y preparar los modelos para comenzar los serializers y ViewSets.
