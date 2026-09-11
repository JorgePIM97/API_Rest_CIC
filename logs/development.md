# CIC — Development Log

## Estado actual

**Proyecto:** Centro de Inteligencia Comercial (CIC)  
**Versión:** 2.0 en desarrollo  
**Fecha de actualización:** 2026-08-31

## Objetivo

Construir una API REST con Django REST Framework como evolución del proyecto existente de análisis de ventas y movilidad de vendedores.

La API se conectará a la base de datos SQL Server existente **ForceSyncDB_Worker**. En la primera etapa no se modificará la información de las tablas de Force Manager; la API comenzará como una API de consulta.

### Tablas iniciales

- `Accounts`
- `Activities`
- `Calendars`
- `dev_Detalle_Corregida`
- `Opportunities`
- `Users`

### Tablas para etapas posteriores

- `MovilidadRegistro`
- `NotificacionesVendedores`
- `PresupuestoSegmentos`
- `ResumenMovilidad`
- `StrikesVendedores`
- `UsuariosCIC`

## Arquitectura inicial

```text
ForceSyncDB_Worker (SQL Server)
        |
        | Django ORM
        v
Django + Django REST Framework
        |
        | JWT + permisos
        v
Flutter / cliente consumidor
```

La aplicación `forcesync` se encargará inicialmente de los modelos que representan los datos existentes provenientes de Force Manager.

## Estructura inicial

```text
cic_api/
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── forcesync/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── migrations/
└── logs/
    ├── dev_log.csv
    ├── development.md
    └── roadmap.md
```

## Trabajo realizado

### 1. Creación del proyecto

Se creó un proyecto Django nuevo para CIC y una aplicación llamada `forcesync`.

### 2. Dependencias

Se definieron las dependencias necesarias para trabajar con:

- Django
- Django REST Framework
- Simple JWT
- python-dotenv
- mssql-django
- pyodbc

### 3. Conexión a SQL Server

Se configuró Django para utilizar la base existente:

```text
ForceSyncDB_Worker
```

La configuración utiliza variables de entorno para evitar almacenar credenciales directamente en el código.

El driver ODBC disponible y seleccionado es:

```text
ODBC Driver 17 for SQL Server
```

### 4. Prueba de conexión

Se ejecutó:

```powershell
python manage.py dbshell
```

La conexión fue exitosa.

Se verificó:

```sql
SELECT DB_NAME() AS BaseDeDatos;
GO
```

Resultado:

```text
ForceSyncDB_Worker
```

### 5. Prueba de datos

Se consultó la tabla `Users`:

```sql
SELECT TOP 5
    Id,
    Name,
    LastName,
    Email,
    IsActive
FROM Users;
GO
```

Se obtuvieron registros reales, confirmando que Django puede consultar la base existente.

### 6. Inspección de modelos

Se utilizó:

```powershell
python manage.py inspectdb Users Accounts Activities Calendars Opportunities > models_generados.py
```

Esto permitió generar una primera representación Django de las tablas existentes.

`dev_Detalle_Corregida` quedó fuera de esta primera inspección porque en el esquema compartido no se identificó una clave primaria declarada.

### 7. Revisión de `Users`

El modelo generado para `Users` contiene:

```python
id = models.IntegerField(db_column='Id', primary_key=True)
```

y:

```python
class Meta:
    managed = False
    db_table = 'Users'
```

Se determinó que `managed = False` es apropiado porque las tablas pertenecen a una base existente que es alimentada por otros procesos.

También se decidió mantener inicialmente el modelo completo y controlar los campos expuestos por la API mediante serializers.

## Relaciones identificadas

```text
Calendars.SalesRepId_Id
        -> Users.Id

Opportunities.SalesRepId_Id
        -> Users.Id

Activities.SalesRepId_Id
        -> Users.Id

Accounts.SalesRepId1_Id
        -> Users.Id

Accounts.SalesRepId2_Id
        -> Users.Id

Accounts.SalesRepId3_Id
        -> Users.Id

Accounts.SalesRepId4_Id
        -> Users.Id

Accounts.SalesRepId5_Id
        -> Users.Id

dev_Detalle_Corregida.Id_Vendedor_FM
        -> Users.Id
```

