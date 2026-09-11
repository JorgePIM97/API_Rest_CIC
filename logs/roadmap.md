# CIC API --- Roadmap

## Fase 0 --- Preparación

-   [x] Crear entorno virtual, proyecto Django y app `forcesync`.
-   [x] Instalar dependencias.
-   [x] Configurar `.env`, `.gitignore` y carpeta `logs`.

## Fase 1 --- SQL Server

-   [x] Configurar `DATABASES` y ODBC Driver 17.
-   [x] Conectar con `ForceSyncDB_Worker`.
-   [x] Validar con `dbshell` y datos reales.

## Fase 2 --- Modelos existentes

-   [x] Inspeccionar `Users`, `Activities`, `Calendars`,
    `Opportunities`, `Accounts` y `dev_Detalle_Corregida`.
-   [x] Renombrar `Users` a `ForceUser`.
-   [x] Mantener `managed = False`.
-   [x] Validar ORM de los seis modelos principales.
-   [x] Analizar relaciones lógicas y ausencia de FK físicas.
-   [x] Mantener como `IntegerField` las relaciones sin integridad
    garantizada.
-   [x] Modelar `Calendar.sales_rep` como ForeignKey lógica con
    `db_constraint=False`.
-   [x] Agregar PK técnica a `dev_Detalle_Corregida`.
-   [x] Consolidar decisiones principales de `models.py`.

## Fase 3 --- API GET

-   [x] Crear `serializers.py`.
-   [x] Crear serializers para los seis modelos principales.
-   [x] Crear `ReadOnlyModelViewSet`.
-   [x] Configurar `DefaultRouter` y URLs.
-   [x] Crear endpoints GET de listado y detalle.
-   [x] Probar endpoints con Postman.
-   [x] Configurar paginación global de 50 registros.
-   [x] Ordenar QuerySets por `id`.
-   [x] Resolver vendedores inexistentes de forma segura.

## Fase 4 --- Relaciones y serializers enriquecidos

-   [x] Manejar valores `0` e IDs huérfanos.
-   [x] Incorporar datos de vendedor cuando existe.
-   [x] Crear serializer anidado para `Calendar`.
-   [x] Crear lista de vendedores para `Account`.
-   [x] Usar `select_related('sales_rep')` en `Calendar`.
-   [x] Optimizar `Activity`, `Opportunity` y `Account` para evitar
    consultas N+1.

## Fase 5 --- JWT

-   [x] Aplicar migraciones internas de autenticación de Django.
-   [x] Crear usuario Django de autenticación.
-   [x] Configurar SimpleJWT.
-   [x] Habilitar login/token y refresh.
-   [x] Proteger endpoints con `IsAuthenticated`.
-   [x] Validar 401 sin token y 200 con Bearer access.
-   [x] Validar renovación mediante refresh.
-   [x] Configurar duración explícita de access y refresh.
-   [x] Mantener separación entre `ForceUser` y usuarios de
    autenticación Django.

## Fase 6 --- Permisos

-   [ ] Definir roles.
-   [ ] Implementar permisos.
-   [ ] Diferenciar usuario normal y administrador.

## Fase 7 --- Tablas manuales CIC

-   [ ] `MovilidadRegistro`.
-   [ ] `NotificacionesVendedores`.
-   [ ] `PresupuestoSegmentos`.
-   [ ] `ResumenMovilidad`.
-   [ ] `StrikesVendedores`.
-   [ ] `UsuariosCIC`.

## Fase 8 --- Carga de Excel

-   [ ] Diseñar endpoint y validar archivo.
-   [ ] Procesar datos y manejar errores/duplicados.
-   [ ] Garantizar que la carga preserve la PK técnica de
    `dev_Detalle_Corregida`.

## Fase 9 --- Análisis y filtros

-   [x] Instalar y configurar `django-filter`.
-   [x] Crear `DevDetalleCorregidaFilter`.
-   [x] Filtrar ventas por vendedor, representante, cliente, artículo y
    estado.
-   [x] Filtrar ventas por rango de fechas.
-   [x] Filtrar ventas por rango de `ingresosusd`.
-   [x] Agregar búsqueda parcial con `SearchFilter`.
-   [x] Agregar ordenamiento con `OrderingFilter`.
-   [x] Combinar filtros, búsqueda y ordenamiento en una misma consulta.
-   [x] Extender filtros a `Activity`.
-   [x] Extender filtros a `Calendar`.
-   [x] Extender filtros a `Opportunity`.
-   [x] Evaluar e implementar filtros para `Account`, incluido filtro
    personalizado por vendedor.
-   [ ] Crear indicadores comerciales y endpoints de análisis.

## Fase 10 --- Flutter

-   [ ] Definir contratos API/frontend.
-   [ ] Autenticación.
-   [ ] Consumo de endpoints.
-   [ ] Vistas CIC.

## Fase 11 --- Calidad y despliegue

-   [ ] Pruebas automatizadas.
-   [ ] Manejo uniforme de errores.
-   [ ] Logging y documentación API.
-   [ ] Optimización de consultas.
-   [ ] Configuración de producción.

## Checkpoint actual --- 2026-09-11

Las fases **0, 1, 2, 3, 4 y 5** están completadas.

La **Fase 9 --- Análisis y filtros** avanzó significativamente: ventas,
actividades, calendarios, oportunidades y cuentas cuentan con filtros de
negocio; además se habilitaron búsqueda y ordenamiento donde
corresponde.

Se completó la optimización N+1: - `Activity`: 52 → 3 consultas SQL. -
`Opportunity`: 3 consultas SQL tras la optimización. - `Account`: 8 → 4
consultas SQL.

El siguiente bloque será crear **indicadores comerciales y endpoints
agregados de análisis**. La fase 6 de permisos/roles continúa pendiente.
