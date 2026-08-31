# CIC — Roadmap

## Fase 0 — Preparación del proyecto
- [x] Crear entorno virtual
- [x] Crear proyecto Django
- [x] Crear app `forcesync`
- [x] Crear `requirements.txt`
- [ ] Crear/validar `.env`
- [ ] Crear/validar `.gitignore`

## Fase 1 — Conexión con ForceSyncDB_Worker
- [x] Configurar SQL Server
- [x] Verificar driver ODBC disponible
- [x] Configurar ODBC Driver 17
- [x] Conectarse mediante `dbshell`
- [x] Confirmar base `ForceSyncDB_Worker`
- [x] Consultar datos reales de `Users`

## Fase 2 — Modelado de tablas existentes
- [x] Ejecutar `inspectdb`
- [x] Generar modelos iniciales
- [x] Revisar `Users`
- [ ] Revisar `Activities`
- [ ] Revisar `Calendars`
- [ ] Revisar `Opportunities`
- [ ] Revisar `Accounts`
- [ ] Determinar la PK de `dev_Detalle_Corregida`
- [ ] Convertir relaciones confirmadas a `ForeignKey`
- [ ] Verificar `managed = False`

## Fase 3 — Primera API de lectura
- [ ] Crear serializers
- [ ] Definir campos públicos
- [ ] Crear `ReadOnlyModelViewSet` para `Users`
- [ ] Crear `ReadOnlyModelViewSet` para `Accounts`
- [ ] Crear `ReadOnlyModelViewSet` para `Activities`
- [ ] Crear `ReadOnlyModelViewSet` para `Calendars`
- [ ] Crear `ReadOnlyModelViewSet` para `Opportunities`
- [ ] Resolver endpoint de `dev_Detalle_Corregida`
- [ ] Crear Routers
- [ ] Configurar URLs
- [ ] Probar GET lista en Postman
- [ ] Probar GET detalle en Postman

## Fase 4 — Relaciones y serializers anidados
- [ ] Serializer de `Users`
- [ ] Serializer anidado de `Activities` → `Users`
- [ ] Serializer anidado de `Calendars` → `Users`
- [ ] Serializer anidado de `Opportunities` → `Users`
- [ ] Serializers de `Accounts` con múltiples vendedores
- [ ] Revisar `related_name`
- [ ] Utilizar `select_related`
- [ ] Crear filtros por vendedor

## Fase 5 — Autenticación
- [ ] Configurar Django REST Framework
- [ ] Instalar/configurar Simple JWT
- [ ] Crear login
- [ ] Crear refresh token
- [ ] Crear endpoint de perfil
- [ ] Proteger endpoints con `IsAuthenticated`
- [ ] Probar Bearer Token desde Postman

## Fase 6 — Permisos y roles
- [ ] Analizar roles necesarios
- [ ] Crear permisos personalizados
- [ ] Separar acceso administrativo y de consulta
- [ ] Probar diferencias entre usuarios
- [ ] Documentar matriz de permisos

## Fase 7 — Datos manuales del CIC
Incorporar progresivamente:

- [ ] `MovilidadRegistro`
- [ ] `NotificacionesVendedores`
- [ ] `PresupuestoSegmentos`
- [ ] `ResumenMovilidad`
- [ ] `StrikesVendedores`
- [ ] `UsuariosCIC`

En esta fase se determinará cuáles endpoints serán de lectura y cuáles necesitarán operaciones de escritura.

## Fase 8 — Carga de Excel
- [ ] Analizar flujo actual de `dev_Detalle_Corregida`
- [ ] Definir endpoint para carga de Excel
- [ ] Validar estructura del archivo
- [ ] Validar registros
- [ ] Definir estrategia de inserción/actualización
- [ ] Registrar errores de importación

## Fase 9 — Consultas y análisis
- [ ] Filtros
- [ ] Búsqueda
- [ ] Paginación
- [ ] Ordenamiento
- [ ] Consultas agregadas
- [ ] Indicadores comerciales
- [ ] Indicadores de movilidad
- [ ] Consultas optimizadas

## Fase 10 — Integración Flutter
- [ ] Definir contrato final de endpoints
- [ ] Consumir JWT desde Flutter
- [ ] Consumir usuarios
- [ ] Consumir cuentas
- [ ] Consumir actividades
- [ ] Consumir calendarios
- [ ] Consumir oportunidades
- [ ] Consumir datos de ventas
- [ ] Implementar manejo de errores
- [ ] Implementar expiración/refresh del token

## Fase 11 — Calidad y despliegue
- [ ] Tests unitarios
- [ ] Tests de API
- [ ] Validaciones
- [ ] Manejo consistente de errores
- [ ] Logging
- [ ] Variables de entorno de producción
- [ ] Configuración de CORS
- [ ] Documentación de API
- [ ] Preparar despliegue

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