Estas relaciones serán revisadas antes de convertir los campos enteros generados por `inspectdb` en `ForeignKey`.

## Decisiones técnicas actuales

1. Las tablas existentes de ForceSyncDB_Worker no serán creadas ni administradas por Django.
2. Se utilizará `managed = False` para estos modelos.
3. La primera versión de los endpoints será únicamente de lectura.
4. Se utilizarán `ReadOnlyModelViewSet` y Routers para los endpoints iniciales.
5. Se utilizarán serializers para controlar qué campos se exponen.
6. Las relaciones con `Users` se modelarán con `ForeignKey` cuando se hayan verificado.
7. JWT y permisos se incorporarán después de tener funcionando la API de lectura.
8. No se debe inventar una primary key para `dev_Detalle_Corregida`; primero se debe determinar cómo identificar un registro de forma segura.

## Pendiente inmediato

Revisar los modelos generados de:

- `Activities`
- `Calendars`
- `Opportunities`
- `Accounts`

y convertir las relaciones confirmadas con `Users` en relaciones ORM apropiadas.

Después:

```text
Models
  ↓
Serializers
  ↓
ReadOnlyModelViewSet
  ↓
Routers
  ↓
GET
  ↓
Postman
```

## Estado actual

### Conexión con SQL Server
La conexión entre Django y SQL Server fue validada correctamente mediante `python manage.py dbshell`. La base confirmada es `ForceSyncDB_Worker`.

### Convención de modelos
| SQL Server | Django |
|---|---|
| `Users` | `ForceUser` |
| `Accounts` | `Account` |
| `Activities` | `Activity` |
| `Calendars` | `Calendar` |
| `Opportunities` | `Opportunity` |
| `dev_Detalle_Corregida` | `DevDetalleCorregida` |

Los modelos de tablas existentes se mantienen con `managed = False`.

## ForceUser
Se renombró el modelo `Users` a `ForceUser`, manteniendo `db_table = 'Users'`.

Se agregó:

```python
def __str__(self):
    return f"{self.name} {self.lastname}"
```

Pruebas realizadas:

```python
ForceUser.objects.count()
```

Resultado: `81`.

También se validó la consulta de los primeros cinco usuarios y la representación legible de objetos.

## Activity
Se incorporó `Activity` a partir de `inspectdb` y se validó lectura ORM.

Ejemplo de relación lógica comprobada:

```text
Activity.salesrepid_id = 69
→ ForceUser.id = 69
→ SILVINO LOPEZ
```

## Integridad de relaciones con Users
SQL Server no contiene restricciones `FOREIGN KEY` físicas para las tablas analizadas.

### Activities → Users
| Estado | Cantidad |
|---|---:|
| Válido | 55,266 |
| ID sin usuario | 1 |
| 0 | 5 |

### Calendars → Users
| Estado | Cantidad |
|---|---:|
| Válido | 20,473 |
| NULL | 6 |

### Opportunities → Users
| Estado | Cantidad |
|---|---:|
| Válido | 5,812 |
| ID sin usuario | 2 |
| 0 | 4 |

### Accounts → Users
Se comprobó que `SalesRepId1_Id` a `SalesRepId5_Id` contienen IDs que pueden corresponder con vendedores de `Users`, pero también pueden existir valores `0`, `NULL` o datos históricos sin correspondencia.

## Prueba temporal de ForeignKey en Activity
Se probó temporalmente:

```python
sales_rep = models.ForeignKey(
    ForceUser,
    on_delete=models.DO_NOTHING,
    db_column='SalesRepId_Id',
    related_name='activities',
    blank=True,
    null=True,
    db_constraint=False,
)
```

Funcionó correctamente para IDs válidos. Por ejemplo:

```python
activity.sales_rep
```

devolvió `SILVINO LOPEZ`.

La relación inversa también funcionó:

```python
user.activities.count()
```

Resultado para `ForceUser.id = 69`: `62`.

Sin embargo, al consultar una actividad con `SalesRepId_Id = 0`:

```python
Activity.objects.get(id=428).sales_rep
```

Django produjo `ForceUser.DoesNotExist`.

### Decisión de diseño
Para relaciones cuya integridad no está garantizada se conservará el identificador como `IntegerField` y la asociación se resolverá de forma segura en la capa de API.

