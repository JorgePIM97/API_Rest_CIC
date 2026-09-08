# CIC API — Roadmap

## Fase 0 — Preparación
- [x] Crear entorno virtual, proyecto Django y app `forcesync`.
- [x] Instalar dependencias.
- [x] Configurar `.env`, `.gitignore` y carpeta `logs`.

## Fase 1 — SQL Server
- [x] Configurar `DATABASES` y ODBC Driver 17.
- [x] Conectar con `ForceSyncDB_Worker`.
- [x] Validar con `dbshell` y datos reales.

## Fase 2 — Modelos existentes
- [x] Inspeccionar `Users`, `Activities`, `Calendars`, `Opportunities`, `Accounts` y `dev_Detalle_Corregida`.
- [x] Renombrar `Users` a `ForceUser`.
- [x] Mantener `managed = False`.
- [x] Validar ORM de `ForceUser`, `Activity`, `Calendar`, `Opportunity`, `Account` y `DevDetalleCorregida`.
- [x] Analizar relaciones lógicas y ausencia de FK físicas.
- [x] Mantener como `IntegerField` las relaciones sin integridad garantizada.
- [x] Modelar `Calendar.sales_rep` como ForeignKey lógica con `db_constraint=False`.
- [x] Agregar PK técnica a `dev_Detalle_Corregida`.
- [x] Consolidar decisiones principales de `models.py`.

## Fase 3 — API GET
- [x] Crear `serializers.py`.
- [x] Crear serializers para los seis modelos principales.
- [x] Crear `ReadOnlyModelViewSet`.
- [x] Configurar `DefaultRouter` y URLs.
- [x] Crear endpoints GET de listado y detalle.
- [x] Probar endpoints con Postman.
- [x] Configurar paginación global de 50 registros.
- [x] Ordenar QuerySets por `id`.
- [x] Resolver vendedores inexistentes de forma segura.

## Fase 4 — Relaciones y serializers enriquecidos
- [x] Manejar valores `0` e IDs huérfanos.
- [x] Incorporar datos de vendedor cuando existe.
- [x] Crear serializer anidado para `Calendar`.
- [x] Crear lista de vendedores para `Account`.
- [x] Usar `select_related('sales_rep')` en `Calendar`.
- [ ] Optimizar `Activity`, `Opportunity` y `Account` para evitar consultas N+1.

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
- [ ] Diseñar endpoint y validar archivo.
- [ ] Procesar datos y manejar errores/duplicados.
- [ ] Garantizar que la carga preserve la PK técnica de `dev_Detalle_Corregida`.

## Fase 9 — Análisis y filtros
- [ ] Filtros por vendedor, fechas, cliente y segmento.
- [ ] Indicadores comerciales.

## Fase 10 — Flutter
- [ ] Definir contratos API/frontend.
- [ ] Autenticación.
- [ ] Consumo de endpoints.
- [ ] Vistas CIC.

## Fase 11 — Calidad y despliegue
- [ ] Pruebas automatizadas.
- [ ] Manejo uniforme de errores.
- [ ] Logging y documentación API.
- [ ] Optimización de consultas.
- [ ] Configuración de producción.

## Checkpoint actual — 2026-09-08
Las fases 0, 1, 2 y 3 están completadas. La fase 4 está funcionalmente completada salvo la optimización de consultas N+1. El siguiente bloque de trabajo es **Fase 5 — JWT**.