Ejemplo:

```python
ForceUser.objects.filter(id=activity.salesrepid_id).first()
```

Así un ID inexistente devuelve `None` en lugar de producir una excepción.

## dev_Detalle_Corregida
`inspectdb` generó `DevDetalleCorregida` con `managed = False` y `db_table = 'dev_Detalle_Corregida'`.

El campo relevante es:

```python
id_vendedor_fm = models.IntegerField(
    db_column='Id_Vendedor_FM',
    blank=True,
    null=True
)
```

### Validación de Id_Vendedor_FM
| Estado | Cantidad |
|---|---:|
| ID válido en Users | 3,808 |
| 0 | 5,752 |

Relación con `RepresentanteDeVentas`:

| Tipo | Cantidad |
|---|---:|
| ID + VENDEDOR | 3,808 |
| 0 + PISO | 5,598 |
| 0 + NO PISO | 154 |

Los 154 casos `0 + NO PISO` son:

| RepresentanteDeVentas | Cantidad |
|---|---:|
| Patio GPA Technical Services | 90 |
| Rafael Arango | 63 |
| GPA | 1 |

### Regla de negocio identificada
`Id_Vendedor_FM > 0` representa un vendedor asociado a `Users.Id`.

`Id_Vendedor_FM = 0` indica que no existe asociación válida con un usuario concreto de Force Manager. La mayoría corresponde a representantes `Piso...`, aunque también existen otros representantes especiales.

Por este motivo `DevDetalleCorregida.id_vendedor_fm` permanecerá como `IntegerField`.

## Principio adoptado para la base heredada
No se convertirá automáticamente a `ForeignKey` cualquier columna que parezca contener un ID. Antes se validarán estructura, restricciones SQL, calidad de datos y significado de negocio.

## Próximo paso
Continuar incorporando y validando `Calendar`, `Opportunity`, `Account` y `DevDetalleCorregida` en `forcesync/models.py`. Después se iniciará la primera API GET con Django REST Framework.

## Estado actual
Las fases de conexión, modelado inicial y primera API GET están completadas. Los seis recursos principales ya pueden consultarse mediante endpoints REST de solo lectura, con paginación global.

## Convención de modelos
| SQL Server | Django |
|---|---|
| `Users` | `ForceUser` |
| `Accounts` | `Account` |
| `Activities` | `Activity` |
| `Calendars` | `Calendar` |
| `Opportunities` | `Opportunity` |
| `dev_Detalle_Corregida` | `DevDetalleCorregida` |

Los modelos de tablas existentes se mantienen con `managed = False`.

## Modelos validados

### ForceUser
- `db_table = 'Users'`.
- Se agregó `__str__` con nombre y apellido.
- ORM validado: **81 registros**.

### Activity
- ORM validado.
- `SalesRepId_Id`: **55,266 válidos, 5 con valor 0 y 1 ID sin usuario**.
- `salesrepid_id` permanece como `IntegerField`.
- La prueba temporal como `ForeignKey` demostró que un valor 0 puede producir `ForceUser.DoesNotExist`.

### Calendar
- ORM validado: **20,487 registros** en la validación más reciente.
- **20,481 IDs válidos y 6 NULL**.
- `sales_rep` se modeló como `ForeignKey` lógica a `ForceUser`, con `db_constraint=False`.
- `ForceUser.id=69` devolvió **183 calendarios**.
- Calendar `115` resolvió vendedor 69; Calendar `112` resolvió `None`.

> La tabla es alimentada externamente y puede cambiar, por lo que los conteos pueden variar entre validaciones.

### Opportunity
- ORM validado: **5,820 registros**.
- `salesrepid_id` permanece como `IntegerField` por valores 0 e IDs huérfanos.
- id `101` → vendedor 0.
- id `105` → vendedor 51 sin `ForceUser`.
- id `107` → vendedor 69 válido.

### Account
- ORM validado: **7,033 registros**.
- `SalesRepId1_Id` a `SalesRepId5_Id` permanecen como `IntegerField`.
- Pueden contener IDs válidos, `0`, `NULL` o IDs sin usuario.
- Account `393` confirmó cuatro vendedores válidos.
- Account `386` confirmó el caso 0/NULL.

### DevDetalleCorregida
El origen es una consulta/exportación de ventas de NetSuite cargada a SQL Server mediante Excel.

La tabla originalmente no tenía PK ni índice único. Se agregó una PK técnica `Id BIGINT IDENTITY(1,1)` con restricción `PK_dev_Detalle_Corregida`. `inspectdb` la detectó como:

```python
id = models.BigAutoField(db_column='Id', primary_key=True)
```

ORM validado: **9,560 registros**.

`Id_Vendedor_FM` permanece como `IntegerField`: 3,808 registros tienen vendedor válido y 5,752 tienen valor 0.

## Principio para relaciones heredadas
No se convierte automáticamente a `ForeignKey` una columna solo porque contenga un ID. Antes se revisan restricciones SQL, valores NULL/0, IDs huérfanos y significado de negocio. Si la integridad no está garantizada, se conserva `IntegerField` y la asociación se resuelve de forma segura en la API.

## Capa REST

### Serializers
Se creó `forcesync/serializers.py` con:
- `ForceUserSerializer`
- `ActivitySerializer`
- `CalendarSerializer`
- `OpportunitySerializer`
- `AccountSerializer`
- `DevDetalleCorregidaSerializer`

`Activity` y `Opportunity` usan `SerializerMethodField` para resolver vendedores de forma segura. `Calendar` usa `ForceUserSerializer` anidado mediante `source='sales_rep'`. `Account` agrega el campo calculado `vendedores`.

### ViewSets
Los seis recursos usan `ReadOnlyModelViewSet`, por lo que esta primera API expone lectura y no escritura sobre las tablas de origen.

`CalendarViewSet` usa:

```python
Calendar.objects.select_related('sales_rep').order_by('id')
```

### Endpoints
| Recurso | Listado | Detalle |
|---|---|---|
| Usuarios | `GET /api/usuarios/` | `GET /api/usuarios/<id>/` |
| Actividades | `GET /api/actividades/` | `GET /api/actividades/<id>/` |
| Calendarios | `GET /api/calendarios/` | `GET /api/calendarios/<id>/` |
| Oportunidades | `GET /api/oportunidades/` | `GET /api/oportunidades/<id>/` |
| Cuentas | `GET /api/cuentas/` | `GET /api/cuentas/<id>/` |
| Ventas | `GET /api/ventas/` | `GET /api/ventas/<id>/` |

Los endpoints probados respondieron **200 OK**.

### Paginación
Configuración global:

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
}
```

Los QuerySets se ordenan por `id` para mantener una paginación estable.

## Rendimiento pendiente
`ActivitySerializer`, `OpportunitySerializer` y especialmente `AccountSerializer` pueden ejecutar consultas adicionales a `ForceUser` durante la serialización. La implementación actual es funcional, pero debe optimizarse antes de producción para evitar N+1.

## Próximo paso
**Fase 5 — JWT:** configurar SimpleJWT, login/refresh, proteger endpoints y mantener separados los usuarios de autenticación Django de `ForceUser`.

## Estado actual
La API de solo lectura para los seis recursos principales está operativa. La autenticación JWT básica está completada y los endpoints de negocio están protegidos globalmente. Además, el endpoint de ventas ya soporta filtros exactos, rangos, búsqueda parcial y ordenamiento.

## Convención de modelos
| SQL Server | Django |
|---|---|
| `Users` | `ForceUser` |
| `Accounts` | `Account` |
| `Activities` | `Activity` |
| `Calendars` | `Calendar` |
| `Opportunities` | `Opportunity` |
| `dev_Detalle_Corregida` | `DevDetalleCorregida` |

Los modelos de tablas existentes se mantienen con `managed = False`.

## Modelos validados

### ForceUser
- `db_table = 'Users'`.
- Se agregó `__str__` con nombre y apellido.
- ORM validado: **81 registros**.

### Activity
- ORM validado.
- `SalesRepId_Id`: **55,266 válidos, 5 con valor 0 y 1 ID sin usuario**.
- `salesrepid_id` permanece como `IntegerField`.
- La prueba temporal como `ForeignKey` demostró que un valor 0 puede producir `ForceUser.DoesNotExist`.

### Calendar
- ORM validado: **20,487 registros** en la validación más reciente.
- **20,481 IDs válidos y 6 NULL**.
- `sales_rep` se modeló como `ForeignKey` lógica a `ForceUser`, con `db_constraint=False`.
- `ForceUser.id=69` devolvió **183 calendarios**.
- Calendar `115` resolvió vendedor 69; Calendar `112` resolvió `None`.

> La tabla es alimentada externamente y puede cambiar, por lo que los conteos pueden variar entre validaciones.

### Opportunity
- ORM validado: **5,820 registros**.
- `salesrepid_id` permanece como `IntegerField` por valores 0 e IDs huérfanos.
- id `101` → vendedor 0.
- id `105` → vendedor 51 sin `ForceUser`.
- id `107` → vendedor 69 válido.

### Account
- ORM validado: **7,033 registros**.
- `SalesRepId1_Id` a `SalesRepId5_Id` permanecen como `IntegerField`.
- Pueden contener IDs válidos, `0`, `NULL` o IDs sin usuario.
- Account `393` confirmó cuatro vendedores válidos.
- Account `386` confirmó el caso 0/NULL.

### DevDetalleCorregida
El origen es una consulta/exportación de ventas de NetSuite cargada a SQL Server mediante Excel.

La tabla originalmente no tenía PK ni índice único. Se agregó una PK técnica `Id BIGINT IDENTITY(1,1)` con restricción `PK_dev_Detalle_Corregida`. `inspectdb` la detectó como:

```python
id = models.BigAutoField(db_column='Id', primary_key=True)
```

ORM validado: **9,560 registros**.

`Id_Vendedor_FM` permanece como `IntegerField`: 3,808 registros tienen vendedor válido y 5,752 tienen valor 0.

## Principio para relaciones heredadas
No se convierte automáticamente a `ForeignKey` una columna solo porque contenga un ID. Antes se revisan restricciones SQL, valores NULL/0, IDs huérfanos y significado de negocio. Si la integridad no está garantizada, se conserva `IntegerField` y la asociación se resuelve de forma segura en la API.

## Capa REST

### Serializers
`forcesync/serializers.py` contiene:
- `ForceUserSerializer`
- `ActivitySerializer`
- `CalendarSerializer`
- `OpportunitySerializer`
- `AccountSerializer`
- `DevDetalleCorregidaSerializer`

`Activity` y `Opportunity` usan `SerializerMethodField` para resolver vendedores de forma segura. `Calendar` usa `ForceUserSerializer` anidado mediante `source='sales_rep'`. `Account` agrega el campo calculado `vendedores`.

### ViewSets
Los seis recursos usan `ReadOnlyModelViewSet`, evitando escritura sobre las tablas de origen.

`CalendarViewSet` usa:

```python
Calendar.objects.select_related('sales_rep').order_by('id')
```

### Endpoints
| Recurso | Listado | Detalle |
|---|---|---|
| Usuarios | `GET /api/usuarios/` | `GET /api/usuarios/<id>/` |
| Actividades | `GET /api/actividades/` | `GET /api/actividades/<id>/` |
| Calendarios | `GET /api/calendarios/` | `GET /api/calendarios/<id>/` |
| Oportunidades | `GET /api/oportunidades/` | `GET /api/oportunidades/<id>/` |
| Cuentas | `GET /api/cuentas/` | `GET /api/cuentas/<id>/` |
| Ventas | `GET /api/ventas/` | `GET /api/ventas/<id>/` |

### Paginación
Se mantiene `PageNumberPagination` global con `PAGE_SIZE = 50`. Los QuerySets se ordenan por `id` para mantener una paginación estable.

## Fase 5 — Autenticación JWT

### Migraciones y usuario Django
Se aplicaron las migraciones internas de `contenttypes`, `auth`, `admin` y `sessions`. La app `forcesync` continúa sin migraciones propias por trabajar con tablas heredadas `managed=False`.

Se creó un superusuario Django para autenticación. Se mantiene la separación conceptual:
- `auth_user`: credenciales y autenticación de la API.
- `ForceUser`: usuarios/vendedores procedentes de la base externa.

### SimpleJWT
SimpleJWT está configurado como autenticación de DRF y `IsAuthenticated` como permiso global.

Endpoints:
- `POST /api/token/`
- `POST /api/token/refresh/`

Pruebas completadas:
- obtención de `access` + `refresh` → **200 OK**;
- endpoint protegido sin token → **401 Unauthorized**;
- endpoint protegido con Bearer access → **200 OK**;
- renovación mediante refresh → **200 OK**.

La duración de `access` y `refresh` quedó definida explícitamente mediante `SIMPLE_JWT` en `config/settings.py`.

## Filtros y consultas de ventas

Se instaló **django-filter 26.1** y se creó `forcesync/filters.py` con `DevDetalleCorregidaFilter`.

### Filtros exactos
- `id_vendedor_fm`
- `representantedeventas`
- `nombrecliente`
- `articulo`
- `estadotransaccion`

### Rangos de fecha
- `fecha_desde` → `fecha >= valor`
- `fecha_hasta` → `fecha <= valor`

Ejemplo:

```text
/api/ventas/?fecha_desde=2025-06-01&fecha_hasta=2025-06-30
```

### Rangos de ingresos USD
- `ingresosusd_min` → `ingresosusd >= valor`
- `ingresosusd_max` → `ingresosusd <= valor`

### SearchFilter
Búsqueda parcial habilitada sobre:
- `nombrecliente`
- `representantedeventas`
- `articulo`
- `numerodedocumento`

Ejemplo:

```text
/api/ventas/?search=MONCLOVA
```

### OrderingFilter
Ordenamiento habilitado para:
- `fecha`
- `ingresos`
- `ingresosusd`
- `representantedeventas`
- `nombrecliente`
- `articulo`

Ejemplo:

```text
/api/ventas/?search=Adan&fecha_desde=2025-06-01&fecha_hasta=2025-06-30&ordering=-ingresosusd
```

La consulta anterior fue validada con **200 OK**, al igual que el orden ascendente por `ingresosusd`.

## Rendimiento pendiente
`ActivitySerializer`, `OpportunitySerializer` y especialmente `AccountSerializer` pueden ejecutar consultas adicionales a `ForceUser` durante la serialización. Debe optimizarse este patrón N+1 antes de producción.

## Próximo paso
Extender el patrón de filtros y consultas de negocio a **Activity, Calendar y Opportunity**, definiendo para cada recurso filtros por vendedor, fechas y campos relevantes. Posteriormente se abordarán permisos/roles y el resto de indicadores comerciales.

## Estado actual

La API de solo lectura para los seis recursos principales está
operativa. La autenticación JWT básica está completada y los endpoints
de negocio están protegidos globalmente. Los endpoints de ventas,
actividades, calendarios, oportunidades y cuentas ya soportan filtros de
negocio, búsqueda y/o ordenamiento según el recurso. También se completó
la optimización del patrón N+1 en Activity, Opportunity y Account.

## Convención de modelos

  SQL Server                Django
  ------------------------- -----------------------
  `Users`                   `ForceUser`
  `Accounts`                `Account`
  `Activities`              `Activity`
  `Calendars`               `Calendar`
  `Opportunities`           `Opportunity`
  `dev_Detalle_Corregida`   `DevDetalleCorregida`

Los modelos de tablas existentes se mantienen con `managed = False`.

## Modelos validados

### ForceUser

-   `db_table = 'Users'`.
-   Se agregó `__str__` con nombre y apellido.
-   ORM validado: **81 registros**.

### Activity

-   ORM validado.
-   `SalesRepId_Id`: **55,266 válidos, 5 con valor 0 y 1 ID sin
    usuario**.
-   `salesrepid_id` permanece como `IntegerField`.
-   La prueba temporal como `ForeignKey` demostró que un valor 0 puede
    producir `ForceUser.DoesNotExist`.

### Calendar

-   ORM validado: **20,487 registros** en la validación más reciente.
-   **20,481 IDs válidos y 6 NULL**.
-   `sales_rep` se modeló como `ForeignKey` lógica a `ForceUser`, con
    `db_constraint=False`.
-   `ForceUser.id=69` devolvió **183 calendarios**.
-   Calendar `115` resolvió vendedor 69; Calendar `112` resolvió `None`.

> La tabla es alimentada externamente y puede cambiar, por lo que los
> conteos pueden variar entre validaciones.

### Opportunity

-   ORM validado: **5,820 registros**.
-   `salesrepid_id` permanece como `IntegerField` por valores 0 e IDs
    huérfanos.
-   id `101` → vendedor 0.
-   id `105` → vendedor 51 sin `ForceUser`.
-   id `107` → vendedor 69 válido.

### Account

-   ORM validado: **7,033 registros**.
-   `SalesRepId1_Id` a `SalesRepId5_Id` permanecen como `IntegerField`.
-   Pueden contener IDs válidos, `0`, `NULL` o IDs sin usuario.
-   Account `393` confirmó cuatro vendedores válidos.
-   Account `386` confirmó el caso 0/NULL.

### DevDetalleCorregida

El origen es una consulta/exportación de ventas de NetSuite cargada a
SQL Server mediante Excel.

La tabla originalmente no tenía PK ni índice único. Se agregó una PK
técnica `Id BIGINT IDENTITY(1,1)` con restricción
`PK_dev_Detalle_Corregida`. `inspectdb` la detectó como:

``` python
id = models.BigAutoField(db_column='Id', primary_key=True)
```

ORM validado: **9,560 registros**.

`Id_Vendedor_FM` permanece como `IntegerField`: 3,808 registros tienen
vendedor válido y 5,752 tienen valor 0.

## Principio para relaciones heredadas

No se convierte automáticamente a `ForeignKey` una columna solo porque
contenga un ID. Antes se revisan restricciones SQL, valores NULL/0, IDs
huérfanos y significado de negocio. Si la integridad no está
garantizada, se conserva `IntegerField` y la asociación se resuelve de
forma segura en la API.

## Capa REST

### Serializers

`forcesync/serializers.py` contiene: - `ForceUserSerializer` -
`ActivitySerializer` - `CalendarSerializer` - `OpportunitySerializer` -
`AccountSerializer` - `DevDetalleCorregidaSerializer`

`Activity` y `Opportunity` usan `SerializerMethodField` para resolver
vendedores de forma segura. `Calendar` usa `ForceUserSerializer` anidado
mediante `source='sales_rep'`. `Account` agrega el campo calculado
`vendedores`.

### ViewSets

Los seis recursos usan `ReadOnlyModelViewSet`, evitando escritura sobre
las tablas de origen.

`CalendarViewSet` usa:

``` python
Calendar.objects.select_related('sales_rep').order_by('id')
```

### Endpoints

  ------------------------------------------------------------------------------------
  Recurso                 Listado                     Detalle
  ----------------------- --------------------------- --------------------------------
  Usuarios                `GET /api/usuarios/`        `GET /api/usuarios/<id>/`

  Actividades             `GET /api/actividades/`     `GET /api/actividades/<id>/`

  Calendarios             `GET /api/calendarios/`     `GET /api/calendarios/<id>/`

  Oportunidades           `GET /api/oportunidades/`   `GET /api/oportunidades/<id>/`

  Cuentas                 `GET /api/cuentas/`         `GET /api/cuentas/<id>/`

  Ventas                  `GET /api/ventas/`          `GET /api/ventas/<id>/`
  ------------------------------------------------------------------------------------

### Paginación

Se mantiene `PageNumberPagination` global con `PAGE_SIZE = 50`. Los
QuerySets se ordenan por `id` para mantener una paginación estable.

## Fase 5 --- Autenticación JWT

### Migraciones y usuario Django

Se aplicaron las migraciones internas de `contenttypes`, `auth`, `admin`
y `sessions`. La app `forcesync` continúa sin migraciones propias por
trabajar con tablas heredadas `managed=False`.

Se creó un superusuario Django para autenticación. Se mantiene la
separación conceptual: - `auth_user`: credenciales y autenticación de la
API. - `ForceUser`: usuarios/vendedores procedentes de la base externa.

### SimpleJWT

SimpleJWT está configurado como autenticación de DRF y `IsAuthenticated`
como permiso global.

Endpoints: - `POST /api/token/` - `POST /api/token/refresh/`

Pruebas completadas: - obtención de `access` + `refresh` → **200 OK**; -
endpoint protegido sin token → **401 Unauthorized**; - endpoint
protegido con Bearer access → **200 OK**; - renovación mediante refresh
→ **200 OK**.

La duración de `access` y `refresh` quedó definida explícitamente
mediante `SIMPLE_JWT` en `config/settings.py`.

## Filtros y consultas de ventas

Se instaló **django-filter 26.1** y se creó `forcesync/filters.py` con
`DevDetalleCorregidaFilter`.

### Filtros exactos

-   `id_vendedor_fm`
-   `representantedeventas`
-   `nombrecliente`
-   `articulo`
-   `estadotransaccion`

### Rangos de fecha

-   `fecha_desde` → `fecha >= valor`
-   `fecha_hasta` → `fecha <= valor`

Ejemplo:

``` text
/api/ventas/?fecha_desde=2025-06-01&fecha_hasta=2025-06-30
```

### Rangos de ingresos USD

-   `ingresosusd_min` → `ingresosusd >= valor`
-   `ingresosusd_max` → `ingresosusd <= valor`

### SearchFilter

Búsqueda parcial habilitada sobre: - `nombrecliente` -
`representantedeventas` - `articulo` - `numerodedocumento`

Ejemplo:

``` text
/api/ventas/?search=MONCLOVA
```

### OrderingFilter

Ordenamiento habilitado para: - `fecha` - `ingresos` - `ingresosusd` -
`representantedeventas` - `nombrecliente` - `articulo`

Ejemplo:

``` text
/api/ventas/?search=Adan&fecha_desde=2025-06-01&fecha_hasta=2025-06-30&ordering=-ingresosusd
```

La consulta anterior fue validada con **200 OK**, al igual que el orden
ascendente por `ingresosusd`.

## Filtros extendidos --- 2026-09-10

### Activity

Se creó `ActivityFilter` con filtros por vendedor, cuenta, tipo, tipo de
check-in y rango de fechas sobre `date`. `ActivityViewSet` incorpora
`SearchFilter` y `OrderingFilter`. Las pruebas por vendedor, rango de
fechas y ordenamiento devolvieron **200 OK**.

### Calendar

Se creó `CalendarFilter`. Durante la validación se comprobó mediante
`_meta` que: - `startdate` es `TextField`; - `enddate` es
`DateTimeField`.

Por esta razón, `fecha_desde`, `fecha_hasta` y el ordenamiento
cronológico utilizan `enddate`. El filtro por `sales_rep=69`, rango de
fechas 2026 y `ordering=-enddate` fue validado con **200 OK**.

### Opportunity

Se creó `OpportunityFilter` usando `datecreated` para `fecha_desde` y
`fecha_hasta`. También se habilitaron filtros por vendedor, estado, tipo
y cuenta, además de búsqueda textual y ordenamiento. Las pruebas
devolvieron **200 OK**.

### Account

Se creó `AccountFilter` con filtros básicos, búsqueda y ordenamiento. Se
agregó el parámetro personalizado `vendedor`, que utiliza `Q` para
localizar un vendedor en cualquiera de `salesrepid1_id` a
`salesrepid5_id`.

Ejemplo validado:

``` text
/api/cuentas/?vendedor=69
```

Resultado: **200 OK**.

## Optimización de consultas N+1

Se eliminó el patrón de consultas repetitivas a `ForceUser` en los
serializers de `Activity`, `Opportunity` y `Account`.

La estrategia consiste en cargar los vendedores necesarios en bloque
desde el ViewSet y exponerlos mediante `vendedores_cache` en el contexto
del serializer.

Resultados medidos: - `Activity`: **52 → 3 consultas SQL**. -
`Opportunity`: **3 consultas SQL** después de eliminar el patrón N+1. -
`Account`: primera optimización **8 consultas**; segunda optimización
usando una sola consulta `values_list` para los cinco campos de
vendedor: **4 consultas SQL**.

La estructura de las respuestas JSON se mantuvo durante las pruebas.

## Próximo paso

Crear **indicadores comerciales y endpoints agregados de análisis** para
que el futuro frontend Flutter consuma resultados calculados por la API
---por ejemplo ventas totales, ventas por vendedor y ventas por
periodo--- en lugar de descargar grandes cantidades de registros y
realizar las agregaciones localmente. La fase de permisos/roles continúa
pendiente.
